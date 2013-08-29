
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

Let's take a look at adding a bit more data::

            from pupa.scrape import Scraper
            from pupa.models import Bill
            class MyFirstBillScraper(Scraper):
                def get_bills(self):
                    bill = Bill(name="HB 101",
                                session=self.session,
                                title="A bill for an act for pudding",
                                organization=self.jurisdiction.metadata['name'])

                    bill.add_sponsor(name="John Smith",
                                     sponsorship_type="Primary",
                                     primary=True,
                                     entity_type="person")
                    # ``sponsorship_type`` is whatever the upstream site
                    # calls this sponsorship type.

                    bill.add_subject("pudding")

                    bill.add_document_link(
                        name="Fiscal Report",
                        url="http://example.com/2013/pudding/fiscal-report.pdf",
                        mimetype="application/pdf")

                    bill.add_document_link(
                        name="Fiscal Report",
                        url="http://example.com/2013/pudding/fiscal-report.odt",
                        mimetype="application/vnd.oasis.opendocument.text")

                    bill.add_version_link(
                        name="As Introduced",
                        url="http://example.com/2013/hb101-introduce.pdf",
                        mimetype="application/pdf")

                    bill.add_action(description="Introduced",
                                    actor="upper",
                                    date="2013-08-28")

                    bill.add_source("http://example.com")
                    yield bill


You can see that we're adding documents, subjects, a version, and attaching
a sponsor to it. All of these methods are documented on the
:class:`pupa.models.bill.Bill` object. The above is only a subset of the full
list of valid keyword arguments that may be passed into the methods.

Now, let's take a look at how we can add Vote information to a bill::

            from pupa.scrape import Scraper
            from pupa.models import Bill, Vote
            class MyFirstBillScraper(Scraper):
                def get_bills(self):
                    bill = Bill(name="HB 101",
                                session=self.session,
                                title="A bill for an act for pudding",
                                organization=self.jurisdiction.metadata['name'])
                    bill.add_source("http://example.com")

                    v = Vote(organization=self.jurisdiction.metadata['name'],
                             session=self.session,
                             date="2013-04",
                             motion="Pass as amended",
                             type="reading:3",
                             passed=True,
                             yes_count=5,
                             no_count=0,
                             other_count=1,)
                    v.add_source("http://example.com")

                    v.set_bill(bill)  # This will attach the bill in a very
                    # careful way, and properly link the vote to the bill by
                    # it's ID.

                    yield v
                    yield bill

The most interesting thing to note is the use of
:meth:`pupa.models.vote.Vote.add_bill`, which auto-attaches the Bill to it's
``bill`` attribute, correctly handing the cross-linking of IDs. You should
only manually attach a bill if you don't have a ``Bill`` object at ``Vote``
scrape time.

If you're unable to scrape the ``Vote`` at the same time as you're scraping
that particular ``Bill``, you can attempt to match by using the alternate
signature of the ``set_bill`` method::

    v.set_bill("HB 101", chamber="upper")

This call will dispatch based on the type of the first argument. For more
information, check out the :meth:`pupa.models.vote.Vote.add_bill`
documentation.
