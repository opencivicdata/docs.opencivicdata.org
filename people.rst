
.. _people:

Contributing a Municipal Person Scraper
=======================================

This document is meant to provide a tutorial-like overview of the steps toward
contributing a munipal Person scraper to the Open Civic Data project.

This guide assumes you have a working pupa setup. If you don't please
look into the intro / quickstart guide.

.. TODO:: HELP WITH LINKING TO INTRO


Creating a New Person scraper
-----------------------------

Great. So, let's get started. A scraper class (such as a PersonScraper) may
live anywhere, but it's common to break each scraper into it's own file, to
avoid having one massive file.

The pattern is usually to create a `person.py` file next to your Jurisdiction's
`__init__.py`, and create a `FooPersonScraper`, where the string `Foo` is a
nicely human readable slug of your Jurisdiction (such as `BostonPersonScraper`
or `NewYorkCityPersonScraper`.)

This scraper class shall inherit from the `Scraper` class, found in
the `pupa.scrape` module.

The following is a short example::

    from pupa.scrape import Scraper
    class MyFirstPersonScraper(Scraper):
        pass

This class won't do anything, and should even result in an error. Let's iterate
on this concept to work up to something useful.

Every `Person` scraper inherets a `scrape_people` method. Usually it's not
advised to override this method, rather, implementing a proper
`get_people` method (which will `yield` back `Person` objects to `scrape_people`
to save to disk) is the correct way to write a scraper.

You may also yield an iterable of `Person` objects, which helps if you
are scraping both people and committees for the Jurisdiction, but want
to keep the scraper logic in their own routines.

As you might have guessed by now, `Person` scrapers scrape many `People`, as
well as any `Membership` objects that you might find along the way.

Let's take a look at a dead-simple Pupa scraper::

    from pupa.scrape import Scraper, Legislator
    class MyFirstPersonScraper(Scraper):
        def get_people(self):
            js = Legislator(name="John Smith", post_id="Ward 1")
            js.add_source(url="http://example.com")
            yield js

You can see that we create the Legislator, with the only two required
params (`name` and `post_id`, add the source of the data (most of the time
this will be the url that you've called with `urlopen`) and yielded the
Legislator back.

Right. Now let's get back to Memberships. Let's say that we've found
that John Smith has a membership in the Transportation committee::

    from pupa.scrape import Scraper, Legislator
    class MyFirstPersonScraper(Scraper):
        def get_people(self):
            js = Legislator(name="John Smith", post_id="Ward 1")
            js.add_source(url="http://example.com")
            js.add_committee_membership("Transportation",
                                        role="Chair")
            yield js

Of course, all of this is well and good if we find all the data on the
same page. However, commonly, it's much easier to scrape each committee
from the committee pages, since this will often have the data in
an easier-to-scrape format.

Rather than write something like::

    from pupa.scrape import Scraper, Legislator, Committee
    class MyFirstPersonScraper(Scraper):
        def get_people(self):
            js = Legislator(name="John Smith", post_id="Ward 1")
            js.add_source(url="http://example.com")

            members = ["John Smith", "Jos Bleau"]

            committee = Committee("Transportation")
            committee.add_source("http://example.com/committee/transport")
            for member in members:
                committee.add_member(member, role='member')

            yield committee
            yield js

However, as you can imagine, this gets quite out of hand quite quickly. One
common pattern is to split the logic into two sections, such as::


    from pupa.scrape import Scraper, Legislator, Committee
    class MyFirstPersonScraper(Scraper):
        def scrape_legislators(self):
            js = Legislator(name="John Smith", post_id="Ward 1")
            js.add_source(url="http://example.com")
            yield js

        def scrape_committees(self):
            members = ["John Smith", "Jos Bleau"]
            committee = Committee("Transportation")
            committee.add_source("http://example.com/committee/transport")
            for member in members:
                committee.add_member(member, role='member')

            yield committee

        def get_people(self):
            yield self.scrape_legislators()
            yield self.scrape_committees()

It's worth noting that you should keep in mind `scrape_people` *is* a special
function (see above), so you should take care not to override this method.
