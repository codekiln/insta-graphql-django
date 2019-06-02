# 03 User Setup

In this section we'll create a superuser that has access 
to the Django Admin

1. Start the docker containers if they are not already started:
  1. `docker-compose -f local.yml up`
  2. Note, this calls [`runserver_plus`](https://django-extensions.readthedocs.io/en/latest/runserver_plus.html)
     when using local settings

2. `docker-compose -f local.yml run django python manage.py createsuperuser`
  1. This uses [`docker-compose run`](https://docs.docker.com/compose/reference/run/)
     to call [`manage.py createsuperuser`](https://docs.djangoproject.com/en/2.2/intro/tutorial02/#creating-an-admin-user)
     on the `django` service in `local.yml`.
  2. Fill in the prompts at the console after calling to create a superuser for the site. 
3. Login as the superuser in the Django Admin
  1. Go to `http://localhost:8000/admin/`
  2. enter the superuser credentials you entered in step 2.2
  3. if you haven't used the [Django Admin, take a look around](https://docs.djangoproject.com/en/2.2/intro/tutorial02/#explore-the-free-admin-functionality)
