
.. _new:

Creating a New Scraper
======================

If you've followed the directions at :doc:`index` then you're ready to start a new scraper.

We'll be creating a new people scraper for Seattle, but simply subsititute your own city name for Seattle as you follow these next few steps.

To copy a skeleton project into a new scraper directory, use pupa's :program:`init` command.  It will ask you a few questions.

.. code-block:: bash

    $ pupa init seattle
    division id (look this up in the opencivicdata/ocd-division-ids repository):
    jurisdiction name: Seattle City Council
    official URL: http://seattle.gov/council/
    create people scraper? [Y/n]: y
    create events scraper? [y/N]: n
    create bills scraper? [y/N]: n
    create votes scraper? [y/N]: n

(For beginners we recommend starting with just a single scraper, it is easy to create more scrapers later.)

In order to prevent duplication and redundancy, standardized division-id's are available in the repository `ocd-division-ids <https://github.com/opencivicdata/ocd-division-ids>`_. In the identifiers subdirectory, you'll find full csvs for each of the jurisdicitions we've entered so far - open the appropriate one and find the relevant division. If you are interested in adding a new geography or a new division within an existing geography, please contact open-civic-data@googlegroups.com.

This process should have created a new directory (named for whatever argument you gave to :program:`pupa init`, seattle in this case) which contains an __init__.py and a file for each scraper you asked pupa to create.

Your __init__.py should look something like this::

    from pupa.scrape import Jurisdiction
    from .people import SeattlePersonScraper


    class Seattle(Jurisdiction):
        division_id = "ocd-division/country:us/state:wa/place:seattle"
        name = "Seattle City Council"
        url = "http://seattle.gov/council/"
        scrapers = {
            "people": SeattlePersonScraper,
        }

        def get_organizations(self):
            org = Organization(name="org_name",
                classification="legislature")

            org.add_post(
                label="position_description",
                role="position_type")

            yield org


Every scraper is required to provide a `Jurisdiction` subclass.  :program:`pupa init` created a working subclass but you may want to specify additional details.  For a full description of all the options visit :doc:`../data/jurisdiction`.

You'll also notice that your class defines a list of scrapers.  These are used by :program:`pupa update` when deciding which scrapers to run.  By default `pupa update` will run all of your scrapers, but you can look at :doc:`../pupa/update` for further details.

In addition, every scraper needs to define at least one organization. In this case, the organiztion will likely be the Seattle City Council. Replace the text org_name with the name of the organization you're scraping. The organization also needs to have a classification. Select the most appropriate from this list, and replace "legislature" with it:

* legislature
* executive
* upper
* lower
* party
* committee
* commission


Finally, the file created by pupa init adds posts to the organization. Scrapers can run without posts, so if you won't be looking at people, feel free to delete this line. But if you will be scraping people, you should add the posts you'll be scraping. For example, for the Seattle City Council, you'll want to add a post for each of the 9 seats (called Positions in Seattle). For Position 1, we'd set the label to "Council Position 1" and the role to "Councilmember".

Once the orginazitaion is created and the positions are added, yield the organization. (If you're not familiar with yield and generators in python, we recommend `this talk <https://www.youtube.com/watch?v=EnSu9hHGq5o#t=13m00s>`_ from PyCon 2013.)

You can create as many organizations as needed. For Seattle, you might also want an executive so you can scrape the mayor's office, and add the mayor as a position. Yield each organization after adding it. Don't worry about adding every committee - organizations such as committees can be added later when you find them with a scraper.

You're now set up to scrape data! Next up we'll discuss how to scrape events, bills and people.
