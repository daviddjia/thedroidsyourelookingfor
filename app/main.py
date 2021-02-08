import star_wars_api

from flask_api import FlaskAPI
from flask import jsonify, request, abort

app = FlaskAPI(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "These aren't the droids you're looking for"

@app.route('/films', methods=['GET'])
def films():
    return jsonify(star_wars_api.get_films())

@app.route('/characters', methods=['POST'])
def characters():
    if not request.json or 'film_id' not in request.json:
        abort(400)
    return jsonify(star_wars_api.get_characters_by_film(
        request.json['film_id']))
