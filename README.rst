Django + Celery example
============================================

This is a very basic and useless example of Celery extending Django with asynchronous tasks, it consist of a simple task that counts to the provided number and sleeps one second in every iteration, using AJAX to check the status of this task from the client side.

Prerequisites
-------------

A development environment that runs `Oracle's VirtualBox`_, Vagrant_, Python_ and Fabric_.

.. _Oracle's VirtualBox: https://www.virtualbox.org/

.. _Vagrant: http://www.vagrantup.com/

.. _Python: http://www.python.org/

.. _Fabric: http://www.fabfile.org


Configuring your virtual environment
------------------------------------

1. Clone the reposiroty.

.. code-block:: bash

    $ git clone git@github.com:gGonz/django_celery_example.git

2. Create the virtual machine.

.. code-block:: bash

   $ cd django_celery_example
   $ vagrant up

3. Build the environment inside the virtual machine.

..  code-block:: bash

    $ fab vagrant bootstrap

4. Run Celery on the virtual machine.

.. code-block:: bash

    $ vagrant ssh                               # ssh into the virtual machine
    $ cd django_site                            # cd into the site directory
    $ nohup python manage.py celery worker &    # run Celery in the background
    $ exit                                      # close the ssh session
    

5. Run the virtual server.

.. code-block:: bash

    $ fab vagrant runserver

6. Open your browser and go to your virtual server on ``http://127.0.0.1:8000``
