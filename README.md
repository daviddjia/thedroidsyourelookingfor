# Star Wars Film/Character API

Build docker container (to host API at `localhost:8080`)
```
cd thedroidsyourlookingfor
docker-compose up --build
```

End-to-end testing using shell script:
```
./test_endpoints.sh
```

Unit testing via pytest:
```
docker exec -it thedroidsyourelookingfor_flask_app_1 pytest
```
