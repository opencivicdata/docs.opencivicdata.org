
.. _events:

Writing an Events Scraper
===========================

.. warning::
    Parts of Open Civic Data underwent a large refactor as of mid-2014, some information on this
    page may be out of date.   We're working on updating this documentation as soon as possible.

    We'll remove these messages from pages as they're updated and vetted.


Events listings are one of the more compelling datasets that we are able to collect, since it allows for near real-time updating of upcoming events. Events include hearings, meetings, or bascially anything with a date and time listed by the organization you're scraping.

Target Data
-----------

Event scrapers pull down information regarding upcoming (or past) Events and associated metadata, such as who was there, what was talked about, and any supporting material.

Some of the commonly scraped data includes:

* Name of the event
* When the event starts and ends
* Items on the Agenda

   * Related entities (people, orgs, bills)
   * Subject of the agenda item
   * Related media

* Where the event is to take place

   * Lat / lon (if it exists)
   * Description of location (such address or building)
   * Venue link

* Associated documents
* Associated people, orgs, participants
* Any video or audio of the event

Creating a new Events scraper
-----------------------------

Let's take a look at a sample Pupa event scraper::

  from pupa.scrape import Scraper
  from pupa.scrape import Event
  import datetime as dt
  import pytz

  class SeattleEventScraper(Scraper):
      def scrape(self):
          when = dt.datetime(1776,7,4,9,15)
          tz = pytz.timezone("US/Pacific") #set the timezone for this location
          when = tz.localize(when)
          e = Event(name="Hearing",  # Event Name
                        start_time=when,  # When the event will take place
                        timezone=tz.zone, #the local timezone for the event
                        location='unknown')  # Where the event will be
          e.add_source("http://example.com")
          yield e

The events scraper looks a lot like a person scraper - the same stuff is going on here - the magic ``scrape`` method, returns an iterable of OpenCivic objects. Unlike people, where we often found committees or other organizations, it's not common to come across other OpenCivic objects while scraping events, so this scraper will usually just return ``Event`` objects.

The scraper above contains the minimum elements required to create an event. But there's much more we might want to add. The following scraper adds particpants and documents that are relevant to the hearing::

  from pupa.scrape import Scraper
  from pupa.scrape import Event
  import datetime as dt
  import pytz

  class SeattleEventScraper(Scraper):
      def scrape(self):
          when = dt.datetime(1776,7,4,9,15)
          tz = pytz.timezone("US/Pacific") #set the timezone for this location
          when = tz.localize(when)
          e = Event(name="Hearing",  # Event Name
                        start_time=when,  # When the event will take place
                        timezone=tz.zone, #the local timezone for the event
                        location='unknown')  # Where the event will be
          e.add_source("http://example.com")

          #add a committee
          e.add_participant(name="Transportation Committee",
                          type="committee")

          #add a person
          e.add_person(name="Joe Smith", note="Hearing Chair")

          #add an mpeg video
          e.add_media_link(note="Video of meeting",
                          url="http://example.com/hearing/video.mpg",
                          media_type="video/mpeg")

          #add a pdf of meeting minutes
          e.add_media_link(note="Meeting minutes",
                          url="http://example.com/hearing/minutes.pdf",
                          media_type="application/pdf")

          yield e


The event is now much more fleshed out. But we're still missing the meat of an event: the agenda! Next we'll add agenda items::

  from pupa.scrape import Scraper
  from pupa.scrape import Event
  import datetime as dt
  import pytz

  class BelmontmaEventScraper(Scraper):
      def scrape(self):
          when = dt.datetime(1776,7,4,9,15)
          tz = pytz.timezone("US/Pacific") #set the timezone for this location
          when = tz.localize(when)
          e = Event(name="Hearing",  # Event Name
                        start_time=when,  # When the event will take place
                        timezone=tz.zone, #the local timezone for the event
                        location='unknown')  # Where the event will be
          e.add_source("http://example.com")

          #add a committee
          e.add_participant(name="Transportation Committee",
                          type="committee")

          #add a person
          e.add_person(name="Joe Smith", note="Hearing Chair")

          #add an mpeg video
          e.add_media_link(note="Video of meeting",
                          url="http://example.com/hearing/video.mpg",
                          media_type="video/mpeg")

          #add a pdf of meeting minutes
          e.add_media_link(note="Meeting minutes",
                          url="http://example.com/hearing/minutes.pdf",
                          media_type="application/pdf")


          #add an agenda item to this event
          a = e.add_agenda_item(description="Testimony from concerned citizens")

          #the testimony is about transportation and the environment
          a.add_subject("Transportation")
          a.add_subject("Environment")

          #and includes these two committees
          a.add_committee("Transportation")
          a.add_committee("Environment and Natural Resources")

          #these people will be present
          a.add_person("Jane Brown")
          a.add_person("Alicia Jones")
          a.add_person("Fred Green")

          #they'll be discussing this bill
          a.add_bill("HB101")

          #here's a document that is included
          a.add_media_link(note="Written version of testimony",
                          url="http://example.com/hearing/testimony.pdf",
                          media_type="application/pdf")

          yield e

This example shows how to use the events model exhaustively. However, we haven't done any actual web-scraping. All of the details we added are hard-coded. It is quite difficult to show an example of a functioning web-scraper for an events page, as we have found that legislative events pages or calendars tend to change formats somewhat frequently. For an example of a scraper that hits an actual webpage to find information, see :doc:`/scrape/people`.