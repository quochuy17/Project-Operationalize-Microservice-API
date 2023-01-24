# Project : Operationalize a Machine Learning Microservice API
In this project, the mission is about to apply pre-trained, sklearn model that has been taught to forecast housing costs in Boston based on a number of characteristics, including information on the typical number of rooms in a home, statistics on highway accessibility, teacher-to-student ratios, and more.

# Project's using tools and libraries
    + Python, Jupiter notebook
    + Visual Studio Code and Colab
    + Docker, Hadolint and Kubernetes (Minikube)

# Project's target
+ Firstly, implementing a Kubernetes-based elastic and fault-tolerant Machine Learning inference API.
+ Secondly, make this microservice highly available by configuring it according to Kubernetes best practices. 
+ Next, test the service under load to validate the design and ensure the application architecture operates as intended.

## Project's data source
    + Initially, utilizing the dataset taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing).
    + Beside that, this project tests your ability to operationalize a Python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

### Project's Tasks
    - In general, the main objective of the project is to operationalize functioning machine learning microservices using Kubernetes, an open-source technology for automating the management of containerized applications (https://kubernetes.io/).
    - The detailed tasks including:
        + Task 1: Complete the Dockerfile
        + Task 2: Run a Container & Make a Prediction
        + Task 3: Improve Logging & Save Output
        + Task 4: Upload the Docker Image
        + Task 5: Configure Kubernetes to Run Locally
        + Task 6: Deploy with Kubernetes and Save Output Logs
        + Task 7: Delete Cluster
        + Task 8: CircleCI Integration
        + Task 9: README.md

### Project's implementing steps
There are some sequential tasks needed to implement including:
    + Initially, complete a Dockerfile to containerize the application 
    + Second, deploy the containerized application using Docker and make a prediction 
    + Third, enhance the logging in the source code for this application 
    + Fourth, configure Kubernetes and set up a Kubernetes cluster (minikube) 
    + Fifth, deploy a container using Kubernetes and make a prediction 
    + Finally, upload the entire Github repository with CircleCI to show that the code has been tested

## The steps for establishing the Environment
- Create a virtualenv and activate it
    ```sh
    python3 -m venv ~/.devops
    source ~/.devops/bin/activate
    ```
- Run `make install` to install the necessary dependencies

    ### Running `app.py`

    1. Standalone:  `python app.py`
    2. Run in Docker:  `./run_docker.sh`
    3. Run in Kubernetes:  `./run_kubernetes.sh`
    4. Make predictions: `./make_prediction.sh`

    ### Docker

    1. Publish docker image: `./upload_docker.sh`

    ### Kubernetes Steps

    * Setup and Configure Docker locally
    * Setup and Configure Kubernetes locally
    * Create Flask app in Container
    * Run via kubectl

### Project's Files included:
There are some needed files to implement including:
    + `.circleci` - circleci config scripts
    + `model_data` - ML model related data (model, csv data)
    + `output_txt_files` - project output files (docker, kubernetes)
        * `docker_out.txt` - run_docker.sh output
        * `docker_prediction_out.txt` - make_prediction.sh output while running docker
        * `kubernetes_container_logs.txt` - kubectl logs output for the pod
        * `kubernetes_out.txt` - run_kubernetes.sh output
        * `kubernetes_prediction_out.txt` - make_prediction.sh output while running k8s pod
    + `app.py` - python web application entry point file
    + `Dickerfile` - docker image config
    + `make_prediction.sh` - make prediction HTTP call script
    + `Makefile` - make file (install, test, lint steps)
    + `requirements.txt` - web application dependencies (python, libraries)
    + `run_docker.sh` - run docker container script
    + `run_kubernetes.sh` - run kubernetes pod for the web app script
    + `upload_docker.sh` - upload docker image to dicker hub script
