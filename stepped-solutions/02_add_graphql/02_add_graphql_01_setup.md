# 02 Add GraphQL - 01 Setup

In this section we'll add GraphQL to our django project.
The GraphQL adapter for Django is [graphene-django](https://github.com/graphql-python/graphene-django).


Note: the docker commands here assume that you have run `export COMPOSE_FILE=local.yml` 
in your terminal and that you are in the `instagraphql_django` folder. If you haven't 
run this command, you'll need to append `-f local.yml` to every `docker-compose` invocation below.

## 1. Installing Graphene-Django
Open `instagraphql_django/requirements/base.txt`, which is where the project's python requirements are stored.

At the end, remove this section, since we won't be using Django REST: 
```
# Django REST Framework
djangorestframework==3.9.4  # https://github.com/encode/django-rest-framework
coreapi==2.3.3  # https://github.com/core-api/python-client
```

Add this section to the end instead, adding `graphene-django`. It's a good idea to check
the [latest version of `graphene-django` on pypi](https://pypi.org/project/graphene-django/) 
before doing this, and updating the below if desired.

```
# GraphQL APIs
graphene-django==2.2.0
```

## 2. Configure Django Settings to Load `graphene-django` on startup
The base django settings are at `instagraphql_django/config/settings/base.py`. 

Look for the `THIRD_PARTY_APPS` array. Remove the entry for `rest_framework` and 
add `graphene_django` instead.

## 3. Configure `django-graphene` in Django settings
Now Django will load the `graphene_django` app when Django starts, but we still need 
to tell the `graphene-django` app where in the code our schema is defined. 

The [configuration options supported `graphene_django` are documented in their README](https://github.com/graphql-python/graphene-django#settings).

At the bottom of the `base.py` settings file, you'll see a section that looks like this: 
```
# Your stuff...
# ------------------------------------------------------------------------------
```

Change it to: 

```python
# django-graphene
# ------------------------------------------------------------------------------
GRAPHENE = {
    'SCHEMA': 'config.schema.schema'
}
```

## 4. Create the schema file

## 5. Recreate the docker container

If you have docker up and running, you'll need to stop it: `docker-compose down`

Now, rebuild the new docker image with the new requirements: `docker-compose up --build`.

