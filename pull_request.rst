.. _pull_request:

Submitting a Pull Request
=====================================

To submit a pull request, follow these steps:

Fork the repo you want to contribute to
---------------------------------------------

First navigate to the repo you want to contribute to and create a fork. If you're contributing a municipal scraper within the United States, for example, view `that repo's page on Github <https://github.com/opencivicdata/municipal-scrapers-us>`_ and click the ``fork`` button.

Next set your new remote ``origin`` to your forked repo, and set the original repo as your ``upstream`` repo.

.. code-block:: bash

    $ git remote add origin git@github.com:yourbadself/municipal-scrapers-us.git
    $ git remote add upstream git@github.com:opencivicdata/municipal-scrapers-us.git

.. seealso::

  Github's docs on forking a repo:
    `https://help.github.com/articles/fork-a-repo <https://help.github.com/articles/fork-a-repo>`_

Submit a pull request
------------------------------------------------------------------------

Finally, navigate to commit you made to your forked repo, and click the button to submit a pull request.

.. seealso::

  Github's docs on using pull request:
    `https://help.github.com/articles/fork-a-repo <https://help.github.com/articles/fork-a-repo>`_

