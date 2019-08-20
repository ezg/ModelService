# ModelService
This repository contains the Models as a Service (MaaS) API for World Modelers.
## Contents

- [Design](#design)
	- [Project Goals](#project-goals)
	- [Architecture](#architecture)
- [Development](#development)
	- [Installation](#installation)
	- [Swagger Editor](#swagger-editor)
	- [Open API Code Generation](#open-api-code-generation)
	- [Running the REST Server](#running-the-rest-server)
- [Usage](#usage)
    - [Exploration](#exploration)
    - [Concepts](#concepts)
    - [Execution](#execution)

## Design

### Project Goals
The goal of this project is to provide a easy to use, descriptive middleware layer API to facilitate model search and discovery, exploration, configuration, and execution. 

#### Model discovery
Model search, discovery, and exploration is managed through the [`Exploration Controller`](https://github.com/WorldModelers/ModelService/blob/master/REST-Server/openapi_server/controllers/exploration_controller.py). The `Exploration Controller` provides a high-level interface into [MINT](http://mint-project.info/) which serves as a lower-level model and data metadata catalog. In the future, users will be able to search across models and datasets by:

* **Keyword**: fuzzy or exact match against words contained in model descriptions, dataset variable names, parameter names, or [standard names](https://csdms.colorado.edu/wiki/CSDMS_Standard_Names) contained in MINT
* **Temporal Coverage**: users may search for models or datasets based on the time ranges that they cover
* **Geospatial Coverage**: users may search for models or datasets that match to a specific geography of interest

#### Model execution
Model execution is managed by the [`Execution Controller`](https://github.com/WorldModelers/ModelService/blob/master/REST-Server/openapi_server/controllers/execution_controller.py). Models consist of pre-built Docker images that are hosted on an arbitrary server. Running a model requires the creation of a specific model controller, such as this one for [Kimetrica's malnutrition model](https://github.com/WorldModelers/ModelService/blob/master/REST-Server/openapi_server/kimetrica.py). The model controller is responsible for obtaining a model configuration and tasking Docker to run the model image inside a container with the given configuration. The model controller specifies a Docker container entrypoint, such as [this one](https://github.com/WorldModelers/ModelService/blob/master/Kimetrica-Integration/run.py) which is responsible for writing the model output (from within the container) to S3.

### Architecture

![MaaS Architecture](images/MaaS-Architecture.png "MaaS Architecture")


## Development

### Installation

Install Redis and start via https://redis.io/topics/quickstart.

```
# SET $HOME/.aws/credentials to proper key and secret.

# Install MAAS
git clone https://github.com/WorldModelers/ModelService.git
cd ModelService/REST-Server
conda create -n maas_env python=3.7 pip jupyter -y
source activate maas_env
pip install -r requirements.txt

# Install FSC Model.  You will get prompted for github credentials.
# This will take quite a bit of time.
cd ../FSC-Integration/
./maas_install.sh

# Install Kimetrica Model.
cd ../../Kimetrica-Integration/

# Please look at this file as you must set the CKAN creds manually right now...
./maas_install.sh


# HOW TO RUN
cd ../../REST-Server
python -m openapi_server
```

### Swagger Editor
To use this, run the following:

```
docker pull swaggerapi/swagger-editor:latest
docker run -d -p 80:8080 swaggerapi/swagger-editor
```

This will run Swagger Editor (in detached mode) on port 80 on your machine, so you can open it by navigating to http://localhost in your browser.

### Open API Code Generation

Unfortunately, the current Swagger Editor does not support code gen for Open API 3.0 and Flask. To generate the server stub use:

```
wget http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/3.3.4/openapi-generator-cli-3.3.4.jar -O openapi-generator-cli.jar

java -jar openapi-generator-cli.jar generate \
  -i model_service_api.yaml \
  -l python-flask \
  -o Rest-Server-UPDATE
```

### Running the REST Server
First navigate to the `REST-Server` directory with `cd REST-Server`. Next, install the requirements with something like:

```
pip3 install -r requirements.txt
```

Now you can run the server with `python3 -m openapi_server`. You can access the UI at [http://0.0.0.0:8080/ui](http://0.0.0.0:8080/ui).

### Results Storage
You must ensure that the results stored by the model are readable and writable by the process running the server. This location is defined in `config.ini`. For example, for FSC in production this could look like:

```
[FSC]
OUTPUT_PATH = /home/ubuntu/ModelService/results/fsc/outputs
```

However you must ensure that this location is readable and writable by the process running the server. Results will be written by the model's Docker container (which may be `root`) so you likely need to `sudo chmod -r +777 /home/ubuntu/ModelService/results` or something like that to ensure appropriate permissions are set.

## Usage

## Exploration

Example queries for the `/search` endpoint can be somewhat complex so below are some example queries that could be run:

### `/search`

**GEO**

```
{
   "query_type":"geo",
   "result_type":"datasets",
   "xmin": 33.9605286,
   "xmax": 33.9895077,
   "ymin": -118.4253354,
   "ymax": -118.4093589
}
```

**TEXT**

```
{
   "query_type":"text",
   "result_type":"datasets",
   "term": "Country Name",
   "type": "standard name"
}
```

```
{
   "query_type":"text",
   "result_type":"models",
   "term": "food",
   "type": "keyword"
}
```

**TIME**

```
{
   "query_type":"time",
   "result_type":"models",
   "start_time": "1960-01-01T00:00:00",
   "end_time": "2019-01-01T23:59:59"
}
```

## Concepts

TODO

## Execution

TODO
