Movies API
==========

This is the movies api for [https://javierdaza.co/koombea-movies/](https://javierdaza.co/koombea-movies/)
I used [django-cookiecutter](https://github.com/pydanny/cookiecutter-django) to speed up the development process of this API.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Celery tasks
^^^^^^^^^^^^

Follow this steps to configure the periodic tasks from the admin

1. In the celery crontabs section, create one that looks like
**0 2 * * * (m/h/d/dM/MY) America/Bogota**

2. Inside Periodic tasks, create one task that:

- Have a Name your task
- Task that points to **movies_api.movies.tasks.create_movies_database_task**
- Select the previusly created crontab schedule for 2:00AM
- Choose a start datetime (Day and Hour)



Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


TODOs
--------------

1. Create 2 directories for *apps* and *api*
2. Define what to do with the updates of each movie in create_movies_database_task
3. Paginate endpoint for listing movies
4. Add abstract Model for common fields like *created*, *modified* and *active*
5. Add version of the API to URLs (http://localhost:8000/v1/movies/vote/4/)
