#!/bin/bash

git pull
docker compose down
docker compose up -d --force-recreate --no-deps --build --remove-orphans
sleep 10
curl http://localhost:9291/metrics
