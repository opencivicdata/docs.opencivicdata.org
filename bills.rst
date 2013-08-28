
.. _bills:

Contributing a Municipal Bill Scraper
=====================================

Bill scrapers are scrapers that pull down all legislatition on a jurisdiction's
legislative website (including, but not limited to things like House and Senate
Resolutions, Bills or city ordinances).

Scrapers should scrape all bills from a session every single night.

Let's start out with a simple scraper::

            from pupa.scrape import Scraper
            from pupa.models import Bill
            class MyFirstBillScraper(Scraper):
                def get_bills(self):
                    bill = Bill(name="HB 101",
                                session=self.session,
                                title="A bill for an act for pudding",
                                organization=self.jurisdiction.metadata['name'])
                    bill.add_source("http://example.com")
                    yield bill

Just as with the other examples, you can see that this is incomplete
and very basic. However, let's ignore the hard-coding of the Bill data (and
assume that the data is coming from a live website), and work with the Bill
object a little.

Let's add some basic actions::

            from pupa.scrape import Scraper
            from pupa.models import Bill
            class MyFirstBillScraper(Scraper):
                def get_bills(self):
                    bill = Bill(name="HB 101",
                                session=self.session,
                                title="A bill for an act for pudding",
                                organization=self.jurisdiction.metadata['name'])
                    bill.add_action(description="Introduced",
                                    actor="upper",
                                    date="2013-08-28")
                    bill.add_source("http://example.com")
                    yield bill

You might notice that ``date`` is a string, not a ``datetime``. This is becase
we may not have all the information needed to fill out a complete ``datetime``
object. For a bill action, we should at least have information out to the
day in which an action was taken, so try to fill that out. Information on
the time would be nice as well, but is not always there.


