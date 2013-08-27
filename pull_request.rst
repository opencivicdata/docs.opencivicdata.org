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


Best Practice
-------------

It's good practice to use a branch when working on the scrapers, this helps
continue to integrate changes into your branch, and helps you compare changes
without much effort.

.. warning::
    Please do make sure you always create a branch off the *master* branch.
    unless you know exaclty why you need to branch off of another branch.

To create a branch, you can simply checkout a new branch (this operation
creates the branch, so don't worry about using `git branch` just yet.)

.. code-block:: bash

    $ git checkout -b bugfix/fix-this-broken-jurisdiction

It's common to prefix a branch with one of `bugfix`, or `feature` (or anything
else that's short and desriptive). After the prefix, you should add a
descriptive slug related to the change, so that it's easy to remember
which branch is which.

After this, you can check which branch you're working on by running
`git branch`, and looking for the marked branch.

.. code-block:: bash

    $ git branch
    * bugfix/fix-this-broken-jurisdiction
      master

To switch back to the master branch (for any reason), you can `checkout` the
branch again.

.. code-block:: bash

    $ git checkout master
    $ git branch
      bugfix/fix-this-broken-jurisdiction
    * master

Keeping your branch up to date
------------------------------

It saves quite a bit of time if you can ensure that all changes have been
incorporated in your branch when sending in a Pull Request. Often times
this is not an issue for short-lived branches, however, sometimes people
have changed code in the `opencivicdata` repo, and you need to merge
code from "`upstream`" into your working branch.

Let's go over how to do this.

.. warning::
    The following assumes you have a setup similar to above. Make sure that
    you have the `upstream` remote set up, and are working on a topic branch.

Firstly, be sure that you've commited all your code, and you're up to date.

.. code-block:: bash

    $ git branch
    * bugfix/fix-this-broken-jurisdiction
      master
    $ git checkout master
    $ git pull upstream master
    $ git checkout bugfix/fix-this-broken-jurisdiction
    $ git merge master

Please do remember to change `bugfix/fix-this-broken-jurisdiction` with the
name of your topic branch that you're working on (see the output of the
first command run).
