================
OCDEP: Documents
================

:Created: 
:Author: Forest Gregg
:Status: Draft

Overview
========

Legislatures produce many documents that are not legislation, but still interesting. These include 

- reports
- communications
- oaths of offices
- orders
- claims

Outside of legislatures, ethics filings, campaign candidate filings, and campaign finance disclosures are all types of documents which we should be able to represent within Open Civic Data.

Pupa should provide a Document class, based on the current Bill type to record and store these documents. The Document class may either be used directly or be subclasssed for specific types of documents like Disclosures.

Implementation
==============

id
    A unique ID in the format ``ocd-document/{uuid}``.

identifier
    A name for the bill, such as 'HB 1' or '2117'.

title
    The current title of the bill, such as 'The Patient Protection and Affordable Care Act'.

from_organization, from_organization_id
    **optional**
    The organization that the document was originally introduced in.  If this is a campaign candidate filing this     
    could be the Board of Elections that receives the filing

classification
    A list of classifications for this document, suggested values would be things like 'report',
    'oath of office', 'ethics disclosure', etc.

subject
    **optional**
    A curated list of subject areas that this bill is a part of.

abstracts
    A list of objects representing available abstracts (sometimes called summaries) for the document, each with the
    following fields:

    abstract
        The text of the abstract.

    note
        **optional**
        A note about the origin of the summary, such as "Republican Caucus Summary" or "Library of Congress Summary"

other_titles
    A list of objects representing alternate titles for the document.

    title
        The text of an alternate title that someone might use to refer to the document.

    note
        **optional**
        A note describing the origin of the title.

other_identifiers
    A list of objects representing alternate identifiers for the bill.

    Also note that this is to refer to bills that have multiple names, such as in Tennessee where
    bills are given a House and Senate number but have shared history.  In states where there
    are two related bills with distinct parallel histories, a second Bill object should be
    created and the ``related_bill`` property (described below) should be used.

    identifier
        The alternate identifier (e.g. HB 7)

    note
        **optional**
        A note describing the reason for the alternate name.

    scheme
        **optional**
        If the identifier belongs to a 3rd-party site (such as OpenStates.org assigned bill ids)
        it must provide a scheme, scheme should be omitted if it is an identifier from the
        primary source.


versions
    All versions of the document.

    note
        Note describing the version 
    date
        The date the version was published in YYYY-MM-DD format (partial dates are acceptable).
    links
        Links to 'available forms' of the version.  Each version can be available in
        multiple forms such as PDF and HTML.  (For those familiar with DCAT this is the same
        as the ``Distribution`` class.)
        Has the following properties:

        url
            URL of the link.
        media_type
            The `media type <http://en.wikipedia.org/wiki/Internet_media_type>`_ of the link.
            
    text
        Full text of the document 



created_at
    Time that this object was created at in the system, not to be confused with the date of
    introduction.

updated_at
    Time that this object was last updated in the system, not to be confused with the last action.

sources
    List of sources used in assembling this object.  Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.

Copyright
=========

This document has been placed in the public domain per the Creative Commons
CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).


Additional fields: 

- effective dates
- submitted dates 
- signatures
- creator
- published dates
