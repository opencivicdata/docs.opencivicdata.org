
.. _events:

Contributing a Municipal Events Scraper
=======================================

Events scrapers are one of the more compelling datasets that we are able to
collect, since it allows for near real-time updating of upcoming events.

Events scrapers pull down any and all events that are currently listed (or
even historical), with as much metadata as we can find (people attending,
bills up for consideration, etc)

Creating a new Events scraper
-----------------------------

Let's take a look at a dead-simple Pupa event scraper::

    from pupa.scrape import Scraper
    from pupa.models import Event
    import datetime as dt
    class MyFirstEventScraper(Scraper):
        def get_events(self):
            when = dt.datetime.now()
            e = Event(name="Hearing",
                      session=self.session,
                      when=when,
                      location='unknown')
            e.add_source("http://example.com")
            yield e

As you can see, this looks a lot like a person scraper - the same stuff is going
on here - the magic ``scrape_events`` method, which invokes the ``get_events``
method, which should return an iterable of events.

However, as before, this is wholly underwhelming - this hardcodes events,
and doesn't do much with the ``Event`` object at all.

Let's elaborate a bit on our usage of the ``Event`` object::

    from pupa.scrape import Scraper
    from pupa.models import Event
    import datetime as dt
    class MyFirstEventScraper(Scraper):
        def get_events(self):
            when = dt.datetime.now()
            e = Event(name="Hearing",
                      session=self.session,
                      when=when,
                      location='unknown')
            e.add_media_link(name="Video of the event",
                             url="http://example.com/video/event.mp4",
                             mimetype='video/mp4')
            e.add_source("http://example.com")
            yield e

Or, a look at how to use the agenda object::

    from pupa.scrape import Scraper
    from pupa.models import Event
    import datetime as dt
    class MyFirstEventScraper(Scraper):
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

For more information about these objects, feel free to check out
the docs on the :class:`pupa.models.event.Event` and
:class:`pupa.models.event.EventAgendaItem` objects.
