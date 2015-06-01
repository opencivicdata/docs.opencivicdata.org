====================
OCDEP: Disclosures
====================

:Created: 
:Author: Bob Lannon
:Status: Draft

Overview
========

Definition of the ``Disclosure`` type to model officially submitted disclosure
records.

Definitions
-----------

Disclosure
    The act of disclosing information to a DisclosureAuthority.

Rationale
=========

Legislative accountability requires full knowledge of the non-governmental
actors who engage with policymakers, regulatory bodies, and other official
sources. Disclosures should properly identify the parties engaging in disclosed
acts, as well as the officials, bodies of government and non-governmental
organizations contacted.

Implementation
==============

Disclosure
----------

id
    Open Civic Data-style id in the format ``ocd-disclosure/{{uuid}}``

name
    Name of the disclosure

jurisdiction
    The jurisdiction of the disclosure

description
    A brief description of the disclosure

related_entities
    A list of sub-objects that are related to this disclosure

    entity_type
        Type of the related entity, typically a person, organization or event
    
    id
        Open Civic Data ID of the entity.
    
    name 
        Human-readable name of this entity, such as “John Q. Smith”, or “Smith, Jones and Pratt LLP”.

    note
        Optional note regarding the relation between this entity and the disclosure. Choices include:
        * authority
        * registrant
        * disclosed_event

classification
    The classification of the discosure, meant to identify the arena of public
    disclosure to which it applies. Some suggested classifications:
        * lobbying
        * contributions
        * post_employment

submitted_date
    Date (and possibly time) when document was submitted.

effective_date
    Effective date of the registration. (May be retroactive, ie, earlier than submitted date).

sources
    List of sources used in assembling this object.  Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

identifiers
    **optional**
    Upstream ids of the disclosure if any exist, such as the filing ID assigned by the Senate Office of Public Record

created_at
    Time that this object was created at in the system, not to be confused with the date of
    introduction.

updated_at
    Time that this object was last updated in the system, not to be confused with the last action.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.

Disclosure Events
-----------------

Disclosures can describe multiple Open Civic Data ``Event`` objects, as
described in `OCDEP 4: Events <http://opencivicdata.readthedocs.org/en/latest/proposals/0004.html>`_. The distinguishing features are the prescribed field values specified below.

id
    Open Civic Data-style id in the format ``ocd-event/{{uuid}}``

classification
    As defined in the ``Event`` type, where values are extended to include:

    * registration
    * report
    * post_employment

participants
    Participants associated with the event. 

    note
        As defined on the ``Event`` type, where values identifies the role of the participant. Choices include the following, and may be updated:
          * registrant       - the entity responsible for registering with the appropriate disclosure authority and reporting to it
          * client           - (lobbying) an entity on whose behalf the registrant is acting
          * lobbyist         - (lobbying) person who actually did the lobbying
          * lobbied          - (lobbying) organizations and/or individuals that were lobbied
          * regarding        - (lobbying) bills, regulations or other matters that can be identified
          * lobbyist-added   - (lobbying) person added as a lobbyist in a registrant-client relationship
          * lobbyist-removed - (lobbying) person removed as a lobbyist in a registrant-client relationship
          * contributor      - (contributions) the source of the transaction
          * recipient        - (contributions) the target of the contribution
          * lender           - (contributions) the source of a loan
          * borrower         - (contributions) the recipient of a loan
          * creditor         - (contributions) entity to which a debt is owed
          * debtor           - (contributions) entity which owes a debt


Defined Schema
--------------

Schema::

    disclosure_schema = {
        "properties": {
            "classification": {
                "type": ["string", "null"],
                "enum": common.DISCLOSURE_CLASSIFICATIONS,
            },
            "identifiers": identifiers,
            "contact_details": contact_details,
            "related_entities": {
                "items": {
                    "properties": {
                        "entity_type": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "note": {
                            "type": ["string", "null"],
                        },
                    },
                    "type": "object"
                },
                "type": "array"
            },
            "submitted_date": {
                "type": "datetime"
            },
            "effective_date": {
                "type": "datetime"
            },
            "timezone": {
                "type": "string"
            },
            "source_identified": {
                "type": "boolean",
            },
            "documents": documents,
            "sources": sources,
            "extras": extras
        },
        "type": "object"
    }

Examples
--------

Lobbying Disclosure::

     {
      "id": "ocd-disclosure/000225e1-a1e1-43d4-9a73-44ec5955a036",
      "related_entities": [
        {
          "entity_id": "ocd-organization/c5d53b25-12ab-4c96-b7f9-a813cd86d789",
          "note": "authority",
          "entity_name": "Office of Public Record, US Senate",
          "entity_type": "organization",
          "classification": ""
        },
        {
          "entity_id": "ocd-event/a89e59a8-52fd-4ece-a4e3-e02366b57460",
          "note": "disclosed_event",
          "entity_name": "Sidley Austin LLP - New Client for Existing Registrant, Vifor Pharma",
          "entity_type": "event",
          "classification": "registration"
        },
        {
          "entity_id": "ocd-organization/885bc9be-f1e0-4166-b01d-5820d449ad7e",
          "note": "registrant",
          "entity_name": "Sidley Austin LLP",
          "entity_type": "organization",
          "classification": ""
        }
      ],
      "jurisdiction": {
        "id": "ocd-jurisdiction/country:us/government",
        "url": "http://usa.gov/",
        "name": "United States Federal Government"
      },
      "effective_date": "2012-03-01T01:00:00+00:00",
      "updated_at": "2015-04-03T04:31:59.433",
      "created_at": "2015-04-03T04:31:59.433",
      "sources": [
        {
          "note": "LDA Form LD-1",
          "url": "http://soprweb.senate.gov/index.cfm?event=getFilingDetails&filingID=a3f1bf3c-7fa0-4b08-b703-bef451bb3d27&filingTypeID=1"
        }
      ],
      "submitted_date": "2012-04-03T01:00:00+00:00",
      "timezone": "America/New_York",
      "classification": "lobbying"
    }

Disclosed Lobbying Event::

    {
      "updated_at": "2015-04-03T04:31:59.066",
      "id": "ocd-event/a89e59a8-52fd-4ece-a4e3-e02366b57460",
      "description": "",
      "all_day": false,
      "classification": "registration",
      "name": "Sidley Austin LLP - New Client for Existing Registrant, Vifor Pharma",
      "extras": "{}",
      "agenda": [
        {
          "related_entities": [],
          "notes": [
            "Regulation of complex large-molecule drugs by the Food and Drug Administration"
          ],
          "description": "issues lobbied on",
          "subjects": [
            "HCR"
          ],
          "order": "0"
        }
      ],
      "media": [],
      "end_time": null,
      "debug": null,
      "status": "confirmed",
      "links": [],
      "jurisdiction": {
        "id": "ocd-jurisdiction/country:us/government",
        "url": "http://usa.gov/",
        "name": "United States Federal Government"
      },
      "participants": [
        {
          "entity_id": "ocd-organization/885bc9be-f1e0-4166-b01d-5820d449ad7e",
          "note": "registrant",
          "entity_name": "Sidley Austin LLP",
          "entity_type": "organization"
        },
        {
          "entity_id": "ocd-person/94b064c5-660c-47a3-bd67-2c27808e6b80",
          "note": "lobbyist",
          "entity_name": "Patricia DeLoatche",
          "entity_type": "person"
        },
        {
          "entity_id": "ocd-organization/5d0731fb-a275-4b97-b19b-dab89635e234",
          "note": "client",
          "entity_name": "Vifor Pharma",
          "entity_type": "organization"
        },
        {
          "entity_id": "ocd-organization/f4391124-579f-4a84-9b22-98a214ada0c6",
          "note": "foreign_entity",
          "entity_name": "Galenica (Group) Ltd.",
          "entity_type": "organization"
        },
        {
          "entity_id": "ocd-person/c0bf1f0e-0bd3-48ca-8629-c8f9fc470d2c",
          "note": "lobbyist",
          "entity_name": "Peter Goodloe",
          "entity_type": "person"
        }
      ],
      "created_at": "2015-04-03T04:31:59.066",
      "sources": [
        {
          "note": "LDA Form LD-1",
          "url": "http://soprweb.senate.gov/index.cfm?event=getFilingDetails&filingID=a3f1bf3c-7fa0-4b08-b703-bef451bb3d27&filingTypeID=1"
        }
      ],
      "timezone": "America/New_York",
      "documents": [],
      "jurisdiction_id": "ocd-jurisdiction/country:us/government",
      "location": {
        "coordinates": null,
        "url": "",
        "name": "United States"
      },
      "start_time": "2012-03-01T01:00:00+00:00"
    }

