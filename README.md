# PandaPower Simulation API

This project is an REST API Service that allows to retrieve information of a simulation using PandaPower library.

## Getting Started

### Deployment

This application was implemented using the following technologies:

* [Python](https://www.python.org/) - Programming Language
* [Django](https://www.djangoproject.com/) - Web Framework
* [Django Rest Framework](https://www.django-rest-framework.org/) - Web API
* [PandaPower](https://www.pandapower.org/) - Power flow calculation
* [Docker](https://www.docker.com/) - Docker Containers.


## Requirements

* Python 3.x.x
* Django 2.x.x
* DRF 
* PandaPower

<br/>

## Running the application 


### Docker Instructions

*(Ensure Docker is installed on your system.)*

#### 1-) Running the containers:

First, clone the repository on your local machine and execute the following commands:

```
$ docker-compose up
```

At this point, the Django app should be running at port 8000 on your Docker host.


#### 2-) List running containers:

In another terminal window, list the running Docker processes with the docker container ls command.

```
$ docker ps
```


#### 3-) Login into the Docker Container.

List containers via:

```
$ docker container ls
```

Run this command in the running container using its *container-id*, to get a bash shell in the container. 
Generically, use docker exec -it <container name> <command> to execute whatever command you specify in the container.

```
$ docker exec -it <container-id> /bin/bash
```


#### 4-) Shut down services and clean up:

- Stop the application by typing Ctrl-C in the same shell in where you started it.

- Or, for a more elegant shutdown, switch to a different shell, and run docker-compose down from the top level of the Django project directory.

```
$ docker-compose down
```
<br/>

## API

You can use the API in this way in order to retrieve the following information:

### Power flow Simulation

Endpoint that launches the simulation using the PandaPower Python module. The response include the active and reactive power of the load in JSON format.


```
POST http://0.0.0.0:8000/pandapower_api/simulation/create/
```

##### Response:
```
{
    "active_power": 0.1,
    "reactive_power": 0.05,
    "status": "success"
}
```

### Active-Power

Endpoint to retrieve the active power of the previously executed simulation.

```
GET http://0.0.0.0:8000/pandapower_api/simulation/active/
```

##### example:

```
{
    "active_power": 0.1,
    "status": "success"
}
```

### Reactive-Power

Endpoint to  retrieve the reactive power of the previously executed simulation.

```
GET http://0.0.0.0:8000/pandapower_api/simulation/reactive/
```

##### example:

```
{
    "reactive_power": 0.05,
    "status": "success"
}
```

### Error cases

##### Example 1: No previous active power

In case the session does not have any previously simulation calculated and therefore no "active power" value. The following response will be given when requesting 
the "Active-Power" endpoint :

```
{
  'message': "No previous simulation has been calculated",
  'status': "error"
}
```

##### Example 2: No previous reactive power

In case the session does not have any previously simulation calculated and therefore no "reactive power" value. The following response will be given when requesting 
the "Active-Power" endpoint :

```
{
  'message': "No previous simulation has been calculated",
  'status': "error"
}
```

### Author:

* **Ernesto Zarza**
