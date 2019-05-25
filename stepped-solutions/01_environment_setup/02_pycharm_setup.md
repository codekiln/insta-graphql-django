# 02 PyCharm Setup

It's okay to use another editor, but PyCharm is a highly recommended 
python IDE. The steps below are optional, but will provide the best 
development experience.

PyCharm has a free Community Edition and a paid Professional Edition. 
The ability to connect PyCharm to a python interpreter inside a docker container 
requires the paid version. This is not required, but is the right way to do it 
if you happen to have it.

If you have PyCharm Community edition, you'll want to create a virtualenv
outside of docker and connect PyCharm to it that way. 


## Add Remote Interpreter 
1. In the Settings/Preferences dialog (⌘,), 
   select Project <project name> | Project Interpreter. 
   Click the The Configure project interpreter icon and select Add.

<details><summary>### Add Remote Interpreter - PyCharm Professional (Optional)</summary>
<p>
Follow the steps from [Pycharm Docs - Configuring Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote)

1. If you don't have the default `Docker` showing up under `server`, you'll need to follow 
   [Pycharm Docs - Configuring Docker](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#configuring-docker),
   but by default this should be installed if you have the Professional
   edition of Pycharm.
2. For `Configuration File(s)`, open the browser and select `local.yml`, 
   our docker-compose file for local development
3. For `Service`, select `django`, which is the service defined in `local.yml`
   that contains python
4. For `Python Interpreter Path`, accept the default `python`. You can see 
   that python is accessed is accessed this way in `compose/local/django/start`.

</p>
</details>


## Set Up Django Project Configuration In PyCharm
1. In In the Settings/Preferences dialog (⌘,), search for Django. 
2. Browse to Languages and Frameworks > Django
3. Check Enable Django Support
4. `Django Project Root` - select the `instagraphql_django` folder
5. `Settings` - select the `config/settings/local.py` file


<details><summary>### Add Run Configuration in PyCharm (Optional)</summary>
<p>
This will enable us to run the site with Django's Runserver inside PyCharm, which 
also enables running the PyCharm integrated debugger. If you already know 
PyCharm's debugger, these steps can be helpful, but if not, you do not need to.
The entrypoint at `instagraphql_django/compose/local/django/start` already runs
[`runserver_plus`](https://django-extensions.readthedocs.io/en/latest/runserver_plus.html),
which has a Werkzeug-based debugger.

These instructions are adapted from [Pycharm Docs - Running your application under Docker-Compose #](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#run),
but they apply to both the PyCharm Professional and Community editions.

1. On the main menu choose Run | Edit Configurations...; 
2. in the dialog that opens, click the + sign (Add Run/Debug configuration for a Django Server) 
   and select _Django Server_
3. Name: Django Runserver
4. Host should be set to `0.0.0.0` and port should be `8001`
5. The Python Interpreter should be set to whatever python interpreter 
   you configured above, depending on whether you have PyCharm Professional 
   or Community Edition
6. click OK
7. Launch the new run configuration by selecting Run | Run 'Django Runserver'
8. To see the app in your web browser, go to http://localhost:8001
</p>
</details>

## Add Database Configuration in PyCharm
This method of adding a Data Source to PyCharm works in both editions.

1. In the Database tool window (View | Tool Windows | Database), 
   click the + icon and select DataSource > PostgreSQL
2. Download the PostgreSQL drivers if necessary.
3. Enter values from `instagraphql_django/.envs/.local/.postgres`:
  1. `host`: `127.0.0.1` (note, this is different than in that file)
  2. `port`: `5432`
  3. `user`: `LyhOMblpizhqwpozTgKXjTUuByaQZPyH`
  4. `password`: `gdicmFhVu6bM3bUVj6M8abCsTH9sxkYLrjKeCmfHYBF22jql5QzK3ZYfJZQQZICX`
4. Test Connection - it should work
5. Press OK
6. Double click to see the schemas and tables