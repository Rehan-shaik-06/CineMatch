# 🎬 CineMatch — Movie Recommendation System

Discover your next favorite movie with CineMatch! 🍿

CineMatch is a content-based movie recommendation system built using Python and Streamlit. Users select a movie they enjoy, and the application recommends five similar movies using precomputed similarity-based recommendations.

## 🌐 Live Demo

**Try CineMatch:** https://cinematch-2vz87avrlzaavutnbleqjm.streamlit.app

## ✨ Features

- 🎥 Search and select movies from the available dataset.
- 🤖 Recommend five movies similar to the selected movie.
- 🖼️ Display movie posters using the TMDB API.
- ⭐ Show movie ratings and release years.
- 🎭 Display movie genres.
- 🌑 Enjoy a dark cinematic interface with gold accents and hover effects.
- ⚡ Load precomputed recommendation indices for efficient recommendations.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Pandas** — Dataset handling and manipulation
- **NumPy** — Numerical operations
- **Scikit-learn** — Text vectorization and similarity calculations during model building
- **Streamlit** — Interactive web application
- **Requests** — API requests
- **TMDB API** — Movie information and posters
- **NLTK** — Text preprocessing and stemming

## 🧠 How It Works

CineMatch uses a content-based recommendation approach.

1. **Data preprocessing:** Movie information such as keywords, cast, crew, and other available metadata is processed into text tags.
2. **Text vectorization:** CountVectorizer converts the movie tags into numerical feature vectors.
3. **Similarity calculation:** Cosine similarity measures how similar the movie representations are.
4. **Precomputation:** The most similar movie indices are saved in `neighbors.npz`.
5. **Recommendation:** When a user selects a movie, the application retrieves its precomputed neighbors and displays five recommendations.
6. **Movie details:** The TMDB API provides posters, ratings, release years, and genres.

## 📂 Project Structure

```text
CineMatch/
├── app.py
├── tmdb.py
├── model_build.py
├── movies.pkl
├── neighbors.npz
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── config.toml
```

- `app.py` — Main Streamlit application.
- `tmdb.py` — Fetches movie details from the TMDB API.
- `model_build.py` — Builds the recommendation data.
- `movies.pkl` — Saved movie dataset.
- `neighbors.npz` — Precomputed recommendation indices.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Excludes local and sensitive files.

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rehan-shaik-06/CineMatch.git
cd CineMatch
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your TMDB API key

Create a `.env` file in the project root:

```text
TMDB_API_KEY=your_actual_tmdb_api_key
```

Replace the placeholder with your own API key.

**Never commit your `.env` file or expose your API key publicly.**

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal.

## 🔑 API Configuration

CineMatch uses the TMDB API to retrieve movie details and poster images.

Obtain an API key through your TMDB account and configure it using an environment variable or Streamlit Secrets.

For Streamlit Community Cloud, add the following to the app's Secrets settings:

```toml
TMDB_API_KEY = "your_actual_tmdb_api_key"
```

## 🚀 Deployment

CineMatch is deployed using Streamlit Community Cloud.

- Application: https://cinematch-2vz87avrlzaavutnbleqjm.streamlit.app
- Hosting: Streamlit Community Cloud
- Source code: GitHub

## 🔮 Future Improvements

- Genre-based filtering and advanced search.
- Movie details and overview panels.
- User favorites and watchlists.
- Improved mobile responsiveness.
- Additional recommendation strategies.
- Personalized recommendations based on user preferences.

## 🙌 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for movie metadata and poster images.
- [Streamlit](https://streamlit.io/) for the web application framework.
- [Scikit-learn](https://scikit-learn.org/) for machine learning utilities.

This product uses the TMDB API but is not endorsed or certified by TMDB.

## 📄 License

Choose a license before permitting others to reuse or modify this project. If you intend to make it open source, consider adding an appropriate license file.

---

**Built with Python, machine learning, and a love for movies. 🎬**
