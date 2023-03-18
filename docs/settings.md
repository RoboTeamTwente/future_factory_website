# Settings
This Django project does contain some settings (`future_factory_website/settings.py`) that are specific to the way it 
has been deployed. This page will explain these settings.

| Setting                | Description                                                                                                                                                                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SECRET_KEY`           | The secret key is taken from the environment variable `DJANGO_KEY`                                                                                                                                                                                     |
| `DEBUG`                | Based on whether the DEBUG environment variable is set to `true`, we run in a debug mode. Otherwise we run in production mode                                                                                                                          |
| `BETA`                 | Based on whether the BETA environment variable is set to `true`, the application runs in beta mode.                                                                                                                                                    |
| `ALLOWED_HOSTS`        | The deployment server runs behind NGINX, which already does host checks. Hence we skip this on the Django side                                                                                                                                         |
| `CSRF_TRUSTED_ORIGINS` | Only these hosts may receive POST requests                                                                                                                                                                                                             |
| `DATABASES`            | The databases are dynamically chosen based on the `DEBUG` variable. The production database assumes that there are environment variables available for the database name, user and password. The server is expected to be found on `future_factory_db` |
| `QUILL_CONFIGS`        | The rich text editor configuration. For more information see its [documentation](https://django-quill-editor.readthedocs.io/en/latest/pages/change-toolbar-configs.html)                                                                               |
| `STATIC_ROOT`          | The location on the deployment server where the static files are stored (part of the code base like .js, .css files)                                                                                                                                   |               
| `MEDIA_ROOT`           | The location on the server where the media files are stored (uploaded by a user)                                                                                                                                                                       |
| `EMAIL_*`              | Email related settings, more details can be found in the [Django documentation](https://docs.djangoproject.com/en/4.1/topics/email/#send-mail)                                                                                                                                                                      |

# Environment variables
For safety reasons all secrets are loaded with the help of environment variables. The following are in use:

| Value               | Description                                              |
|---------------------|----------------------------------------------------------|
| `DJANGO_KEY`        | Used for the `SECRET_KEY` setting                        |
| `DEBUG`             | Used to determine whether we are running in debug mode   |
| `BETA`              | Used to determine whether we are running in beta mode    |
| `POSTGRES_NAME`     | The name of the database used in production mode         |
| `POSTGRES_USER`     | The username to authenticate at the production database  |
| `POSTGRES_PASSWORD` | The password for the production database                 |
| `EMAIL_PASSWORD`    | The password to the email account used for sending email |