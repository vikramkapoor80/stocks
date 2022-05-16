# Cloud SRE/DevOps Challenge

Cloud SRE/DevOps Challenge

Cloud SRE/DevOps Challenge  creates a stock ticker app built with flask conterize the app and setup kubernetes manifest.

# setup
flask - docker - kubernetes
- Installing python
- create virtual enviroment
- Install dependancies
- create flask app
- build Docker image using Dockerfile
- write docker compose
- writing kubernetes Manifest files


## Features
- Flask Based App - Stock Ticker
- Docker Container for the Flask App
- Kubernetes Manifest


## Primary Goals
 - To Write a web service that looks up a fixed number of closing prices of a specific stock. 
 - To use Docker to containerize the app
 - To create kubernetes manifest for deployment of docker images in a kubernetes cluster.



## Table of Contents

1. [Getting Started With Flask App](#getting-started)
1. [Screenshots](#screenshots)
1. [Dependancies](#Dependancies)
1. [Project Structure](#ProjectStructure)
1. [Docker Image](#docker)
1. [Kubernetes Manifest](#kubernetes-manifest)




## Getting Started With Flask App

clone the project

```bash
$ git clone flask-docker-kubernetes.git
$ cd flask-docker-kubernetes
```

create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ python3 -m venv /path/to/your/virtual/environment
$ source <path/to/venv>/bin/activate
```

install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

setup `flask` command for our app

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

5) start test server at `localhost:5000`

```bash
$ flask run
```


## Screenshots

![Home](/screenshots/data.png)


## Dependancies

- asgiref==3.5.1
- certifi==2021.10.8
- charset-normalizer==2.0.12
- click==8.1.3
- colorama==0.4.4
- Flask==2.0.2
- idna==3.3
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- requests==2.27.1
- urllib3==1.26.9
- Werkzeug==2.1.2
- python-dotenv==0.20.0



## Project Structure

flask-docker-kubernetes
├── static
│   ├── bootstrap.bundle.min.js
│   ├── bootstrap.min.css
│   └── jquery.slim.min.js
├── templates
│   │   ├── base.html
│   │   ├── msg.html
│   │   ├── header.html
│   │   ├── index.html
├── app.py
├── .env
├── .env.prod
├── Dockerfile
├── .dockerignore
├── kubernetes-manifest.yaml
├── README.md
├── .gitignore
├── requirements.txt
├── screenshots
│   ├── data.png



## Build Docker

Build Docker Image Locally

```bash
$ docker build --tag stock-ticker .
```

Docker Run 

```bash
$ docker run -d --env-file ./env.prod --name stock-ticker-app -p 80:80 stock-ticker
```


## Publish Docker Image

Creating a repository on Docker Hub

The username is your Docker hub name, and the repository_name in this case is stock-ticker; the repository we created earlier.

```bash
$ docker build -t username/stock-ticker .

```

Pushing Docker image

Login
```bash
$ docker login

```

Login
```bash
$ docker push username/stock-ticker

```

## Kubernetes Manifest

Kubernete Deployment

```bash
$ kubectl apply -f stockticker-kubernetes-manifest.yaml
```

Get Deployments
```bash
$ kubectl get deployments
```


Get services
```bash
$ kubectl get services
```