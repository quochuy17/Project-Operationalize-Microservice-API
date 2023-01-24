#!/usr/bin/env bash

# Firstly, define the ID/path of Docker
dockerpath="huyluu/proj4-devops"

# Next, just utilize Kubernetes to execute the Docker Hub container
kubectl run proj4-devops --image=$dockerpath --port=80

# Thirdly, just list out some related kubernetes pods
kubectl get pods

# Finally, just deliver the host with the container port
kubectl port-forward proj4-devops 8080:80


