
.. _intro:


Contributing to the Open Civic Data Effort
==============================================

This document is meant to provide a tutorial-like overview of the steps toward contributing a munipal scraper to the Open Civic Data organization on Github.

This page provides information about the project and important links, but you can always skip straight to :ref:`getting_started` if you're anxious to write some code.

About the Project
------------------------------------------

The `opencivicdata <https://github.com/opencivicdata/>`_ organization on Github is an inter-organizational place to contribute open source code for gathering information on government organizations, people, legislation, and events.

.. seealso::

    The `opencivicdata <https://github.com/opencivicdata/>`_ organization on Github:
      `https://github.com/opencivicdata/ <https://github.com/opencivicdata/>`_

The organization's page contains a number of a arbitrarily bug-named (and non bug-named) code repositories directed at scraping information on people and organizations (`pupa <https://github.com/opencivicdata/pupa>`_), code to validate the resulting json data (`larvae <https://github.com/opencivicdata/larvae>`_), a web-based adminstrative interface for editing and manually editing the same data (`anthropod <https://github.com/opencivicdata/anthropod>`_), a set of unique "OCD" identifiers for political geography divisions within the United States and Canada (`ocd-division-ids <https://github.com/opencivicdata/ocd-division-ids>`_), a google group where these and other equally exciting topics are discussed in exuisite detail (open-civic-data@googlegroups.com), a web service for querying the hierarchy of OCD division IDs (`locust <https://github.com/opencivicdata/locust>`_), an API for all the resulting scraped data (`imago <https://github.com/opencivicdata/imago>`_), and repositories of municipal scrapers for cities in the United States (`municipal-scrapers <https://github.com/opencivicdata/municipal-scrapers-us>`_) and Canada (`municipal-scrapers-ca <https://github.com/opencivicdata/municipal-scrapers-ca>`_), and, of course, these lovely docs as well (`municipal-scrapers-docs <https://github.com/opencivicdata/municipal-scrapers-docs>`_).

The work of this Github organization is a result of the combined efforts of `n` different groups working together in a hurricane of awesomeness and mad clown love, including:

- James McKinney
- Others
- Sunlight Foundation

.. _getting_started:

Getting Started
--------------------

If you're a reasonably experienced developer comfortable with `virtualenv <http://www.virtualenv.org/en/latest/>`_ and `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ and don't mind getting set up on your own, simply create a new virtualenv, install pip, clone the scraper repo you want to contribute to, and skip ahead to :ref:`jurisdiction`.

.. code-block:: bash

    $ mkproject municipal-scrapers
    $ pip install -e git+git@github.com:opencivicdata/pupa.git#egg=Package
    $ git clone https://github.com/opencivicdata/municipal-scrapers-us
    # Or to write a scraper for a Canadian city:
    $ https://github.com/opencivicdata/municipal-scrapers-ca

If you need a quick refresher on getting your environment setup, first read about :ref:`environment`.

Onward!