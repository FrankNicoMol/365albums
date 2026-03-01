# 365 Albums — 2026

A personal project to track a New Year's resolution: listen to 365 albums in 2026.

Paste Spotify album links into a markdown file, run the script, and it will:
- Fetch album metadata from the Spotify API
- Maintain sorted *to listen* and *listened* lists in markdown
- Export a CSV with artist, album, year, duration, and genres
- Generate a single-page HTML overview

---

## Setup

### 1. Clone the repo

```bash
git clone <repo-url>
cd spotify_scraper
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up Spotify credentials

Create a Spotify app at [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) to get a client ID and secret. Then:

```bash
cp spotify_albums/spotify_credentials.sh.example spotify_albums/spotify_credentials.sh
# fill in your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
```

### 4. Configure your markdown paths

```bash
cp config/paths.yaml.example config/paths.yaml
# fill in the paths to your markdown files
```

`paths.yaml` expects three markdown files:

| Key | Purpose |
|---|---|
| `links` | Paste raw Spotify album URLs here |
| `not_listened` | Auto-maintained queue of albums to listen to |
| `listened` | Albums you have already listened to |

### 5. Add an image

Place a `.png` in the `img/` folder. The most recently named file (sorted alphabetically) is used as the hero image on the generated webpage.

---

## Usage

```bash
python main.py
```

This will:
1. Load Spotify credentials automatically
2. Convert all links in `links.md` to album entries in `not_listened.md`, then clear `links.md`
3. Sort both `not_listened.md` and `listened.md` alphabetically
4. Export a dated CSV to `csv/albums_YYYYMMDD.csv`
5. Generate `index.html` with a stats overview

---

## Project structure

```
spotify_scraper/
├── main.py                        # entry point
├── requirements.txt
├── config/
│   ├── paths.yaml                 # your paths (git-ignored)
│   └── paths.yaml.example         # template
├── spotify_albums/                # package
│   ├── config.py                  # YAML config loader
│   ├── dataframe.py               # build pandas DataFrame from Spotify API
│   ├── env.py                     # load shell credentials into os.environ
│   ├── markdown.py                # read/write markdown album lists
│   ├── page.py                    # generate index.html
│   ├── spotify_api.py             # Spotify API calls
│   ├── spotify_credentials.sh     # your credentials (git-ignored)
│   └── spotify_credentials.sh.example
├── csv/                           # generated CSVs (git-ignored)
└── img/                           # hero image for the webpage
```
