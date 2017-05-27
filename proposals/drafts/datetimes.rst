=========================================
OCDEP: Standardize Usage of Dates & Times
=========================================

:Created: 2017-05-26
:Author: James Turk
:Status: Proposed

Overview
========

There are currently three ways we handle dates & times throughout Open Civic Data.  This proposal aims to evaluate them and make several changes that will increase consistency & serve as guidance for future decisions.

Rationale
=========

The current situation:

"Fuzzy Date Field"
    This is implemented as a char field allowing up to 10 characters.  Dates are expected to conform to the YYYY[-MM[-DD]] format.

This comes from Popolo, and allows dates to be specified with varying degrees of accuracy depending on what is known.  (e.g. sometimes we only know a person's birth year, or the month something came into being)

The field is used in the following places:

* BillAbstract.date
* BillAction.date
* BillDocument.date
* BillVersion.date
* EventDocument.date
* EventMedia.date         (via EventMediaBase)
* EventAgendaMedia.date   (via EventMediaBase)
* LegislativeSession.{start_date,end_date}
* Membership.{start_date,end_date}
* Organization.{founding_date,dissolution_date}
* OrganizationName.{start_date,end_date}      (via OtherNameBase)
* Person.{birth_date,death_date}
* PersonName.{start_date,end_date}            (via OtherNameBase)
* Post.{start_date,end_date}

"Fuzzy Datetime Field"

    For VoteEvents sometimes the time is important too, so we extended the aove field to 19 characters, allowing an additional inclusion of time in HH:MM:SS.

This field is used only in

* VoteEvent.{start_date,end_date}

Finally, we sometimes use native DateTime fields.

Notably this is used for every model's created_at/updated_at timestamp.

It is also used for 

* Event.{start_time,end_time}

This has the advantage of being timezone-aware.

Issues with current approach
----------------------------

For the most part this is OK, and we're fairly consistent.  Most uses of fuzzy date align with the goals, but in a few cases it seems like we've made some mistakes:

VoteEvent's special case of fuzzy time is a problem in two ways:

1) it can have a time but lacks a timezone
2) it is misnamed, ending in _date while allowing a time to be stored

And three other issues:

3) We need the ability to set times on BillAction.date, just like VoteEvent.  We are frequently forced to truncate times.
4) The VoteEvent/Event mismatch between real DateTimeField and "fuzzy date time field" seems likely to trip people up.
5) The extended format is almost ISO8601 datetime, but uses a space instead of a 'T' as the separator of date & time.

Implementation
===============

1) To address #1 and #5: add timezone to "fuzzy datetime" and bring the full format in line w/ ISO8601, changing the format from:
        YYYY[[[-MM]-DD] HH:MM:SS]
            to 
        YYYY[[[-MM]-DD]THH:MM:SS(Z|+XX:YY)]

Also considered:

* Convert it to a full datetime, but this would require a time on
  every vote.  We might not have one.
* Define that time is always stored in UTC, but this would be more
  error prone than being explicit.

2) To address #2, rename VoteEvent.start_date,end_date to start_time,end_time to match Event and be more clear.

Also considered:

* Leaving this be, but I think we should take this opportunity to fix as many time related issues as we can and this is a definite mistake in naming.

3) To address #3, extend BillAction.date to match "fuzzy datetime" rules and rename it to BillAction.time

* It could also become a full datetime (see #1), but would mostly have to fake the time.
* The name of the field isn't great this way either, other options?

4) To address #4, I propose we have Event adopt the fuzzy datetime.  This would make it consistent w/ VoteEvent and BillAction if the other proposals are adopted.


Copyright
=========

This document has been placed in the public domain per the Creative Commons
CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).
