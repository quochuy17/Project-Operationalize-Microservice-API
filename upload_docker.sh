#!/usr/bin/env bash
# Initially, just make the Docker's path
dockerpath="huyluu/proj4-devops"

# Next, just make some related authenticate & tag for Docker's configurations
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag proj4-devops:latest $dockerpath

# Finally, just deliver the related image to the repository of the docker
docker image push $dockerpath