#!/bin/bash
set -e
set -x

# build and push postgres-dev image
docker build -t advent-of-ds:postsgres-1.0-dev -f ./db/postgres/Dockerfile.dev ./db/postgres
docker tag advent-of-ds:postsgres-1.0-dev johntrunix/advent-of-ds:postsgres-1.0-dev
docker push johntrunix/advent-of-ds:postsgres-1.0-dev

# build and push backend-dev image
# ...

# build and push frontend-dev image
# ...

docker images --filter=reference=*advent-of-ds*