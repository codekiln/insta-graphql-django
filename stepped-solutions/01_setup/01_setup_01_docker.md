# 01 Docker Setup

## Build Image and Bring Environment Up
1. `cd instagraphql_django`
2. Download Requirements
  1. Docker; if you don’t have it, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms)
  2. Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/)
3. Build the Docker container - `docker-compose -f local.yml build`
  1. For more commands, see [Getting Up and running Locally With Docker](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
4. Instantiate the container to bring up the environment
  1. run `export COMPOSE_FILE=local.yml`. If you don't run this, you'll need to append `-f local.yml` to every `docker-compose` command.
  2. `docker-compose up`
5. Connect to postgres with `psql` to validate it works (optional)
  1. use the `POSTGRES_USER` and `POSTGRES_DB` from `instagraphql_django/.envs/.local/.postgres`
     * tip: if using a bash-based terminal you can use 
       `set -a; . instagraphql_django/.envs/.local/.postgres; set +a;` to source the variables 
       in that file into the shell
  2. `docker-compose exec postgres psql -d $POSTGRES_DB -U $POSTGRES_USER`
  3. inside the postgres shell, take a look around with postgres commands such as `/list`

## run `export COMPOSE_FILE=local.yml` before using `docker-compose` in this project
Note: the docker commands here assume that you have run `export COMPOSE_FILE=local.yml` 
in your terminal and that you are in the `instagraphql_django` folder. If you haven't 
run this command, you'll need to append `-f local.yml` to every `docker-compose` invocation.