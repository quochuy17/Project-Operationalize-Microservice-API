#!/usr/bin/env bash

## Install Docker local environment

# Initially, just create the image, then add the tag
docker build . --tag=proj4-devops 

# Next, just enumerate all associated Docker images
docker image ls

# then, after completing the aforementioned procedures, launch the flask app for analysis
# config with port 80
docker run -it --rm --name proj4-devops -p 8080:80 proj4-devops
