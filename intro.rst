
.. _intro:


Contributing to the Open Civic Data Effort
==============================================

.. seealso:

    By the way, these docs are a work in progress--please don't share yet.

The `opencivicdata <https://github.com/opencivicdata/>`_ organization on Github is an inter-organizational place to contribute open source code for gathering information on government organizations, people, legislation, and events. The `opencivicdata <https://github.com/opencivicdata/>`_ page contains a number of arbitrarily bug-named (and non bug-named) code repositories, including:

- code for scraping information on people, organizations, and organizations (`pupa <https://github.com/opencivicdata/pupa>`_)
- code to validate the resulting json data (`larvae <https://github.com/opencivicdata/larvae>`_)
- a web-based adminstrative interface for editing and manually editing the same data (`anthropod <https://github.com/opencivicdata/anthropod>`_)
- a set of unique "OCD" identifiers for political geography divisions within the United States and Canada (`ocd-division-ids <https://github.com/opencivicdata/ocd-division-ids>`_)
- a google group where these and other equally exciting topics are discussed in exuisite detail (open-civic-data@googlegroups.com)
- a web service for querying the hierarchy of OCD division IDs (`locust <https://github.com/opencivicdata/locust>`_)
- an API for all the resulting data (`imago <https://github.com/opencivicdata/imago>`_)
- repositories of municipal scrapers for cities in the United States (`municipal-scrapers-us <https://github.com/opencivicdata/municipal-scrapers-us>`_) and Canada (`municipal-scrapers-us <https://github.com/opencivicdata/municipal-scrapers-ca>`_)
- and, of course, these lovely docs as well (`municipal-scrapers-docs <https://github.com/opencivicdata/municipal-scrapers-docs>`_).

The storage format for people, organizations, and events collected using these tools is the excellent `Popolo JSON format <http://popoloproject.com/>`_.

.. seealso::

    The `opencivicdata <https://github.com/opencivicdata/>`_ organization on Github:
      `https://github.com/opencivicdata/ <https://github.com/opencivicdata/>`_

    The Popolo Project homepage:
        `http://popoloproject.com/ <http://popoloproject.com/>`_

The work of this Github organization is a result of the combined efforts of `n` different groups working together, including:

- James McKinney
- Others XXX: insert more groups
- Sunlight Foundation

.. _getting_started:

Getting Started
--------------------

If you need a quick refresher on getting your python environment setup for scraper development, first read about :ref:`environment`.

If you're a reasonably experienced developer comfortable with `virtualenv <http://www.virtualenv.org/en/latest/>`_ and `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ and don't mind getting set up on your own, simply create a new virtualenv, install `pupa <https://github.com/opencivicdata/pupa>`_, clone the scraper repo you want to contribute to, and skip ahead to :ref:`jurisdiction`.

.. code-block:: bash

    $ # Create a new virtualenv
    $ mkproject municipal-scrapers
    $ # Install pupa
    $ pip install -e git+git@github.com:opencivicdata/pupa.git#egg=Package
    $ # Copy the pupa default settings:
    $ curl -o pupa_settings.py https://raw.github.com/opencivicdata/pupa/master/pupa/core/default_settings.py
    $ # Clone the repo
    $ git clone https://github.com/opencivicdata/municipal-scrapers-us
    $ # Or to write a scraper for a Canadian city:
    $ https://github.com/opencivicdata/municipal-scrapers-ca

In addition, if you use OS X as your operating system, see the excellent `OSX-specific docs <https://github.com/opennorth/blank-pupa>`_ published by `Open North <https://github.com/opennorth/>`_, then move on to :ref:`jurisdiction`.