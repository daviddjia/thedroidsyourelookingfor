from cache import cache

import requests
import json

FILMS_URL = 'http://swapi.dev/api/films/'

def get_films():
    film_data_with_characters = get_films_with_characters()
    return [
        {k: v for k, v in film.items() if k != 'characters'}
        for film in film_data_with_characters]

@cache.list(3600)
def get_films_with_characters():
    all_film_data = requests.get(url=FILMS_URL).json()['results']
    return [{
        'id': id,
        'title': data['title'],
        'release_date': data['release_date'],
        'characters': data['characters'],
    } for id, data in enumerate(all_film_data)]

def get_characters_by_film(film_id):
    film_data_with_characters = get_films_with_characters()
    for film in film_data_with_characters:
        if film['id'] == film_id:
            return [{
                'id': id,
                'name': get_character_name(character_url),
            } for id, character_url in enumerate(film['characters'])]

@cache.dict(3600)
def get_character_name(character_url):
    print(character_url)
    return requests.get(url=character_url).json()['name']
