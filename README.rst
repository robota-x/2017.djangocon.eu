#####################
DjangoCon Europe 2017
#####################

This is the project for the http://2017.djangocon.eu/ website.

Run locally
-----------

* Make sure that you have Python 3.5 installed on your system.
* Set up your project::

    git clone https://github.com/djangocon/2017.djangocon.eu.git  # Clone the project
    cd 2017.djangocon.eu

* Create and edit the ``djangocon_europe/.env`` file to contain your secret data (used by `django-environ` so refer to that package documentation for further details)::

    DATABASE_URL=psql://user@password:host:port/db_name
    DEBUG=True
    ALLOWED_HOSTS=["*"]
    SECRET_KEY=my-secret-key
    EMAIL_HOST=localhost
    EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend



Note: the used version has a bug where null parameters are converted to None instead of empty string. You can get around that locally by fixing the package. See https://github.com/joke2k/django-environ/pull/57/files


* Set up your virtualenv ::

    virtualenv --python=/usr/bin/python3.5 env                    # Start a virtualenv
    . env/bin/activate                                            # Use the virtualenv
    pip install --upgrade pip                                     # Use a current pip version
    pip install pip-tools
    pip-sync                                                      # Install dependencies

Note: if you're using Ubuntu pip-sync will fail due to pgk-resources being uninstalled. Either use :code:`pip install -r requirements.txt` (and lose the sync function) or uncomment the #setuptools line in requirements.txt. See https://github.com/nvie/pip-tools/issues/389 and related


* Set up the Django project::

    python manage.py migrate
    python manage.py runserver


How this site works
-------------------

DjangoCon Europe 2017 website heavily relies on django CMS for most of its features.

As a primer, have a look at:

* `django CMS tutorial`_ for the basic django CMS concepts
* `Using django CMS`_ tutorial

Expected pages
##############

The template expects that the following pages exits:

* Home page (with reverse id "home")
* Code of Conduct page (reverse id "coc")
* Blog page (reverse id "blog")
* Manifesto page (reverse id "manifesto")

Before browsing the site, go to http://localhost:8000/admin/cms/page/ and
create the pages / edit the advanced properties of the existing pages
to set the reverse id.

Default pages
#############

The ``initial_pages.json`` file includes the above pages to help you bootstrapping the website.

To load the pages run::

    python manage.py loaddata initial_pages.json

Compile sass files
------------------

We use `compass`_ to compiles scss files to css::

    compass compile

After that collectstatic files::

    python manage.py collectstatic -l



.. _django-environ: https://github.com/joke2k/django-environ
.. _compass: http://compass-style.org/install/
.. _Using django CMS: http://django-cms.readthedocs.io/en/release-3.4.x/user/index.html
.. _django CMS tutorial: http://django-cms.readthedocs.io/en/release-3.4.x/introduction/index.html

License
-------

All the code except file in ``styles`` and ``djangocon_europe/static/img`` directories are released with BSD-3 clauses

Files in ``styles`` and ``djangocon_europe/static/img`` are not reusable without prior consent.
