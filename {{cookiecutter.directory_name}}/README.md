### {{cookiecutter.project_name}}
> Project Description here <br />
>  
> 1. ...
> 2. ...
> 3. ...

## Overview
Text here

![Model Architecture](public/images/Architecture.png?raw=true "Model Architecture")

## Installing / Getting started

This is a python project, and should run fine on version >= 3. 
1. Install python 3.x
2. Create a virtual environment for python

    ```shell
    pip3 install virtualenv
    mkdir ~/.virtualenvs
    
    pip3 install virtualenvwrapper
    
    # Add following to bash_profile
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
    source ~/.bash_profile
    
    source /usr/local/bin/virtualenvwrapper.sh
    
    workon
    mkvirtualenv {{cookiecutter.project_name}}
    ```
    This setups up a new virtualenv called {{cookiecutter.project_name}}. <br />

3. Install the required libraries for this project

    ```shell
    pip3 install -r requirements.txt
    ```
4. Install MySQL and configure it in `conf/config.yaml`

### Initial Configuration
There are 2 levels of setup required - 
1. Setup config data correctly in conf/config.yaml
2. Add environment variables in a .env file located in root directly. Details are given below


### Environment Variables to be added to .env
```shell
env=DEV
REDIS_URL=redis://127.0.0.1:6379
REDIS_HOST=127.0.0.1
REDIS_USER=""
REDIS_PORT=6379
REDIS_PASSWORD=""
DB_HOST=localhost
DB_PORT=7709
DB_USER=****
DB_PASSWORD=****
```

### *Running Code Directly (Non Docker)*

There are 3 ways to run this directly (locally)
1. Use python to run scheme wise script directly
    
    ```shell
    python3 <<scheme_script_name>>.py
    ```
    App would be accessible on http://127.0.0.1:{{cookiecutter.project_server_port}}<br /><br />

2. Using WSGI Server for running app (without config)

    You can also use following for running the app : 
    ```shell
    gunicorn app.controllers.api_controller:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:{{cookiecutter.project_server_port}}
    ```
    App would be accessible on http://127.0.0.1:{{cookiecutter.project_server_port}}<br /><br />

3. Using WSGI Server for running app (with config)

    Use following for running the app : 
    ```shell
    gunicorn -c conf/gunicorn.conf.py --log-level=debug --worker-class uvicorn.workers.UvicornWorker app.controllers.api_controller:app
    ```
    App would be accessible on http://0.0.0.0:{{cookiecutter.project_server_port}}<br /><br />

## Deploying / Publishing

### Docker
#### Local
For building the project run
```shell
docker build -t {{cookiecutter.docker_image_url}} .
```
#### Remote
This project is configured with gitlab runner to build a docker image and push it to docker registry.
Simply make the necessary change and push it to git.<br />

##### Docker Script for local/ remote 

```shell
#!/bin/bash

docker run -d -it --rm -p 5002:5002 --name {{cookiecutter.project_name}} \
	-e env=PROD \
	-e REDIS_URL=redis://***.***.***.***:6379 \
	-e REDIS_HOST=***.***.***.*** \
	-e REDIS_USER= \
	-e REDIS_PORT=6379 \
	-e REDIS_PASSWORD= \
	-e DB_HOST=***.***.***.*** \
	-e DB_PORT=7709 \
	-e DB_USER=grafana_nexxo \
	-e DB_PASSWORD=**** \
	{{cookiecutter.docker_image_url}}

```
