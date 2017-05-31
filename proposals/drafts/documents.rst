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
    A name for the bill, such as 'Communication F2015-119'.

title
    The current title of the bill, such as 'Office of Inspector General's Audit and Program Review Section's Draft 2015 Annual Plan'.

from_organization, from_organization_id
    **optional**
    The organization that the document was originally sent to.  If this is a campaign candidate filing this     
    could be the Board of Elections that receives the filing
    
creators
     An array of creators of the entities
     
    name
        The upstream-given name of this creator.

    entity_type
        'organization' or 'person' - the type of the creator.

    organization, organization_id
        If the ``entity_type`` is 'organization' and the entity is resolved, will be the
        creating organization.

    person, person_id
        If the ``entity_type`` is 'person' and the entity is resolved, will be the
        creating individual.

classification
    A list of classifications for this document, suggested values would be things like 'report',
    'oath of office', 'ethics disclosure', etc.

subject
    **optional**
    A curated list of subject areas that this document covers.

abstracts
    A list of objects representing available abstracts (sometimes called summaries) for the document, each with the
    following fields:

    abstract
        The text of the abstract.

    note
        **optional**
        A note about the origin of the summary, such as "Clerk Staff Summary"

other_titles
    A list of objects representing alternate titles for the document.

    title
        The text of an alternate title that someone might use to refer to the document.

    note
        **optional**
        A note describing the origin of the title.

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

related_documents
    List of all related documents. An example might be a an amended campaign finance document that supersedes an earlier filing. 

    An array of entities with the following fields:

    identifier
        The identifier of the related documents, such as "D-1 Statement of Organization".
    relation_type
        Description of the relation between the two bills, can be:

        * replaced-by - A document that was replaced by another document.
        * replaces - A document that supercedes another document.

    related_document_id
        If the related document exists in the data set, a link to the complete record for the document. (can be null if no such link has yet been made)

links
    Links to ‘available forms’ of the document. Each document can be available in multiple forms such as PDF and HTML. (For those familiar with DCAT this is the same as the Distribution class.) Has the following properties:

    url
        URL of the link.
    media_type
        The media type of the link.
    full_text
         If available, the full text of the document in text based format

actions
    A list of objects representing individual actions that take place on a actions, such as submissions and publications. Actions consist of the following properties:
    
    organization, organization_id
        The organization that this action took place within.

    description
        Description of the action.

    date
        The date the action occurred in YYYY-MM-DD format. (can be partial by omitting -MM-DD or
        -DD component).

    classification
        A list of classifications for this actions, suggested values would be things like
        'submission', 'publication', etc.

    related_entities
        A list of all related entities (such as legislators mentioned by name in the action).
        Each entity has the following fields:

        name
            The upstream-given name of this related entity.

        entity_type
            'organization' or 'person' - the type of entity that is related

        organization, organization_id
            If the ``entity_type`` is 'organization' and the entity is resolved, will be the
            organization that is related.

        person, person_id
            If the ``entity_type`` is 'person' and the entity is resolved, will be the
            person that is related.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.
    

    

Copyright
=========

This document has been placed in the public domain per the Creative Commons
CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).

