
.. _events:

Writing an Events Scraper
===========================

Events scrapers are one of the more compelling datasets that we are able to
collect, since it allows for near real-time updating of upcoming events.

Events scrapers pull down any and all events that are currently listed (or
even historical), with as much metadata as we can find (people attending,
bills up for consideration, etc)

Target Data
-----------

Event scrapers pull down information regarding upcoming (or even past) Events
and associated metadata, such as who was there, what was talked about, and
any supporting material.

Some of the commonly scraped data includes:

* Name of the event
* When the event starts and ends
* Items on the Agenda

   * Related entities (people, orgs, bills)
   * Subject of the agenda item
   * Related media

* Where the event is to take place

   * Lat / lon (if it exists)
   * Venue link

* Associated documents
* Associated people, orgs, participants
* Any video or audio of the event

Creating a new Events scraper
-----------------------------

Let's take a look at a dead-simple Pupa event scraper::

    from pupa.scrape import Scraper
    from pupa.models import Event
    import datetime as dt
    class EventScraper(Scraper):
        def get_events(self):
            when = dt.datetime.now()
            e = Event(name="Hearing",  # Event Name
                      session=self.session,  # Session the Event is in
                      when=when,  # When the event will take place
                      location='unknown')  # Where the event will be
            e.add_source("http://example.com")
            yield e

As you can see, this looks a lot like a person scraper - the same stuff is going
on here - the magic ``scrape_events`` method, which invokes the ``get_events``
method, which should return an iterable of OpenCivic objects. In the case of
the Events scraper, it's not common to come across other OpenCivic objects
during the scrape, so this will usually just return ``Event`` objects.

For more information on the ``scrape_events`` or ``get_events`` methods, you
might consider reading about
:meth:`pupa.scrape.base.Scraper.scrape_events` and
:meth:`pupa.scrape.base.Scraper.get_events` in the Pupa docs.

However, as before, this is wholly underwhelming - this hardcodes events,
and doesn't do much with the ``Event`` object at all.

Let's elaborate a bit on our usage of the ``Event`` object::

    from pupa.scrape import Scraper
    from pupa.models import Event
    import datetime as dt
    class EventScraper(Scraper):
        def get_events(self):
            when = dt.datetime.now()
            e = Event(name="Hearing",
                      session=self.session,
                      when=when,
                      location='unknown')

            e.add_location_url("http://example.com/venue/where")
            e.add_link("http://example.com/event/2013/08/129384/info")

            e.add_document(name='Fiscal Report',
                           url="http://example.com/event/2013/08/129384/docs/report.xls",
                           mimetype="application/vnd.ms-excel")

            e.add_participant(name="John Q. Hacker",
                              type='person',
                              note='attorney')

            e.add_media_link(name="Video of the event",
                             url="http://example.com/video/event.mp4",
                             mimetype='video/mp4')
            e.add_source("http://example.com")
            yield e

OK. Now that we have some basics down, let's take a look at one of the bigger
chunks of any ``Event`` scraper - adding the Agenda items to the ``Event``::

    from pupa.scrape import Scraper
    from pupa.models import Event
    import datetime as dt
    class EventScraper(Scraper):
        def get_events(self):
            when = dt.datetime.now()
            e = Event(name="Hearing",
                      session=self.session,
                      when=when,
                      location='unknown')
            e.add_source("http://example.com")

            item = e.add_agenda_item(description="Joe Smith to Discuss HB 100")
            item.add_bill(bill="HB 100")
            item.add_person(person="Joe Smith")

            yield e

You can see that we've created an ``EventAgendaItem`` object, which we can use
to associate entities (such as ``people`` or ``organizations`` with the agenda
item).

For more information about these objects, feel free to check out
the docs on the :class:`pupa.models.event.Event` and
:class:`pupa.models.event.EventAgendaItem` objects.
