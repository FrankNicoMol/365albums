import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .markdown import capitalize


def get_album_id(url):
    return re.search(r'/album/([A-Za-z0-9]+)', url).group(1)


def get_album(spotify, url):
    album = spotify.album(get_album_id(url))
    return [capitalize(album['artists'][0]['name']), capitalize(album['name'])]


def get_albums(urls):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    albums_list = [[get_album(spotify, url), url] for url in urls]
    albums_list.sort()
    return albums_list


def fetch_album_details(spotify, url):
    album = spotify.album(get_album_id(url))

    year = album['release_date'][:4]
    duration_ms = sum(t['duration_ms'] for t in album['tracks']['items'])
    duration_min = round(duration_ms / 60000, 1)

    artist = spotify.artist(album['artists'][0]['id'])
    genres = ', '.join(artist['genres']) if artist['genres'] else 'unknown'

    return year, duration_min, genres
