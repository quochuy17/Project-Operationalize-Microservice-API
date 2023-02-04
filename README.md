# Project : Operationalize a Machine Learning Microservice API
In this project, the mission is about to apply pre-trained, sklearn model that has been taught to forecast housing costs in Boston based on a number of characteristics, including information on the typical number of rooms in a home, statistics on highway accessibility, teacher-to-student ratios, and more.

# Project's using tools and libraries
    + Python, Jupiter notebook
    + Visual Studio Code and Colab
    + Docker, Hadolint and Kubernetes (Minikube)\

## Project's materials
    + Initially, utilizing the dataset taken from Kaggle, on the data source site (https://www.kaggle.com/c/boston-housing).
    + Beside that, this project tests your ability to operationalize a Python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

# Project's target
+ Firstly, implementing a Kubernetes-based elastic and fault-tolerant Machine Learning inference API.
+ Secondly, make this microservice highly available by configuring it according to Kubernetes best practices. 
+ Next, test the service under load to validate the design and ensure the application architecture operates as intended.

### Project's Files included:
In this project, there are some essential files in order to implement including:
    + .circleci 
    + model_data with data source files
    + output_txt_file including "docker_out.txt" and "kubernetes_out.txt"
    + app.py, Makefile
    + Dockerfile with related files for working with docker and other features
    + "make_prediction.sh", "run_docker.sh", "run_kubernetes.sh", "upload_docker.sh" 

### Project's implementing steps
There are some sequential tasks needed to implement including:
    + Initially, complete a Dockerfile to containerize the application 
    + Second, deploy the containerized application using Docker and make a prediction 
    + Third, enhance the logging in the source code for this application 
    + Fourth, configure Kubernetes and set up a Kubernetes cluster
    + Fifth, deploy a container using Kubernetes and make a prediction 
    + Finally, upload the entire Github repository with CircleCI to show that the code has been tested

## The steps for establishing the Environment
** Firstly, just create a virtualenv and activate the created feature by using the siutable command.

** Next, after above step, just type the command `make install` to install the essential dependencies including:
    # STEP 1 : Running the "app.py"
        + Standalone:  "python app.py"
        + Run with Docker:  "run_docker.sh"
        + Run with Kubernetes:  "run_kubernetes.sh"

    # STEP 2: next, the Docker's implementing steps including:
        + Then, when need to publish the docker image: `./upload_docker.sh`

    # STEP 3: then, with the Kubernetes's implementing steps including:
        + Firstly, setup Docker on the local environment
        + Secondly, Setup Kubernetes on the local environment
        + Third, create Flask app in Container
        + Then, just run via the kubectl
        
** Finally, while you still have your .devops environment activated, you will still need to install:
        + Docker
        + Hadolint
        + Kubernetes


 
