.. _pull_request:

Submitting a Pull Request
=====================================

.. warning::
    Parts of Open Civic Data underwent a large refactor as of mid-2014, some information on this
    page may be out of date.   We're working on updating this documentation as soon as possible.

    We'll remove these messages from pages as they're updated and vetted.


The municipal scraping effort we're working on is extremely friendly to
contributors of all backgrounds, and we accept code contributions via
GitHub Pull Requests.

Before you begin, you should create a GitHub account if you don't already
have one, and learn the basics of using Git (slightly out of scope for this
document). This guide only assumes elementry proficiency with Git.

Don't worry about a perfect patch series, we're all quite happy to go back
and forth and work on changes, if they're needed.

In general, if you just keep the Pull Request short and self-contained,
it will be much easier to review and accept than a change modifying 3
jurisdictions at once.


Fork the repo you want to contribute to
---------------------------------------------

First navigate to the repo you want to contribute to and create a fork. If you're contributing a municipal scraper within the United States, for example, view `that repo's page on Github <https://github.com/opencivicdata/municipal-scrapers-us>`_ and click the ``fork`` button.

This creates a repo (called ``municipal-scrapers-us``, if you've followed the
link just up above) on your personal account that you can commit to.

You can ``clone`` this repo down to your local machine by using `git clone` (do
read up on the `GitHub guide <https://help.github.com/articles/fork-a-repo#step-2-clone-your-fork>`_ if you're having trouble with this step - or git!)

After pulling the repo down, we'll set a new remote called ``upstream`` to help
interact with the ``opencivicdata`` repo later on.

.. code-block:: bash

    $ git remote add upstream git@github.com:opencivicdata/municipal-scrapers-us.git

If you cloned the ``opencivicdata`` repo before you forked the repo on GitHub,
don't worry - you can adjust this fairly quickly!

.. code-block:: bash

    $ git remote rm origin
    $ git remote add origin git@github.com:yourbadself/municipal-scrapers-us.git
    $ git fetch origin

.. seealso::

  Github's docs on forking a repo:
    `https://help.github.com/articles/fork-a-repo <https://help.github.com/articles/fork-a-repo>`_

Submit a pull request
------------------------------------------------------------------------

Before you submit your Pull Request, it's quite handy to run through a quick
checklist of common (and easy to catch) gotchas:

  * Have you added yourself to the ``AUTHORS`` file? If not, please do.
  * Is your Pull Request up-to-date with the ``opencivicdata`` repo? If it's
    not, it might be helpful to jump down to the
    ``Keeping your branch up to date`` section below. It's usually quite easy!

Finally, navigate to commit you made to your forked repo, and click the button to submit a pull request.

.. seealso::

  Github's docs on using pull request:
    `https://help.github.com/articles/fork-a-repo <https://help.github.com/articles/fork-a-repo>`_


Best Practice
-------------

.. note::
    This guide won't get into a generic ``git`` tutorial, and assumes
    elementary proficiency with ``git`` and some knowledge of GitHub.

It's good practice to use a branch when working on the scrapers, this helps
continue to integrate changes into your branch, and helps you compare changes
without much effort. With many people working on the codebase at the same time,
it's likely we'll end up with changes that impact others sometimes. By using
a branch, it's much easier to fix these conflicts.

.. warning::
    Please do make sure you always create a branch off the *master* branch.
    unless you know exaclty why you need to branch off of another branch.

To create a branch, you can simply checkout a new branch (this operation
creates the branch, so don't worry about using ``git branch`` just yet.)

.. code-block:: bash

    $ git checkout -b bugfix/fix-this-broken-jurisdiction

It's common to prefix a branch with one of ``bugfix``, or ``feature`` (or
anything else that's short and desriptive). After the prefix, you should add a
descriptive slug related to the change, so that it's easy to remember
which branch is which. These are sometimes called "Topic branches".

After this, you can check which branch you're working on by running
``git branch``, and looking for the marked branch.

.. code-block:: bash

    $ git branch
    * bugfix/fix-this-broken-jurisdiction
      master

To switch back to the master branch (for any reason), you can ``checkout`` the
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
have changed code in the ``opencivicdata`` repo, and you need to merge
code from "``upstream``" into your working branch.

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

Please do remember to change ``bugfix/fix-this-broken-jurisdiction`` with the
name of your topic branch that you're working on (as seen in the output of the
first command run).

Checking what you've changed
----------------------------

You can check how much has changed at any point very simply, by using
``git diff``. Something like::

    $ git diff master --color

Can come in quite handy when reviewing changes before sending in a Pull
Request.
