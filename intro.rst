
Contributing a Municipal Scraper
======================================

This document is meant to provide a tutorial-like overview of the steps toward contributing a munipal scraper to the Open Civic Data project.

The green arrows designate "more info" links leading to advanced sections about the described task.


Setting Up Your Environment
------------------------------------

The recommended way to manage dependencies in python is with `virtualenv <https://pypi.python.org/pypi/virtualenv>`_. If virtualenv is new territory for you, go there first and get set up, then check out `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ for extra convenience in setting up, activating, deactivating, and tearing down virtualenvs.

To get started on your first scraper, create a new virtualenv to manage the dependencies for your code. ::

    $ cd ~/.virtualenvs
    $ virtualenv municipal-scrapers

Note that you can write scrapers in python 2.7 or python 3.3 or higher.
To create a virtualenv using a version of python other than your system version, use the -p command line flag: ::

    $ virtualenv -p`which python3.3` municipal-scrapers

Next activate your virtualenv: ::

    $ source municipal-scrapers/bin/activate

Next, create a directory to hold your scrapers. (Don't be silly, of course you'll want to write more than one.) ::

    $ mkdir ~/projects/municipal scrapers
    $ cd !:1

And for the record, if you're using `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_, the previous four steps can be abbreviated to: ::

    $ mkproject municipal-scrapers

Finally, install `pupa <https://github.com/opencivicdata/pupa>`_, the scraper framework we'll be using to scrape municipal data. ::

    $ pip install -e git+git@github.com:opencivicdata/pupa.git#egg=Package


Creating a New Scraper
----------------------------------------

Now you're ready to start a new scraper! To copy a skeleton project into a new scraper directory, use pupa's init command. Let's create a new scraper for Albequerque::

    $ pupa init albequerque

Pupa will copy the skeleton project into a new albequerque directory with the following structure. ::

    albequerque/
    ├── __init__.py
    └── people.py


Open up the new :file:`albequerque/__init__.py` file and check out it's contents. It will look like this:

.. literalinclude:: ../pupa/example/__init__.py

This file contains a single subclass of a Jurisdiction base class. The jursdiction class represents the municipality we're scraping information for, and is the place we'll store the metadata required during the scrape. To get started, all we have to do is edit the metadata on this class to be specific to Albequerque.

Edit the Jurisdiction's Metadata
--------------------------------------

Take a look at the Albequerque-specific changes below:

.. literalinclude:: albequerque.__init__.diff
    :language: diff

* Change the `jurisdiction_id`
  * The first edit changes the example `jurisdiction_id` to make it specific to Albequerque, New Mexico, by setting the state abbreviation to "nm" and the place name to "albequerque," followed by a slash and the word "council."

.. admonition:: Read more about OCD identifiers

    :ref:`ocdid`

* Change the Basic Jurisdiction Details
  * Next notice that we changed "name", "legislature_name", "legislature_url", all of what are pretty self-explanatory.

Edit the Term Information
+++++++++++++++++++++++++++++++

.. admonition:: Read more about terms

    :ref:`term`

.. _ocdid:

OCD Identifiers
------------------------------------------

Blah blah.

.. _term:

How to Choose the right value for Term
+++++++++++++++++++++++++++++++++++++++++++

Blah blah.