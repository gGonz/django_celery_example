from fabric.api import env, local, run, cd, task, require, settings
from fabric.colors import green, red


#
# Environments
#
@task
def vagrant():
    """
    Local development environment (Vagrant virtual machine).

    """
    # User
    env.user = 'vagrant'

    # Connects to the local SSH
    env.hosts = ["127.0.0.1:2222"]

    # SSH key created by Vagrant
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1].replace('"', '')

    # The django directory
    env.site_dir = '~/django_site'


#
# Tasks
#
@task
def bootstrap():
    """
    Builds the development environment from an "empty" system with
    the required dependencies installed.

    """
    require('site_dir')

    # Configuring PostGIS
    run('sudo su -c "createuser --createdb vagrant" postgres')

    # Creating the database
    run('createdb celery_example_db -l en_US.UTF-8 -E UTF8 -T template0')

    # Syncs the db and collects the static files
    syncdb()
    collectstatic()


@task
def resetdb():
    """
    Drops the database and creates a new empty one.

    """
    require('site_dir')
    run('dropdb tuola')
    run('createdb celery_example_db -l en_US.UTF-8 -E UTF8 -T template0')
    syncdb()

#
# manage.py
#
@task
def syncdb():
    require('site_dir')
    with cd(env.site_dir):
        run('python manage.py syncdb --noinput')

@task
def collectstatic():
    require('site_dir')
    with cd(env.site_dir):
        run('python manage.py collectstatic --noinput')


@task
def runserver():
    require('site_dir')
    with cd(env.site_dir):
        run('python manage.py runserver_plus 0.0.0.0:8000')
