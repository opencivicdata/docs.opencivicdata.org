
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
