#!/bin/sh

echo "GET /films"
curl localhost:8080/films

echo "\nPOST /characters (film_id=0)"
curl -X POST -H "Content-Type: application/json"  -d '{"film_id":0}' \
    localhost:8080/characters
echo "\nPOST /characters (film_id=1)"
curl -X POST -H "Content-Type: application/json"  -d '{"film_id":1}' \
    localhost:8080/characters
echo "\nPOST /characters (film_id=2)"
curl -X POST -H "Content-Type: application/json"  -d '{"film_id":2}' \
    localhost:8080/characters
echo "\nPOST /characters (film_id=3)"
curl -X POST -H "Content-Type: application/json"  -d '{"film_id":3}' \
    localhost:8080/characters
echo "\nPOST /characters (film_id=4)"
curl -X POST -H "Content-Type: application/json"  -d '{"film_id":4}' \
    localhost:8080/characters
echo "\nPOST /characters (film_id=5)"
curl -X POST -H "Content-Type: application/json"  -d '{"film_id":5}' \
    localhost:8080/characters
