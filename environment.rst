
.. _environment:


Setting Up Your Environment
===============================

The recommended way to manage dependencies in python is with `virtualenv <https://pypi.python.org/pypi/virtualenv>`_. If virtualenv is new territory for you, go there first and get set up, then check out `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ for extra convenience in setting up, activating, deactivating, and tearing down virtualenvs.

To get started on your first scraper, create a new virtualenv to manage the dependencies for your code.

.. code-block:: bash

    $ cd ~/.virtualenvs
    $ virtualenv municipal-scrapers

    # Next activate your virtualenv.
    $ source municipal-scrapers/bin/activate

    # Next, clone the scraper repo you want to contribute to.
    # For scrapers related to cities in the US, its:
    $ git clone https://github.com/opencivicdata/municipal-scrapers-us
    # Or to write a scraper for a Canadian city:
    $ https://github.com/opencivicdata/municipal-scrapers-ca

.. seealso::

    Note to self:
        Is this the correct url for Canada muni scrapers? Or is it Open North's repo? git@github.com:opennorth/mycityhall-scrapers.git

Note that you can write scrapers in python 2.7 or python 3.3 or higher.
To create a virtualenv using a version of python other than your system version, use the -p command line flag:

.. code-block:: bash

    $ virtualenv -p`which python3.3` municipal-scrapers

And for the record, if you're using `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_, the previous four steps be abbreviated to:

.. code-block:: bash

    $ mkproject municipal-scrapers

Finally, install `pupa <https://github.com/opencivicdata/pupa>`_, the scraper framework we'll be using to scrape municipal data.

.. code-block:: bash

    $ pip install -e git+git@github.com:opencivicdata/pupa.git#egg=Package

Go Forth and Contribute
---------------------------

And now you're ready to get busy :ref:`jurisdiction`.