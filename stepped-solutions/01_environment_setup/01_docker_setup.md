# 01 Docker Setup

## Build Image and Bring Environment Up
1. `cd instagraphql_django`
2. Download Requirements
  1. Docker; if you don’t have it, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms)
  2. Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/)
3. Build the Docker container - `docker-compose -f local.yml build`
  1. For more commands, see [Getting Up and running Locally With Docker](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
4. Instantiate the container to bring up the environment
  1. `docker-compose -f local.yml up`
5. Connect to postgres with `psql`
  1. use the `POSTGRES_USER` and `POSTGRES_DB` from `instagraphql_django/.envs/.local/.postgres`
  2. `docker-compose -f local.yml exec postgres psql -d $POSTGRES_DB -U $POSTGRES_USER`
  3. inside the postgres shell, take a look around with postgres commands such as `/list`

