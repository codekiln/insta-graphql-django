# 02 Add GraphQL - 01 Configure Django Settings

In this section we'll add GraphQL to our django project.
The GraphQL adapter for Django is [graphene-django](https://github.com/graphql-python/graphene-django).


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

We'll define our schema using two schema files. 

First, create a new `schema.py` file in the `instagraphql_django/users/` directory. 
This will be contain the schema for the `users` 

Next, create a `schema.py` in the `config/` directory. This will stitch together the 
schemas from all of our Django apps.

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
    'SCHEMA': 'instagraphql_django.schema.schema'
}
```
