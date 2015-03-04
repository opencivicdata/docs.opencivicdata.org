Creating a New Scraper
======================

.. warning::
    Parts of Open Civic Data underwent a large refactor as of mid-2014, some information on this
    page may be out of date.   We're working on updating this documentation as soon as possible.

    We'll remove these messages from pages as they're updated and vetted.


If you've followed the directions at :doc:`index` then you're ready to start a new scraper.

We'll be creating a new people scraper for Seattle, but simply subsititute your own city name for Seattle as you follow these next few steps.

To copy a skeleton project into a new scraper directory, use pupa's :program:`init` command.  It will ask you a few questions.

.. code-block:: bash

    $ pupa init seattle
    jurisdiction name: Seattle City Council
    jurisdiction id: ocd-jurisdiction/country:us/state:wa/place:seattle/council
    official URL: http://seattle.gov/council/
    create people scraper? [Y/n]: y
    create events scraper? [y/N]: n
    create bills scraper? [y/N]: n
    create votes scraper? [y/N]: n

(For beginners we recommend starting with just a single scraper, it is easy to create more scrapers later.)

This should have created a new directory (named for whatever argument you gave to :program:`pupa init`) which contains an __init__.py and a file for each scraper you asked pupa to create.

Your __init__.py should look something like this::

    from pupa.scrape import Jurisdiction
    from .people import SeattlePersonScraper


    class Seattle(Jurisdiction):
        jurisdiction_id = "ocd-division/country:us/state:wa/place:seattle/council"
        name = "Seattle City Council"
        url = "http://seattle.gov/council/"
        scrapers = {
            "people": SeattlePersonScraper,
        }

Every scraper is required to provide a `Jurisdiction` subclass.  :program:`pupa init` created a working subclass but you may want to specify additional details.  For a full description of all the options visit :doc:`../data/jurisdiction`.

You'll also notice that your class defines a list of scrapers.  These are used by :program:`pupa update` when deciding which scrapers to run.  By default `pupa update` will run all of your scrapers, but you can look at :doc:`../pupa/update` for further details.

This is all well and good, but now let's hack this example file to customize it to work for Albuquerque.

Edit the Jurisdiction's Metadata
--------------------------------------

Take a look at the Albuquerque-specific changes below:

.. literalinclude:: /includes/__init__.py.diff
    :language: diff

Let's go over the changes made above one at a time.

- Change the `jurisdiction_id`:

  The first edit changes the example `jurisdiction_id` to make it specific to Albuquerque, New Mexico, by setting the state abbreviation to "nm" and the place name to "albuquerque," followed by a slash and the word "council." Adding "council" at the end of the `jurisdiction_id` is simply a convention this project uses when scraping information about a city council. (You can also read more about :ref:`ocdid`.)

- Change the Basic Jurisdiction Details:

  Next notice that we changed `name`, `legislature_name`, `legislature_url`, all of which are pretty self-explanatory. The `legislature_url` is the url of the Albuquerque City Council website we'll be scraping.

- Edit the `parties` information:

  Enter the parties information for the target jurisdiction.

Alright, these three changes were easy. Now let's enter the jurisdiction's `terms` and `sessions` info.

Choosing the appropriate values for `terms` and `sessions`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This is the only really tricky part of starting a new jurisdiction. The term is the length of time that officials in the Albuquerque City Council hold office. Sometimes this is straight-forward, and a few minutes of strategic googling reveals that the council members all serve predictable two-year terms and come up for election every even numbered year, for example. But some jurisdictions have staggered elections in which only some of the council members participate in a given election, while others will be up for election during a later election.

The rule for determining the term length is actually pretty simple:

Step 1: Figure out the `term` length
***************************************

If the municipality has a uniform term, use that; if it has staggered terms, the term length is the length of time in between elections. So if council members serve two-year terms, but each year staggered elections are held in which only half of the council members are up for re-election, the term length is one year.

Step 2: Figure out the start year of the `term`
***************************************************

As for the value you'll enter into the metadata as the term's `name`, by convention the project uses a year range, like '2013-2014', so you'll also need to figure out the year of the most recent election.

How does one go about locating this information? An excellent place to look is in the relevant municipality's town charter or equivalent document. In this case, I found Albuquerque's town charter by simply googling "Albuquerque charter" and clicking the first result, which was a `PDF of the charter <http://www.cabq.gov/council/documents/charter-review-task-force/city_charter.pdf>`_ located on the town's official .gov website: `http://www.cabq.gov/ <http://www.cabq.gov/>`_. Perusing the table of contents, I noticed a section entitled "Terms of Office" in Article IV, section 4 of the charter. Here's what it says:

  "The terms of the office of a Councilor, unless sooner recalled or removed, shall begin on December 1st of the year of election and be four years or until a successor is duly elected and qualified. The Councillors may succeed themselves in office. The terms of office of Councillors shall be staggered with four or five districted Councillors elected every two years."

Aha. In Albuquerque, each council member serves a four year term, and staggered elections are held every two years. So our term length will be two years. The final step is to figure out the start year in the range we'll use as the term `name` value, and to do that, we'll again turn to Albuquerque's official website. This time, some quick research took me to the city's `2013 General Election Calendar <http://www.cabq.gov/voting-elections/candidate-information/2013-general-election-information/2013-general-election-calendar>`_. So our term will begin in 2013 with a two-year duration, making our term `name` value '2013-2015'.

Accordingly, in the diff above we changed the name of the term to ``"2013-2015"``, added the start and end years of the term as integers, and added the current legislative session of ``"2013"`` to the term's `sessions` list, which may expand in the future to include the 2014 and 2015 sessions.

Testing your scraper
--------------------

As you develop it will be a good idea to run the scraper to ensure that the output JSON is in good shape.

Run the scraper::

    $ pupa update albuquerque

Where ``albuquerque`` is simply a Python-importable path to your Jurisdiction
definition. From there, the ``jurisdiction`` object will be able to tell
``pupa`` where to find the scrapers.

In addition, there are some useful arguments to know about.

Firstly, when doing local testing, ``--fast`` disables Pupa's scrape throttling,
and uses the ``scrape_cache`` to prevent fetching pages over the line. This is
useful when doing prototyping, but shouldn't be used regularly, since it puts
more load on these websites, and will read stale data (if your cache stays
around).

Secondly, if you've not got MongoDB installed, it's useful to pass ``--scrape``
to ``pupa``, to prevent the ``--import`` and ``--report`` stages from running,
which require a running MongoDB server to connect to.

Lastly, being able to restrict which scraper gets run via ``--people``,
``--bills``, ``--events``, ``--votes`` and ``--speeches`` may help bring
overall scrape time down.

At any point, you can run::

    $ pupa update -h


To get most up-to-date information regarding the invocation of Pupa.

Usually, during rapid development, the invocation would look something like::

    $ pupa update albuquerque --fast --bills

After this completes, the data will be in the ``scraped_data`` folder. Each
OpenCivic object that gets saved will be written to
``scraped_data/<jurisdiction_id>/<type>_<tmp_id>.json``.

This object will be a JSON-encoded OpenCivic object, which is a well-documented
and defined format for Government data.

By spot-checking a few of the entries, you can check to see if data
looks funny, or if things aren't being categorized properly.

.. NOTE::
    This is likely to change, eventually a MongoDB-based viewer will be
    a better way to view such data. For now, most of us are checking up on
    the raw JSON as we go.

If you want to spot-check some data, using a modern POSIX system should
allow you to run something similar to::

    $ python -mjson.tool $(ls | shuf -n 1) | vim -

Feel free to change ``vim`` to whatever editor you prefer for such tasks.

If you do use vim, there's a helpful
`JSON Plugin <http://www.vim.org/scripts/script.php?script_id=1945>`_

Post-import spot-checking
+++++++++++++++++++++++++

Validating data in the database is slightly harder (since you have to have
a running MongoDB server), but allows you to look at the data *after* the
import process, which means there will be less duplicated entries, and IDs
will be resolved.


By default, Pupa will import entries into the ``opencivicdata`` database,
but this *may* be overridden on a per-project basis using a ``pupa_settings``
entry. Double-check by trying to import ``pupa_settings``, and reading it's
``MONGO_DATABASE`` attribute. If the attribute isn't present, or the settings
file is otherwise missing, it'll default back to ``opencivicdata`` (you can
always check the default database by running something like
``python -c "import pupa.core; print pupa.core.default_settings.MONGO_DATABASE"``
).

The ``pupa`` repo contains a very basic static checking script, called
``scruffy``. It's advised that you run ``scruffy`` over your database if you
have it imported anyway. You can run ``scruffy`` by going to your ``pupa``
source repo, and ``cd`` into ``tools``.

You can invoke ``scruffy`` by running something like::

    $ python -m scruffy > report.json

Wich will drop a JSON file full of potental issues in the database. Some of
these are not severe (such as unmatched memberships), and others may be the
result of buggy code (people without memberships, etc), but there's a good deal
of code to do basic sanity checking on OCD objects stored in the Database.

If you want a quick overview on what tags are present in the report, you can
run a command similar to::

    $ python -m json.tool report.json | grep "tagname" | sort | uniq -c

To get a rough feel for what sorts of errors have been detected in the
database.

The entries in the ``scruffy`` report also contain the IDs of the object which
presented an error. You can use this to look it up from the DB. The
``collection`` attribute will let you know which MongoDB collection this item
is present in, and the ``id`` will give you the MongoDB ``_id``.

As example, given the following JSON fragment::

        {
            "collection": "people",
            "data": {
                ...
            },
            "id": "ocd-person/ed7ff556-f9f9-11e2-b7c7-f0def1bd7298",
            "severity": "important",
            "tagname": "..."
        },

We can get the record in question by working with::

    $ mongodb opencivicdata
    > db.people.find({"_id": "ocd-person/ed7ff556-f9f9-11e2-b7c7-f0def1bd7298"})[0]
    {
        ...
    }

where the MongoDB database (``opencivicdata`` above) is from your Pupa config,
and the collection (``people`` above) is the ``collection`` from the Scruffy
report, and the ``_id`` is set to the ``id`` in the scruffy report.

Unless this object is something transiant (such as a ``Membership`` object
that was converted), the ``_id`` should stay stable enough for testing locally.

Once you deploy the code elsewhere, new IDs will be generated, since the
database will not have an ID assigned for that entity yet.

Sumbit A Pull Request
-------------------------

Now that we have created some thoughtful metadata, you might considering :ref:`pull_request`. It's arguably a little premature at this stage, but by all means, read about how to do that if you're inclined.

.. seealso::

  Github's docs on using pull request:
    `https://help.github.com/articles/using-pull-requests <https://help.github.com/articles/using-pull-requests>`_

Get Up and Stretch! We're done editing the metadata for Albuquerque, and next we'll write the people scraper. Go get a refill, then continue on to :ref:`people`.
