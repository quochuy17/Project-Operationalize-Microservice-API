#!/usr/bin/env bash

# In general, there are total of three main steps so as to install Docker on the local environment including:

# Initially, just create the image, then add the suitable tag
docker build --tag=proj4-devops .

# Next, just enumerate all associated Docker images for evaluating 
docker image ls

# Finally, after completing the aforementioned procedures, launch the Flask App for other analysis( just config with port 80)
docker run -it --rm --name proj4-devops -p 8080:80 proj4-devops
