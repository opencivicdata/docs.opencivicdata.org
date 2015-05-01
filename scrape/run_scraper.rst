Running the Scraper
====================

As you develop it will be a good idea to run the scraper to ensure that the output JSON is in good shape.

Run the scraper::

    $ pupa update seattle

Where ``seattle`` is simply a Python-importable path to your scraper directory. From there, the ``jurisdiction`` object will be able to tell
``pupa`` where to find the scrapers.

In addition, there are some useful arguments to know about.

Firstly, when doing local testing, ``--fast`` disables Pupa's scrape throttling,
and uses the ``scrape_cache`` to prevent fetching pages over the line. This is
useful when doing prototyping, but shouldn't be used regularly, since it puts
more load on these websites, and will read stale data (if your cache stays
around).

Secondly, if don't have an opencivicdata postgres database set up, it's useful to pass ``--scrape``
to ``pupa``, to prevent the ``--import`` and ``--report`` stages from running.

Lastly, being able to restrict which scraper gets run by indicating ``people``, ``bills``, ``events`` or ``votes`` after the jurisdiction.

At any point, you can run::

    $ pupa update -h


To get most up-to-date information regarding the invocation of Pupa.

Usually, during rapid development, the invocation would look something like::

    $ pupa update seattle people --fast


Validating Data
------------------

After this completes, the data will be in the ``scraped_data`` folder. Each OpenCivic object that gets saved will be written to ``scraped_data/<jurisdiction_id>/<type>_<tmp_id>.json``.

This object will be a JSON-encoded OpenCivic object, which is a well-documented and defined format for Government data.

By spot-checking a few of the entries, you can check to see if data looks funny, or if things aren't being categorized properly.


If you want to spot-check some data, using a modern POSIX system should
allow you to run something similar to::

    $ python -m json.tool $(ls | shuf -n 1) | vim -

Feel free to change ``vim`` to whatever editor you prefer for such tasks.

If you do use vim, there's a helpful
`JSON Plugin <http://www.vim.org/scripts/script.php?script_id=1945>`_
