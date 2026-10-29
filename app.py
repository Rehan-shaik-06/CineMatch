import pandas as pd
import streamlit as st
import numpy as np
import html

from tmdb import get_movie_details

st.set_page_config(page_title="CineMatch", page_icon="🎬", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background:
            radial-gradient(ellipse at 50% -10%, rgba(140, 80, 20, 0.35), transparent 55%),
            #050505;
    }
    header[data-testid="stHeader"] { background: transparent; }

    .main-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 6rem;
    font-weight: 400;
    letter-spacing: 0.12em;
    text-align: center;
    margin: 2rem 0 0;
    background: linear-gradient(90deg, #FFE9B0, #F5A623, #E5670F);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 1.1rem;
    color: #D0D0D0;
    margin-bottom: 2rem;
    text-align: center;
}
    .subtitle b { color: #FFE9B0; }

    .stButton > button {
        background: #1C1C1C;
        color: #FFFFFF;
        border: 1px solid #2E2E2E;
        border-radius: 10px;
        padding: 0.6rem 1.8rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background: #262626;
        border-color: #F5A623;
        color: #FFE9B0;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(245, 166, 35, 0.15);
    }
    .card {
    display: block;
    text-decoration: none;
    background: #141414;
    border: 1px solid #2A2A2A;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
.card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: #F5A623;
    box-shadow: 0 16px 36px rgba(245, 166, 35, 0.2);
}
.card img { width: 100%; display: block; aspect-ratio: 2 / 3; object-fit: cover; }
.card-body { padding: 0.8rem 0.9rem 1rem; }
.card-title { color: #FFFFFF; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.3rem; }
.card-meta { color: #FFE9B0; font-size: 0.8rem; }
.card-genre { color: #9A9A9A; font-size: 0.78rem; margin-top: 0.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_movies():
    return pd.read_pickle("movies.pkl")


@st.cache_data
def load_neighbors():
    with np.load("neighbors.npz") as data:
        return data["idx"].copy()


neighbors = load_neighbors()

try:
    movies = load_movies()
except FileNotFoundError:
    st.error("movies.pkl not found. Put it in the same folder as app.py.")
    st.stop()

if "title" not in movies.columns:
    st.error(f"No 'title' column found. Columns are: {list(movies.columns)}")
    st.stop()

st.markdown('<h1 class="main-title">CINEMATCH</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Pick a movie you love. We\'ll find <b>five more</b> you\'ll enjoy.</p>',
    unsafe_allow_html=True,
)

_, mid, _ = st.columns([1, 2, 1])
with mid:
    selected = st.selectbox(
        "Search or choose a movie",
        movies["title"].values,
        index=None,
        placeholder="Search for a movie...",
        label_visibility="collapsed",
    )

if st.button("Recommend"):
    if selected is None:
        st.warning("Please choose a movie first.")
    else:
        neighbors = np.load("neighbors.npz")["idx"]
        pos = int((movies["title"] == selected).values.argmax())

        with st.spinner("Finding movies..."):
            cols = st.columns(5, gap="medium")
            for col, i in zip(cols, neighbors[pos][:5]):
                row = movies.iloc[i]
                d = get_movie_details(row["id"])
                with col:
                    if d is None:
                        st.warning(f"Couldn't load details for {row['title']}")
                        continue
                    title = html.escape(row["title"])
                    st.markdown(
                        f'<a class="card" href="{d["imdb_url"]}" target="_blank">'
                        f'<img src="{d["poster"]}" alt="{title}">'
                        f'<div class="card-body">'
                        f'<div class="card-title">{title}</div>'
                        f'<div class="card-meta">{d["year"]} · ⭐ {d["rating"]}</div>'
                        f'<div class="card-genre">{d["genres"]}</div>'
                        f'</div></a>',
                        unsafe_allow_html=True,
                    )

st.caption("This product uses the TMDB API but is not endorsed or certified by TMDB.")