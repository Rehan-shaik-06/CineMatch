import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BASE = "https://api.tmdb.org/3"
IMG = "https://image.tmdb.org/t/p/w500"
FALLBACK = "https://placehold.co/500x750/141414/888888?text=No+Poster"


def get_key():
    key = os.getenv("TMDB_API_KEY")
    if not key:
        try:
            key = st.secrets["TMDB_API_KEY"]
        except Exception:
            key = None
    return key


@st.cache_data(ttl=86400, show_spinner=False)
def _fetch(movie_id):
    r = requests.get(
        f"{BASE}/movie/{movie_id}",
        params={"api_key": get_key()},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def get_movie_details(movie_id):
    """Returns a dict with poster, imdb link, year, rating, genres, overview. None if the request fails."""
    try:
        d = _fetch(int(movie_id))
    except Exception:
        return None

    imdb_id = d.get("imdb_id")
    title = d.get("title", "")
    return {
        "title": title,
        "poster": IMG + d["poster_path"] if d.get("poster_path") else FALLBACK,
        "imdb_url": f"https://www.imdb.com/title/{imdb_id}/"
        if imdb_id
        else f"https://www.imdb.com/find/?q={title}",
        "year": (d.get("release_date") or "")[:4],
        "rating": round(d.get("vote_average") or 0, 1),
        "genres": ", ".join(g["name"] for g in d.get("genres", [])[:2]),
        "overview": d.get("overview", ""),
    }