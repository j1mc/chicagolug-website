The Chicago GNU/Linux User Group Website
========================================

A very simple database-free website using the [Flask microframework](http://flask.pocoo.org).

You can see it running at [http://chicagolug.org](http://chicagolug.org)

How to install and run locally
------------------------------

(Assumes you have Pip, virtualenv and virtualenvwrapper installed).

    git clone http://gitorious.org/chicagolug-org/chicagolug-flask
    # Yes, gitorious.org is the primary code-host. Github is just a mirror.
    cd chicagolug-flask
    virtualenv venv
    source venv/bin/activate
    pip install flask markdown PyYAML gunicorn pygments
    python wsgi/chicagolug.py

The development server should now be running on [localhost:5000](http://localhost:5000)

