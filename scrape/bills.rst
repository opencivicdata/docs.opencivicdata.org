
.. _bills:

Writing a Bill Scraper
=======================

Bill scrapers are scrapers that pull down all legislatition on a jurisdiction's legislative website (including, but not limited to things like House and Senate Resolutions, Bills or city ordinances).

Scrapers should scrape all bills from a session every single night.

Target Data
-----------

Bill scrapers are used to pull in information regarding Legislation, and basic associated metadata.

Bill scrapers should collect all the information it's able to. The most common bits of data are:

  * Basic information (name, session, chamber, summary)
  * Sponsorship information (primary, secondary, etc)
  * Actions regarding the legislation (introduction date, committee referral,
    chamber crossover, etc)
  * Alternate names of the Legislation
  * Related documents (fiscal reports, supporting data)
  * Bill versions (Introduced Version, as amended)
  * Related bills (companion bills, reintroductions)
  * Subjects (Technology, Transportation, Education)

.. NOTE::

    In addition to the data above, it's common for Bill scrapers to also scrape
    in Vote information as well, since it's often linked directly from the Vote
    page.

Overview
--------


Bills are certainly the most complicated and varied thing we'll be scraping as part of this project. For starters, bills are the only object that needs to be attached to a legislative session. A legislative session the period during which actions can happen to a bill. After the end of a session, bills that have not been passed would need to be re-introduced. For example, the US Congress has 2-year sessions that start at the beginning of odd years. Sessions sometimes have numbers (the US congressional session starting in 2015 is the 114th session). Note that sessions are not necessarily the same thing as terms. In the US House, a Rep's term is 2 years long and coincides with the bounds of a session, but Senators' terms are 6 years long, so span multiple sessions. In some jurisdictions, members can be elected mid-session.

For municipal governments, it can be somewhat difficult to find information about legislative sessions. We recommend contacting the city or town clerk's office, or the press office for larger cities.

When you've figured out the beginning and end dates for the most recent session, add it to :file:`__init__.py`:. The variable legislative_sessions needs to be a list of dictionaries with at least an identifier, a name, a start_date and an end_date. The identifier should be a unique description of the session (so the 2015 regular session of a legislature might have an identifier of 2015), the name should be a human-readable string, and the dates should be in format YYYY-MM-DD. For example::

    legislative_sessions = [{"identifier":"2015",
                "name":"2015 Regular Session",
                "start_date": "2015-01-01",
                "end_date": "2016-12-31"}]

Now that we've got at least one session in :file:`__init__.py`, let's start out with a simple scraper::

    from pupa.scrape import Scraper
    from pupa.scrape import Bill


    class SeattleBillScraper(Scraper):

        def scrape(self):
            session = self.jurisdiction.legislative_sessions[0]
            bill = Bill(identifier="R101",
                    legislative_session=session["identifier"],
                    title="More cookies for children",
                    classification="resolution")
            bill.add_source("http://example.com")
            yield bill

Only identifier, legislative_session and title are required. Classification will default to "bill" if none is given. Classification may be any of the following:

    * bill
    * resolution
    * concurrent resolution
    * joint resolution
    * memorial
    * commemoration
    * concurrent memorial
    * joint memorial
    * proposed bill
    * proclamation
    * nomination
    * contract
    * claim
    * appointment,
    * constitutional amendment
    * petition
    * order
    * concurrent order
    * appropriation
    * ordinance

For a bicameral legislature, the chamber should also be included in the bill initialization (as 'upper' or 'lower').

We can add a variety of other pieces of information to a bill. All are optional and bills will successfully import without any of these extras, but please note that internal quality checks may be triggered by bills with no versions or actions as those ought to exist for every available bill. The scraper below gives examples of all additional pieces of data that can be added::

    from pupa.scrape import Scraper
    from pupa.scrape import Bill


    class SeattleBillScraper(Scraper):

        def scrape(self):
            session = self.jurisdiction.legislative_sessions[0]
            bill = Bill(identifier="R101",
                    legislative_session=session["identifier"],
                    title="More cookies for children",
                    classification="resolution")
            bill.add_source("http://example.com")
            
            #add a sponsor
            bill.add_sponsorship(name="Joe Smith", #name of person or org
                    classification="Primary", #primary? secondary? first? co-sponsor? etc
                    entity_type="person", #person or organization
                    primary=True #boolean, T if primary, F otherwise
                    )

            #add subject(s)
            bill.add_subject("Nutrition")
            bill.add_subject("Youth")

            #add abstract or summary
            bill.add_abstract(abstract="Provides every child with a cookie",
                            note="Abstract for introduced version")


            #add other title(s) the bill may have gone by
            #perhaps a former title or a subtitle?
            bill.add_title("Om nom nom cookies")

            #add other ID(s) the bill has previously had
            #this can be useful for bills that are
            #renamed or substituted or have an omnibus relationship
            bill.add_identifier("R095")

            #add versions of the bill text
            bill.add_version_link(note="Introduced",
                                url="http://example.com/R101.pdf",
                                date="2015-05-05", #optional, YYYY-MM-DD
                                media_type="application/pdf" #optional but useful!
                                )

            #add other documents (not versions)
            #such as fiscal analysis, committee report,
            #testimony, etc
            bill.add_document_link(note="Fiscal Note",
                                url="http://example.com/R101/FiscalNote.pdf",
                                date="2015-05-05", #optional, YYYY-MM-DD
                                media_type="application/pdf" #optional but useful!
                                )

            #add related bill, useful for bills that were replaced,
            #substituted, in an omnibus relationship, continued
            #from a previous session, etc.
            bill.add_related_bill(identifier="R105",
                                legislative_session=session["identifier"],
                                relation_type="companion" #companion, prior-session,
                                                    #replaced-by, replaces
                                )


            #add actions. an action can also take a chamber
            #('upper' or 'lower') if this is a bicameral legislature
            act = bill.add_action(description="Bill Introduced",
                            date="2015-05-05",
                            classification="introduction", #see note about allowed classifications
                            )
            
            #add entities to the action. This is how you'd add
            #committees or people who participated
            act.add_related_entity(name="Transportation Committee",
                                    entity_type="organization")

            yield bill



Bill actions should be one of the following:
    * filing
    * introduction
    * reading-1
    * reading-2
    * reading-3
    * passage
    * failure
    * withdrawal
    * substitution
    * amendment-introduction
    * amendment-passage
    * amendment-withdrawal
    * amendment-failure
    * amendment-amended
    * committee-referral
    * committee-passage
    * committee-passage-favorable
    * committee-passage-unfavorable
    * committee-failure
    * executive-received
    * executive-signature
    * executive-veto
    * executive-veto-line-item
    * veto-override-passage
    * veto-override-failure

Note that when we actually scrape the site, we'd like to limit the bills we ingest to the current legislative session. Depending on the site, this can be done by navigating to a page that only contains information from the current session, or by limiting a search by the date range related to a session.

Scraping Votes
------------------


In almost every case, votes are found on the same page as bills, so we tend to scrape them from the bill scraper. Below is an example (we've removed all but the required features of a bill to keep things shorter.)

Now, let's take a look at how we can add Vote information to a bill::

    from pupa.scrape import Scraper
    from pupa.scrape import Bill, Vote


    class SeattleBillScraper(Scraper):

        def scrape(self):
            session = self.jurisdiction.legislative_sessions[0]
            bill = Bill(identifier="R101",
                    legislative_session=session["identifier"],
                    title="More cookies for children",
                    classification="resolution")
            bill.add_source("http://example.com")
            
            #create a vote
            v = Vote(legislative_session=session["identifier"],
                        motion_text = 'Shall the bill pass the first reading?',
                        start_date = '2015-05-06', #date of the vote
                        classification = 'bill-passage', #or 'amendment-passage' or 'veto-override'
                        result = 'pass', #or 'fail'
                        bill = bill
                        )

            #we'll add the legislators' votes below.
            #note that sometimes only the counts are available,
            #not how individuals vote. So skip to the counts if
            #that's the case.

            #add yes and no votes
            v.yes("John Smith")
            v.no("Susan Jones")
            v.yes("Jessica Brown")

            #add votes with other classifications
            #option can be 'yes', 'no', 'absent',
            #'abstain', 'not voting', 'paired', 'excused'
            v.vote(option="absent",
                    voter="Angela Cruz")


            #when possible it is best to set the vote
            #counts separately from the way individuals voted
            #this is important because vote documents can often
            #be the hardest thing to parse and the most liekly to contain errors
            #so if we can get good, reliable data on the vote count,
            #we should use it.
            v.set_count(option="yes", value=2)
            v.set_count(option="no", value=1)
            v.set_count(option="absent", value=1)

            v.add_source("https://example.com/R101/votes")

            yield bill
            yield v


If you're unable to scrape the ``Vote`` at the same time as you're scraping that particular ``Bill``, you can attempt to match by using the alternate signature of the ``set_bill`` method::

    v.set_bill("R101", chamber="upper")

This call will dispatch based on the type of the first argument. For more information, check out the :meth:`pupa.models.vote.Vote.set_bill` documentation.
