================
Style Guidelines
================

General
=======

Version Control
---------------

Code is managed in git. Changes should contain clear, descriptive
English text describing the thought that went into why you're making the
change, rather than describing what you changed.

In two weeks, It's a lot more helpful to know *why* you changed `foo` to
`foo_with_bar`, than read a commit message that says
`change foo to be foo_with_bar`.

The first line of a Git commit should be 50 chars or less, followed by a
blank line, followed by a longer description of the changeset (if required).
The long description should contains lines that are all under 72 chars.


Line Length
-----------

Please try to keep line length under 80 chars wide, 100 characters should be
considered the hard limit.


Open Civic Data Workflow
========================


Submitting Changes
------------------

All changes should be submitted in the form of a Pull Request. Small changes,
even ones that appear to be quite simple, can often prove to cause issues down
the line.


Suggested Git Branching Model
-----------------------------

It's strongly encouraged to use a sane Git branching model, one such model is:

Maintain two remotes::

    upstream: Open Civic Data repo
    origin:   Fork of the repo

Always keep `upstream/master`, `origin/master` and `refs/heads/master` 100%
ABSOLUTELY in sync. Before making a new branch, or sending in a PR, give master
a pull, and make sure things are all sync'd nicely.


Here's an example of creating a new branch::

    git checkout master
    git checkout -b paultag/bugfix/fix-typo-in-readme
    git push -u origin paultag/bugfix/fix-typo-in-readme

It should go without saying that both `paultag` and `bugfix` should be changed
to match your username, and the flavor of branch is usually something like
`feature`, or `bugfix`.


Python Code Guidelines
======================

Python Version
--------------

Please use an up to date Python. All new development is Python 3.4+ only. All
efforts to support older versions of Python 3, or even Python 2 are on a purely
best-effort basis, and large refactors of code to make it Python 2 compatable
will likely be rejected.


Code Standards
--------------

All code must follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_.
You may check compliance with PEP8 by using the `flake8` tool.

::

    pip install flake8
    flake8 .


Please address outstanding `flake8` issues. Any test suites should also test
code style.


Comments
--------

Please add comments and descriptive docstrings to your code. Clearly, if the
code doesn't require them, that's OK, but comments can be quite helpful later on.

Sprinkle them around like sriracha.


Trailing Spaces
---------------

Please ensure that we don't have any trailing spaces on any code lines or
commit lines.
