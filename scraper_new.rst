Creating a New Scraper
======================

Now you're ready to start a new scraper! To copy a skeleton project into a new scraper directory, use pupa's :program:`init` command. Let's create a new scraper for Albuquerque, New Mexico:

.. code-block:: bash

    $ pupa init albuquerque

Pupa will copy a skeleton project into a new albuquerque directory with the following structure.

.. code-block:: bash

    $ tree albuquerque/
    albuquerque/
    ├── __init__.py
    └── people.py


Open up the new :file:`albuquerque/__init__.py` file and check out it's contents. It will look like this:

.. literalinclude:: ../pupa/example/__init__.py

This file contains a single subclass of a Jurisdiction base class. The jurisdiction class represents the municipality we're scraping information for, and is the place we'll store the metadata required during the scrape. To get started, all we have to do is edit the metadata on this class to be specific to Albuquerque.

Notice also the `get_scraper` function. Your jurisdiction class needs to implement this simple function to define what scraper gets used given a `term`, `session`, and `scraper_type`. `scraper_type` will be a string equal to ``"people"``, ``"bills"``, or ``"events"``. As you can see, the default implementation of this function simply returns the `PeopleScraper` if the `scraper_type` is 'people', but this function can easily scale up to supply a different people scraper for different terms or even sessions, which might be necessary if the municipality rolls out a new website for a new term, requiring a new scraper.

This is all well and good, but now let's hack this example file to customize it to work for Albuquerque.

Edit the Jurisdiction's Metadata
--------------------------------------

Take a look at the Albuquerque-specific changes below:

.. literalinclude:: includes/__init__.py.diff
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

Step 1: Figure out the `term` lenth
***************************************

If the municipality has a uniform term, use that; if it has staggered terms, the term length is the length of time in between elections. So if council members serve two-year terms, but each year staggered elections are held in which only half of the council members are up for re-election, the term length is one year.

Step 2: Figure out the start year of the `term`
***************************************************

As for the value you'll enter into the metadata as the term's `name`, by convention the project uses a year range, like '2013-2014', so you'll also need to figure out the year of the most recent election.

How does one go about locating this information? An excellent place to look is in the relevant municipality's town charter or equivalent document. In this case, I found Albuquerque's town charter by simply googling "Albuquerque charter" and clicking the first result, which was a `PDF of the charter <http://www.cabq.gov/council/documents/charter-review-task-force/city_charter.pdf>`_ located on the town's official .gov website: `http://www.cabq.gov/ <http://www.cabq.gov/>`_. Perusing the table of contents, I noticed a section entitled "Terms of Office" in Article IV, section 4 of the charter. Here's what it says:

  "The terms of the office of a Councilor, unless sooner recalled or removed, shall begin on December 1st of the year of election and be four years or until a successor is duly elected and qualified. The Councillors may succeed themselves in office. The terms of office of Councillors shall be staggered with four or five districted Councillors elected every two years."

Aha. In Albuquerque, each council member serves a four year term, and staggered elections are held every two years. So our term length will be two years. The final step is to figure out the start year in the range we'll use as the term `name` value, and to do that, we'll again turn to Albuquerque's official website. This time, some quick research took me to the city's `2013 General Election Calendar <http://www.cabq.gov/voting-elections/candidate-information/2013-general-election-information/2013-general-election-calendar>`_. So our term will begin in 2013 with a two-year duration, making our term `name` value '2013-2015'.

Accordingly, in the diff above we changed the name of the term to ``"2013-2015"``, added the start and end years of the term as integers, and added the current legislative session of ``"2013"`` to the term's `sessions` list, which may expand in the future to include the 2014 and 2015 sessions.

Sumbit A Pull Request
-------------------------

Now that we have created some thoughtful metadata, you might considering :ref:`pull_request`. It's arguably a little premature at this stage, but by all means, read about how to do that if you're inclined.

.. seealso::

  Github's docs on using pull request:
    `https://help.github.com/articles/using-pull-requests <https://help.github.com/articles/using-pull-requests>`_

Get Up and Stretch! We're done editing the metadata for Albuquerque, and next we'll write the people scraper. Go get a refill, then continue on to :ref:`people`.
