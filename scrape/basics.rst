
.. _basics:

Getting Started Writing Scrapers
===================================

While we strive to make writing scrapers as simple as possible, there are a few prerequisites:

* `Python`_ (or Ruby using `pupa-ruby <https://github.com/opennorth/pupa-ruby>`_)
* `Understanding GitHub`_
* `Scraping Basics`_

If you're already well-versed in Python, GitHub, and basics of web scraping you can skip to `Getting Started`_.

.. note::

    These instructions are intended for Linux or OS X.  If you're using Windows you'll probably benefit from using something like `MinGW <http://www.mingw.org/>`_ or a VM running Linux.  If you're using OS X you may also find the excellent `OS X-specific docs <https://github.com/opennorth/opennorth.ca/wiki/Python-Quick-Start%3A-OS-X>`_ published by `Open North <https://github.com/opennorth/>`_  useful.


Python
---------

If you aren't already familiar with Python you might want to start with `Python on Codecademy <http://www.codecademy.com/tracks/python>`_.

.. note::

    Make sure you are using Python 3.3 or newer.

Having a local development environment is recommended, `virtualenv <httpe://pypi.python.org/pypi/virtualenv>`_ & `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ are optional tools that will help you keep your Python environment clean if you work on multiple projects.


Understanding GitHub
-----------------------

Contributing code requires a free `GitHub <http://github.com>`_ account, if you haven't use Git before there's a `Git tutorial <https://help.github.com/articles/set-up-git#platform-all>`_ to get you started.


Scraping Basics
------------------

It is useful to understand the basic concept of web scraping before beginning, which is somewhat beyond the scope of this documentation. We recommend this `source <http://docs.python-guide.org/en/latest/scenarios/scrape/>`_.

We recommend the `lxml.html <http://lxml.de/lxmlhtml.html>`_ library. If you work with jQuery but haven't used XPath you may also find `lxml.cssselect <http://lxml.de/cssselect.html>`_ useful, though it is a bit more limited.

In our experience spending a few minutes brushing up on the basics of `XPath <https://www.w3schools.com/xml/xpath_syntax.asp>`_ is well worth it as it makes scrapers easier to write and more maintainable in the long run.


Getting Started
-----------------

The first thing to do is to choose a repository to work with, or create a new one.

Most likely you'll be creating a fork of one of the existing scraper repositories:

* `scrapers-us-municipal <https://github.com/opencivicdata/scrapers-us-municipal>`_ - US municipal governments
* `scrapers-us-state <https://github.com/opencivicdata/scrapers-us-state>`_ - US state-level governments
* `scrapers-us-federal <https://github.com/opencivicdata/scrapers-us-federal>`_ - US federal government
* `scrapers-ca <https://github.com/opencivicdata/scrapers-ca>`_ - Canadian legislative
* `influence-usa/scrapers-us-state <https://github.com/influence-usa/scrapers-us-state>`_ - US state influence data

If your scraper falls into one of those categories you should fork it and create a new directory within that repository.  We'd also suggest you work on a branch to make merging changes as easy as possible.

If you're hoping to create a scraper for something not yet covered please email the `Open Civic Data list <https://groups.google.com/forum/#!forum/open-civic-data>`_ and we can work with you to decide the best way to proceed.

Once you've chosen a repository you'll need to install the `pupa` library (the first syllable of pupa is pronounced 'pew' as in 'pew pew pew pew pew'). Also install any other dependencies (like `lxml`) that you'll be using to do your scraping. If you're using an existing repo, you should be able to get all necessary libraries by installing the requirements listed in that repository's requirements.txt file.

An example of how you might configure your setup:

.. code-block:: bash

    # using a virtualenv highly recommended
    $ mkvirtualenv --python `which python3` opencivicdata
    # Install pupa
    $ pip install --upgrade pupa
    # Clone the repo that you forked on GitHub
    $ git clone git@github.com:<yourusername>/scrapers-us-state.git
    # Switch to a branch to make pulling your work later as easy as possible
    $ cd scrapers-us-state
    $ git checkout --branch <new-branch-name>
    # ...do work...
    $ git push --set-upstream origin <new-branch-name>

If you're all set up, you can move on to :doc:`new`.
