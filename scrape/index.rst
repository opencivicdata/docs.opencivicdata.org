Getting Started Writing Scrapers
================================

Before you begin, it is expected that you're a somewhat experienced developer comfortable with `GitHub <http://github.com>`_ and Python.  Some virtualenv knowledge might be helpful as well.

.. note::

    * If you're new to Python you can check out `Python on Codeacademy <http://www.codecademy.com/tracks/python>`_.
    * If you're interested in writing scrapers in Ruby, you may want to check out `pupa-ruby <https://github.com/opennorth/pupa-ruby>`_ by our friends at OpenNorth.

    * To get started with Git/GitHub, there's a `Git tutorial <https://help.github.com/articles/set-up-git#platform-all>`_ to get you started.
    * `virtualenv <httpe://pypi.python.org/pypi/virtualenv>`_ & `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ are optional tools that will help you keep your Python environment clean if you work on multiple projects.

    

These instructions are intended for a POSIX-like operating system, Linux or OSX.  If you're using Windows you'd benefit from using something like `MinGW <http://www.mingw.org/>`_.  If you're using OSX you may find the excellent `OSX-specific docs <https://github.com/opennorth/blank-pupa>`_ published by `Open North <https://github.com/opennorth/>`_  useful.

The first thing to do is to choose a repository to work with.  For the examples here we'll be working with http://github.com/opencivicdata/municipal-scrapers-us/ which is a collection of scrapers for US cities.  If you're working with another country or a special jurisdiction it may be necessary to find a different repository.

Once you've created a fork of the desired repository on GitHub you can set up your local environment.  To do this you'd create a new virtualenv, install `pupa <https://github.com/opencivicdata/pupa>`_, and clone the scraper repo you want to contribute to:

.. code-block:: bash

    # doing the following inside a virtualenv highly recommended
    # Install pupa
    $ pip install -e git+git@github.com:opencivicdata/pupa.git#egg=pupa
    # Clone the repo
    $ git git@github.com:opencivicdata/municipal-scrapers-us.git

Now you're ready to proceed to :doc:`./new`.
