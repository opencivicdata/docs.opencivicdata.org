====================
OCDEP: Disclosures
====================

:Created: 
:Author: Bob Lannon
:Status: Draft

Overview
========

Definition of the ``Disclosure`` type and the ``ReportingPeriod`` type, top-level types that model officially submitted disclosure records. In addition, a subtype of ``Organization`` called ``DisclosureAuthority`` and a subtype of ``Event`` called ``DisclosureEvent``.

Definitions
-----------

Disclosure
    The act of disclosing information to a DisclosureAuthority.

ReportingPeriod
    The duration of time that a disclosure refers to.

DisclosureAuthority
    The authority to which disclosures must be submitted.

DisclosedEvent
    The actual event being disclosed. Rather than employ a taxonomy of event types, events can be identified with one another to the extent that they share participant types and participant roles. Participant roles are expressed through the "note" field. A sufficiently expressive list of roles should allow full coverage of multiple disclosure authorities and jurisdictions without sacrificing comparability.

Rationale
=========

Legislative accountability requires full knowledge of the non-governmental actors who engage with policymakers, regulatory bodies, and other official sources. Disclosures should properly identify the parties engaging in disclosed acts, as well as the officials, bodies of government and non-governmental organizations contacted.

Implementation
==============

DisclosureAuthority
-------------------
The basis for the DisclosureAuthority is the Open Civic Data ``Organization`` type, as described in `OCDEP 5: People, Organizations, Posts, and Memberships <http://opencivicdata.readthedocs.org/en/latest/proposals/0005.html>`_.

ReportingPeriod
---------------
id
    Open Civic Data-style id in the format ``ocd-disclosure/{{uuid}}``

description
    Description of the reporting period

authorities
    A list of ``DisclosureAuthority`` entities that define the reporting period

period_type
    The duration of the period. Choices are:

    * daily         - reports due on a daily basis
    * weekly        - reports due on a weekly basis
    * monthly       - reports due on a monthly basis
    * quarterly     - reports due on a quarterly basis
    * semi-annually - reports due twice a year
    * annually      - reports due once per year
    * cycle         - reports due once per election cycle
    * defined       - reports due as specially defined by statute or by the authority

start_date
    Start date of the reporting period

end_date
    End date of the reporting period

Disclosure
----------

id
    Open Civic Data-style id in the format ``ocd-disclosure/{{uuid}}``

registrant, registrant_id
    The organization or individual who is registering.

authority, authority_id
    The organization that the registration is due to.

reporting_period, reporting_period_id
    The reporting period to which this registration was submitted.

related_entities
    A list of sub-objects that are related to this disclosure

    entity_type
        Type of the related entity, such as bill, person, or organization.
    
    id
        Open Civic Data ID of the entity.
    
    name
        Human-readable name of this entity, such as “John Q. Smith”, or “Smith, Jones and Pratt LLP”.
    note
        Optional note regarding the relation between this entity and the disclosure. Choices include:
        * client
        * beneficiary
        * foreign-entity
        * affiliate
        * lobbyist

disclosed_events
    A list of events disclosed. See ``DisclosedEvent`` object below.

identifiers
    **optional**
    Upstream ids of the disclosure if any exist, such as the filing ID assigned by the Senate Office of Public Record

submitted_date
    **optional**
    Date (and possibly time) when document was submitted.

effective_date
    **optional**
    Effective date of the registration. (May be retroactive, ie, earlier than submitted date).

created_at
    Time that this object was created at in the system, not to be confused with the date of
    introduction.

updated_at
    Time that this object was last updated in the system, not to be confused with the last action.

documents
    All documents related to the disclosure with the exception of versions (which are part of
    the above ``versions``).

    note
        Note describing the document's relation to the disclosure (e.g. 'submitted filing', 'request for additional information', etc.)
    date
        The date the document was published in YYYY-MM-DD format
        (partial dates are acceptable).
    links
        Links to 'available forms' of the document.  Each document can be available in
        multiple forms such as PDF and HTML.  (For those familiar with DCAT this is the same
        as the ``Distribution`` class.)
        Has the following properties:

        url
            URL of the link.
        media_type
            The `media type <http://en.wikipedia.org/wiki/Internet_media_type>`_ of the link.

sources
    List of sources used in assembling this object.  Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.

DisclosedEvent
--------------
The basis for the DisclosedEvent is the Open Civic Data ``Event`` type, as described in `OCDEP 4: Events <http://opencivicdata.readthedocs.org/en/latest/proposals/0004.html>`_. The distinguishing features are the prescribed field values specified below.

id
    Open Civic Data-style id in the format ``ocd-event/{{uuid}}``

classification
    As defined in the ``Event`` type, where values are extended to include:

    * lobbying
    * contribution

participants
    Participants associated with the event. 

    note
        As defined on the ``Event`` type, where values identifies the role of the participant. Choices include the following, and may be updated:
          * lobbyist         - (lobbying) person who actually did the lobbying
          * lobbied          - (lobbying) organizations and/or individuals that were lobbied
          * regarding        - (lobbying) bills, regulations or other matters that can be identified
          * contributor      - (contributions) the source of the transaction
          * recipient        - (contributions) the target of the contribution
          * lender           - (contributions) the source of a loan
          * borrower         - (contributions) the recipient of a loan
          * creditor         - (contributions) entity to which a debt is owed
          * debtor           - (contributions) entity which owes a debt
          * lobbyist-added   - (lobbying) person added as a lobbyist in a registrant-client relationship
          * lobbyist-removed - (lobbying) person removed as a lobbyist in a registrant-client relationship


Defined Schema
--------------

Schema::

    disclosure_actions = ["registration", "report"]

    disclosure_classifications = ["lobbying", "contributions"]

    disclosure_participant_roles = ["lobbyist",
                                    "lobbied",
                                    "regarding",
                                    "contributor",
                                    "recipient",
                                    "lender",
                                    "borrower",
                                    "creditor",
                                    "debtor"]

    disclosed_event_schema = {
        "properties": {
            "id": {
                "type": "string"
            },
            "classification": {
                "type": "string",
                "enum": disclosure_actions
            },
            "name": {
                "type": "string"
            },
            "start_time": {
                "type": "datetime"
            },
            "timezone": {
                "type": "string"
            },
            "all_day": {
                "type": "boolean"
            },
            "end_time": {
                "type": ["datetime", "null"]
            },
            "status": {
                "type": "string",
                "blank": True,
                "enum": ["cancelled", "tentative", "confirmed", "passed"],
            },
            "description": {
                "type": "string",
                "blank": True
            },
            "location": {
                "type": "object",
                "properties": {

                    "name": {
                        "type": "string"
                    },

                    "note": {
                        "type": "string",
                        "blank": True
                    },

                    "url": {
                        "required": False,
                        "type": "string",
                    },

                    "coordinates": {
                        "type": ["object", "null"],
                        "properties": {
                            "latitude": {
                                "type": "string",
                            },

                            "longitude": {
                                "type": "string",
                            }
                        }
                    },
                },
            },

            "media": media_schema,

            "documents": {
                "items": {
                    "properties": {
                        "note": {
                            "type": "string"
                        },
                        "url": {
                            "type": "string"
                        },
                        "media_type": {
                            "type": "string"
                        },
                    },
                    "type": "object"
                },
                "type": "array"
            },

            "links": {
                "items": {
                    "properties": {

                        "note": {
                            "type": "string",
                            "blank": True
                        },

                        "url": {
                            "format": "uri",
                            "type": "string"
                        }
                    },
                    "type": "object"
                },
                "type": "array"
            },

            "participants": {
                "items": {
                    "properties": {

                        "name": {
                            "type": "string",
                        },

                        "id": {
                            "type": ["string", "null"]
                        },

                        "type": {
                            "enum": ["organization", "person"],
                            "type": "string"
                        },

                        "note": {
                            "type": "string",
                            "enum": disclosure_participant_roles
                        },

                    },
                    "type": "object"
                },
                "type": "array"
            },

            "agenda": {
                "items": {
                    "properties": {
                        "description": {
                            "type": "string"
                        },

                        "order": {
                            "type": ["string", "null"]
                        },

                        "subjects": {
                            "items": {"type": "string"},
                            "type": "array"
                        },

                        "media": media_schema,

                        "notes": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array",
                            "minItems": 0
                        },

                        "related_entities": {
                            "items": {
                                "properties": {
                                    "entity_type": {
                                        "type": "string"
                                    },

                                    "id": {
                                        "type": ["string", "null"]
                                    },

                                    "name": {
                                        "type": "string"
                                    },

                                    "note": {
                                        "type": ["string", "null"]
                                    },
                                },
                                "type": "object"
                            },
                            "minItems": 0,
                            "type": "array"
                        },
                    },
                    "type": "object"
                },
                "minItems": 0,
                "type": "array"
            },
            "sources": sources,
            "extras": extras
        },
        "type": "object"
    }

    disclosure_related_entity_roles = ["client",
                                       "beneficiary",
                                       "foreign-entity",
                                       "affiliate"]

    disclosure_schema = {
        "properties": {
            "id": {
                "type": "string"
            },
            "registrant": {
                "type": "string"
            },
            "registrant_id": {
                "type": "string"
            },
            "authority": {
                "type": "string"
            },
            "authority_id": {
                "type": "string"
            },
            "reporting_period": {
                "type": "string"
            },
            "reporting_period_id": {
                "type": "string"
            },
            "related_entities": {
                "items": {
                    "properties": {
                        "entity_type": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "note": {
                            "type": "string",
                            "enum": disclosure_related_entity_roles,
                        },
                    },
                    "type": "object"
                },
                "type": "array"
            },
            "disclosed_events": {
                "items": disclosed_event_schema,
                "type": "array"
            },
            "official_id": {
                "type": "string"
            },
            "submitted_date": {
                "type": fuzzy_date_blank
            },
            "effective_date": {
                "type": fuzzy_date_blank
            },
            "created_at": {
                "type": "datetime"
            },
            "updated_at": {
                "type": "datetime"
            },
            "documents": {
                "items": {
                    "properties": {
                        "note": {
                            "type": "string"
                        },
                        "url": {
                            "type": "string"
                        },
                        "media_type": {
                            "type": "string"
                        },
                    },
                    "type": "object"
                },
                "type": "array"
            },
            "sources": sources,
            "extras": extras
        },
        "type": "object"
    }

Examples
--------


Lobbying Registration Example::

    # DisclosureAuthorities
    sopr = {
      "id": "ocd-organization/d006f8f6-a35a-11e4-9771-bb010e0210e2",
      "name": "Senate Office of Public Record",
      "other_names": [],
      "identifiers": [],
      "classification": "office",
      "jurisdiction": "us/government",
      "jurisdiction_id": "",
      "parent_id": "{{senate's ID}}",
      "founding_date": "",
      "dissolution_date": "",
      "image": "",
      "contact_details": [
        {
          "type": "voice",
          "label": "",
          "value": "202-224-0322",
          "note": ""
        }
      ],
      "links": [
        {
            "url": "http://www.senate.gov/pagelayout/legislative/one_item_and_teasers/opr.htm",
            "note": "Profile page"
        },
        {
            "url": "http://www.senate.gov/pagelayout/legislative/g_three_sections_with_teasers/lobbyingdisc.htm#lobbyingdisc=lda",
            "note": "Disclosure Home"
        },
        {
            "url": "http://soprweb.senate.gov/index.cfm?event=selectfields",
            "note": "Disclosure Search Portal"
        },
        {
            "url": "http://soprweb.senate.gov/",
            "note": "Disclosure Electronic Filing System"
        }
      ]
    }

    house_clerk = {
      "id": "ocd-organization/1aa0689a-a55c-11e4-9771-bb010e0210e2",
      "name": "Office of the Clerk of the U.S. House of Representatives",
      "other_names": [],
      "identifiers": [],
      "classification": "office",
      "jurisdiction": "us/government",
      "jurisdiction_id": "",
      "parent_id": "{{senate's ID}}",
      "founding_date": "",
      "dissolution_date": "",
      "image": "",
      "contact_details": [
        {
          "type": "address",
          "label": "contact address",
          "value": "U.S. Capitol, Room H154, Washington, DC 20515-6601",
          "note": ""
        },
        {
            "type": "email",
            "label": "general inquiries",
            "value": "info.clerkweb@mail.house.gov",
            "note": ""
        },
        {
            "type": "email",
            "label": "general technical support",
            "value": "techsupport.clerkweb@mail.house.gov",
            "note": ""
        },
        {
            "type": "email",
            "label": "HouseLive support",
            "value": "houselive@mail.house.gov",
            "note": ""
        }
      ],
      "links": [
        {
            "url": "http://lobbyingdisclosure.house.gov/",
            "note": "Lobbying Disclosure"
        },
        {
            "url": "http://clerk.house.gov/",
            "note": "Home"
        },
        {
            "url": "http://disclosures.house.gov/ld/ldsearch.aspx",
            "note": "Lobbying Disclosure Search"
        }
      ]
    }

    #ReportingPeriod
    reporting_period_eg_one =  {
        "id": "ocd-disclosure/reporting-period/d577982e-a55b-11e4-9771-bb010e0210e2",
        "description": "Federal Lobbying Disclosure: 2013, Second Quarter",
        "authorities": [
            sopr,
            house_clerk
        ],
        "period_type": "quarterly",
        "start_date": "2013-04-01",
        "end_date": "2013-06-30"
    }

    registrant_eg_one = {
      "id": "ocd-organization/23f9ce4e-a553-11e4-9771-bb010e0210e2",
      "name": "101 Strategy Partners, LLC",
      "other_names": [],
      "identifiers": [
        {
          "identifier": "42145",
          "scheme": "SOPR Lobbying Registrant ID"
        },
        {
          "identifier": "400987818",
          "scheme": "House Clerk Lobbying Registrant ID"
        }
      ],
      "jurisdiction": "",
      "jurisdiction_id": "",
      "classification": "Corporation",
      "parent_id": "",
      "founding_date": "",
      "dissolution_date": "",
      "image": "",
      "contact_details": [
        {
          "type": "voice",
          "label": "contact_phone",
          "value": "+1-202-414-6169",
          "note": "Mr. Blake Johnson"
        },
        {
          "type": "email",
          "label": "Mr. Blake Johnson",
          "value": "bjohnson@101sp.com",
          "note": "Mr. Blake Johnson"
        },
        {
          "type": "address",
          "label": "contact address",
          "value": "101 Constitution Ave NW, Suite L110, Washington, DC 20001",
          "note": "Mr. Blake Johnson"
        }
      ],
      "links": [],
      "extras": {
          "contact_details_structured": [
              {
                  "type": "address",
                  "label": "contact address",
                  "parts": [
                      {
                          "label": "address_one",
                          "value": "101 Constitution Ave NW",
                      },
                      {
                          "label": "address_two",
                          "value": "Suite L110",
                      },
                      {
                          "label": "city",
                          "value": "Washington",
                      },
                      {
                          "label": "state",
                          "value": "DC",
                      },
                      {
                          "label": "state",
                          "value": "20001",
                      },
                      {
                          "label": "country",
                          "value": "USA"
                      }
                  ],
                  "note": "registrant contact on SOPR LD-1"
              },
          ]
      }
    }

    client_eg_one = {
      "id": "ocd-organization/fc2be3fa-a55e-11e4-9771-bb010e0210e2",
      "name": "Imperatis Corp.",
      "other_names": [],
      "identifiers": [],
      "jurisdiction": "",
      "jurisdiction_id": "",
      "classification": "Corporation",
      "parent_id": "",
      "founding_date": "",
      "dissolution_date": "",
      "image": "",
      "contact_details": [
        {
          "type": "address",
          "label": "contact address",
          "value": "2231 Crystal Drive, Suite 401, Arlington, VA 22202",
          "note": ""
        }
      ],
      "links": [],
      "extras": {
          "contact_details_structured": [
              {
                  "type": "address",
                  "label": "contact address",
                  "parts": [
                      {
                          "label": "address",
                          "value": "2231 Crystal Drive, Suite 401",
                      },
                      {
                          "label": "city",
                          "value": "Arlington",
                      },
                      {
                          "label": "state",
                          "value": "VA",
                      },
                      {
                          "label": "zip",
                          "value": "22202",
                      },
                      {
                          "label": "country",
                          "value": "USA"
                      }
                  ],
                  "note": "client contact on SOPR LD-1"
              },
          ]
      }
    }

    filing_documents_one = [
            {
                "note": "submitted filing",
                "date": "2013-05-28",
                "links": [
                    {
                        "url": "http://soprweb.senate.gov/index.cfm?event=getFilingDetails&filingID=b4c3bd67-7c7c-45e6-8b6c-5fd6b55eec3f&filingTypeID=1",
                        "media_type": "text/html"
                    },
                    {
                        "url": "http://disclosures.house.gov/ld/ldxmlrelease/2013/RR/300567856.xml",
                        "media_type": "text/xml"
                    }
                ]
            }
        ]

    # Disclosure
    registration_eg = {
        "id": "ocd-disclosure/2f62bbd4-a561-11e4-9771-bb010e0210e2",
        "registrant": "101 Strategy Partners, LLC",
        "registrant_id": "23f9ce4e-a553-11e4-9771-bb010e0210e2",
        "authority": "Senate Office of Public Record",
        "authority_id": "d006f8f6-a35a-11e4-9771-bb010e0210e2",
        "reporting_period": "d577982e-a55b-11e4-9771-bb010e0210e2",
        "related_entities": [],
        "identifiers": [
            {
                "identifier": "b4c3bd67-7c7c-45e6-8b6c-5fd6b55eec3f",
                "scheme": "SOPR Lobbying Disclosure Filing ID"
            },
            {
                "identifier": "300567856",
                "scheme": "House Clerk Lobbying Disclosure Document ID"
            }
        ],
        "effective_date": "2013-05-28",
        "created_at": "2015-01-26T08:44:21Z",
        "updated_at": "2015-01-26T08:44:21Z",
        "documents": filing_documents_one,
        "disclosed_events": [
            {
                "id": "ocd-event/b2cfa11c-a5a7-11e4-9771-bb010e0210e2",
                "classification": "registration",
                "name": "101 Strategy Partners, LLC - New Client for Existing Registrant (2013Q2)",
                "start_time": "2013-05-28",
                "timezone": "America/New_York",
                "all_day": False,
                "end_time": None,
                "status": "",
                "description": "",
                "location": None,
                "media": None,
                "documents": filing_documents,
                "links": "",
                "participants": [
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/fc2be3fa-a55e-11e4-9771-bb010e0210e2",
                        "name": "Imperatis Corp.",
                        "note": "client"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/6cc21a3e-a560-11e4-9771-bb010e0210e2",
                        "name": "Lee Johnson",
                        "note": "lobbyist"
                    },
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/23f9ce4e-a553-11e4-9771-bb010e0210e2",
                        "name": "101 Strategy Partners, LLC",
                        "note": "registrant"
                    }
                ],
                "agenda": [
                    {
                        "description": "lobbying issues covered",
                        "subjects": [
                            "DEF"
                        ],
                        "media": None,
                        "notes": [
                            "Intelligence support for overseas combat operations"
                        ],
                        "related_entities": []
                    }
                ]
            }
        ],
        "extras": {
            "sopr_ld1_fields": {
                "self_employed_individual": False,
                "general_description": "Public Affairs and Communications",
                "signatures": [
                    {
                        "signature_date": "2013-05-28T14:29:38Z",
                        "signature": "Digitally Signed By: Blake Johnson"
                    },
                ],

            }
        }
    }

    lobbyist_eg = {
        "id": "ocd-person/6cc21a3e-a560-11e4-9771-bb010e0210e2",
        "name": "Lee Johnson",
        "other_names": [],
        "identifiers": [],
        "gender": "",
        "birth_date": "",
        "death_date": "",
        "image": "",
        "summary": "",
        "biography": "",
        "national_identity": "",
        "contact_details": [],
        "links": [],
        "memberships": [
            {
                "organization": {
                    "id": "ocd-organization/23f9ce4e-a553-11e4-9771-bb010e0210e2",
                    "classification": "corporation",
                    "name": "101 Strategy Partners, LLC",
                },
                "post": {
                    "id": "ocd-post/b2b1f7c4-a5b2-11e4-9771-bb010e0210e2",
                    "role": "lobbyist",
                    "start_date": "2012-09-12",
                }
            }
        ],
        "extras": {}
    }

    main_contact_eg = {
        "id": "ocd-person/34d69332-a5b2-11e4-9771-bb010e0210e2",
        "name": "Mr. Blake Johnson",
        "other_names": [],
        "identifiers": [],
        "gender": "",
        "birth_date": "",
        "death_date": "",
        "image": "",
        "summary": "",
        "biography": "",
        "national_identity": "",
        "contact_details": [],
        "links": [],
        "memberships": [
            {
                "organization": {
                    "id": "ocd-organization/23f9ce4e-a553-11e4-9771-bb010e0210e2",
                    "classification": "corporation",
                    "name": "101 Strategy Partners, LLC",
                },
                "post": {
                    "id": "ocd-post/1f6ebafe-a5b4-11e4-9771-bb010e0210e2",
                    "role": "contact",
                    "start_date": "2012-09-12",
                }
            }
        ],
        "extras": {}
    }

Lobbying Report Example::

    registrant_eg_two = {
      "id": "ocd-organization/88c1eee4-a5e2-11e4-9771-bb010e0210e2",
      "name": "DRINKER BIDDLE & REATH LLP",
      "other_names": [],
      "identifiers": [
        {
          "identifier": "12631",
          "scheme": "SOPR Lobbying Registrant ID"
        },
        {
          "identifier": "31801",
          "scheme": "House Clerk Lobbying Registrant ID"
        }
      ],
      "jurisdiction": "",
      "jurisdiction_id": "",
      "classification": "Corporation",
      "parent_id": "",
      "founding_date": "",
      "dissolution_date": "",
      "image": "",
      "contact_details": [
        {
          "type": "voice",
          "label": "contact_phone",
          "value": "+1-202-230-5145",
          "note": "ILISA HALPERN PAUL"
        },
        {
          "type": "email",
          "label": "contact_email",
          "value": "ilisa.paul@dbr.com",
          "note": "ILISA HALPERN PAUL"
        },
        {
          "type": "address",
          "label": "contact address",
          "value": "1500 K STREET, NW, WASHINGTON, DC, 20005",
          "note": "Mr. Robert Driscoll"
        }
      ],
      "links": [],
      "extras": {
          "contact_details_structured": [
              {
                  "type": "address",
                  "label": "contact address",
                  "parts": [
                      {
                          "label": "address_one",
                          "value": "1500 K STREET, NW",
                      },
                      {
                          "label": "address_two",
                          "value": "",
                      },
                      {
                          "label": "city",
                          "value": "WASHINGTON",
                      },
                      {
                          "label": "state",
                          "value": "DC",
                      },
                      {
                          "label": "country",
                          "value": "USA"
                      },
                      {
                          "label": "zip",
                          "value": "20005"
                      }
                  ],
                  "note": "registrant principal place of business on SOPR LD-2"
              },
              {
                  "type": "address",
                  "label": "principal place of business",
                  "parts": [
                      {
                          "label": "city",
                          "value": "Philadelphia",
                      },
                      {
                          "label": "state",
                          "value": "PA",
                      },
                      {
                          "label": "country",
                          "value": "USA"
                      },
                      {
                          "label": "zip",
                          "value": "19103-6996"
                      }
                  ],
                  "note": "registrant principal place of business on SOPR LD-2"
              },
          ]
      }
    }

    reporting_period_eg_two =  {
        "id": "ocd-disclosure/reporting-period/e9aaedd4-a5e5-11e4-9771-bb010e0210e2",
        "description": "Federal Lobbying Disclosure: 2013, Third Quarter",
        "authorities": [
            sopr,
            house_clerk
        ],
        "period_type": "quarterly",
        "start_date": "2013-07-01",
        "end_date": "2013-09-30"
    }

    filing_documents_two = [
            {
                "note": "submitted filing",
                "date": "2013-10-17",
                "links": [
                    {
                        "url": "http://soprweb.senate.gov/index.cfm?event=getFilingDetails&filingID=80b956e1-3448-404a-bdfd-558ffe2631ce&filingTypeID=69",
                        "media_type": "text/html"
                    },
                    {
                        "url": "http://disclosures.house.gov/ld/ldxmlrelease/2013/RR/300567856.xml",
                        "media_type": "text/xml"
                    }
                ]
            }
        ]

    client_eg_two = {
      "id": "ocd-organization/b82bca00-a5e8-11e4-9771-bb010e0210e2",
      "name": "Smith & Nephew, Inc.",
      "other_names": [],
      "identifiers": [
          {
              "identifier": "12631-1005496",
              "scheme": "SOPR Lobbying Registrant-Client ID"
          },
          {
              "identifier": "318010137",
              "scheme": "House Clerk Lobbying Registrant-Client ID"
          }
      ],
      "jurisdiction": "",
      "jurisdiction_id": "",
      "classification": "Corporation",
      "parent_id": "",
      "founding_date": "",
      "dissolution_date": "",
      "image": "",
      "contact_details": [
        {
          "type": "address",
          "label": "contact address",
          "value": "1701 Pennsylvania Avenue, N.W., Suite 300, Washington, DC, 20006, USA",
          "note": "client address on SOPR LD-1"
        },
        {
          "type": "address",
          "label": "principal place of business",
          "value": "1701 Pennsylvania Avenue, N.W., Suite 300, Washington, DC, 20006, USA",
          "note": ""
        }
      ],
      "links": [],
      "extras": {
          "contact_details_structured": [
              {
                  "type": "address",
                  "label": "contact address",
                  "parts": [
                      {
                          "label": "address",
                          "value": "1701 Pennsylvania Avenue, N.W., Suite 300",
                      },
                      {
                          "label": "city",
                          "value": "Washington",
                      },
                      {
                          "label": "state",
                          "value": "DC",
                      },
                      {
                          "label": "zip",
                          "value": "20006",
                      },
                      {
                          "label": "country",
                          "value": "USA"
                      }
                  ],
                  "note": "client address on SOPR LD-1"
              },
              {
                  "type": "address",
                  "label": "principal place of business",
                  "parts": [
                      {
                          "label": "city",
                          "value": "Memphis",
                      },
                      {
                          "label": "state",
                          "value": "TN",
                      },
                      {
                          "label": "zip",
                          "value": "38116",
                      },
                      {
                          "label": "country",
                          "value": "USA"
                      }
                  ],
                  "note": "client address on SOPR LD-1"
              },
          ],
          "description": "Developer of advanced medical devices for healthcare professionals around the world"
      }
    }

    # Disclosure
    report_eg = {
        "id": "2f62bbd4-a561-11e4-9771-bb010e0210e2",
        "registrant": "DRINKER BIDDLE & REATH, LLP",
        "registrant_id": "88c1eee4-a5e2-11e4-9771-bb010e0210e2",
        "authority": "Senate Office of Public Record",
        "authority_id": "d006f8f6-a35a-11e4-9771-bb010e0210e2",
        "reporting_period_id": "ocd-disclosure/reporting-period/e9aaedd4-a5e5-11e4-9771-bb010e0210e2",
        "reporting_period": "Federal Lobbying Disclosure: 2013, Third Quarter",
        "related_entities": [],
        "identifiers": [
            {
                "identifier": "80b956e1-3448-404a-bdfd-558ffe2631ce",
                "scheme": "SOPR Lobbying Disclosure Filing ID"
            },
            {
                "identifier": "300595733",
                "scheme": "House Clerk Lobbying Disclosure Document ID"
            }
        ],
        "effective_date": "2013-10-17",
        "created_at": "2015-01-26T10:44:21Z",
        "updated_at": "2015-01-26T10:44:21Z",
        "documents": filing_documents_two,
        "disclosed_events": [
            {
                "id": "ocd-event/b2cfa11c-a5a7-11e4-9771-bb010e0210e2",
                "classification": "report",
                "name": "DRINKER BIDDLE & REATH - Lobbying Report, TAX for client Smith & Nephew (2013Q3)",
                "start_time": "2013-07-01",
                "timezone": "America/New_York",
                "all_day": False,
                "end_time": "2013-09-30",
                "status": "",
                "description": "",
                "location": None,
                "media": None,
                "documents": filing_documents,
                "links": "",
                "participants": [
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/b82bca00-a5e8-11e4-9771-bb010e0210e2",
                        "name": "Smith & Nephew, Inc.",
                        "note": "client"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jodie Curtis",
                        "note": "lobbyist"
                    },
                    {
                        "entity_type": "organization",
                        "name": "DRINKER BIDDLE & REATH, LLP",
                        "id": "ocd-organization/88c1eee4-a5e2-11e4-9771-bb010e0210e2",
                        "note": "registrant"
                    },
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/{{house uuid}}",
                        "name": "US HOUSE OF REPRESENTATIVES",
                        "note": "lobbied"
                    }
                ],
                "agenda": [
                    {
                        "description": "lobbying issues covered",
                        "subjects": [
                            "TAX"
                        ],
                        "media": None,
                        "notes": [
                            "S. 232/H.R. 523, The Protect Medical Innovation Act of 2013."
                        ],
                        "related_entities": [
                            {
                                "entity_type": "bill",
                                "entity_name": "S 232",
                                "id": "ocd-bill/{{bill uuid}}",
                                "title": "The Protect Medical Innovation Act of 2013",
                                "related_bills": [
                                    {
                                        "identifier": "HR 523"
                                    }
                                ]
                            },
                            {
                                "entity_type": "bill",
                                "entity_name": "HR 523",
                                "id": "ocd-bill/{{bill uuid}}",
                                "title": "The Protect Medical Innovation Act of 2013",
                                "related_bills": [
                                    {
                                        "identifier": "S 232"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "id": "ocd-event/226e6360-a5f2-11e4-9771-bb010e0210e2",
                "classification": "report",
                "name": "DRINKER BIDDLE & REATH - Lobbying Report, MMM for client Smith & Nephew (2013Q3)",
                "start_time": "2013-07-01",
                "timezone": "America/New_York",
                "all_day": False,
                "end_time": "2013-09-30",
                "status": "",
                "description": "",
                "location": None,
                "media": None,
                "documents": filing_documents,
                "links": "",
                "participants": [
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/b82bca00-a5e8-11e4-9771-bb010e0210e2",
                        "name": "Smith & Nephew, Inc.",
                        "note": "client"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jodie Curtis",
                        "note": "lobbyist"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jim Twaddell",
                        "note": "lobbyist",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/f07f0666-a5ec-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Arlen Specter",
                                },
                                "post": {
                                    "id": "ocd-post/e9b95034-a5ec-11e4-9771-bb010e0210e2",
                                    "role": "legal aide",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/f07f0666-a5ec-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Arlen Specter",
                                },
                                "post": {
                                    "id": "ocd-post/12008148-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "deputy communications director",
                                }
                            }
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jeremy Scott",
                        "note": "lobbyist",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/471f0282-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Mike DeWine",
                                },
                                "post": {
                                    "id": "ocd-post/8355a260-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "staff assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/471f0282-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Mike DeWine",
                                },
                                "post": {
                                    "id": "ocd-post/12008148-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "legal correspondent",
                                }
                            }
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/e47bebbc-a5ed-11e4-9771-bb010e0210e2",
                        "name": "Ilsa Halpern Paul",
                        "note": "lobbyist",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/d10ea088-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Dianne Feinstein",
                                },
                                "post": {
                                    "id": "ocd-post/f87a5b12-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "staff assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/d10ea088-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Dianne Feinstein",
                                },
                                "post": {
                                    "id": "ocd-post/3a10bc24-a5ee-11e4-9771-bb010e0210e2",
                                    "role": "legal correspondent",
                                }
                            },
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/b5e9e3d8-a5ef-11e4-9771-bb010e0210e2",
                        "name": "Rebecca McGrath",
                        "note": "lobbyist",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/d2ad924e-a5ef-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Chris Dodd",
                                },
                                "post": {
                                    "id": "ocd-post/d95fab7c-a5ef-11e4-9771-bb010e0210e2",
                                    "role": "legal assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/d2ad924e-a5ef-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Chris Dodd",
                                },
                                "post": {
                                    "id": "ocd-post/15c99e60-a5f0-11e4-9771-bb010e0210e2",
                                    "role": "scheduler",
                                }
                            },
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Julie Hyams",
                        "note": "lobbyist",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/8218c230-a5f0-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Representative Louis Stokes",
                                },
                                "post": {
                                    "id": "ocd-post/89b84e8e-a5f0-11e4-9771-bb010e0210e2",
                                    "role": "legal assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/8218c230-a5f0-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Representative Louis Stokes",
                                },
                                "post": {
                                    "id": "ocd-post/a39a5bbc-a5f0-11e4-9771-bb010e0210e2",
                                    "role": "staff assistant",
                                }
                            }
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Erin Morton",
                        "note": "lobbyist"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Anna Howard",
                        "note": "lobbyist"
                    },
                    {
                        "entity_type": "organization",
                        "name": "DRINKER BIDDLE & REATH, LLP",
                        "id": "ocd-organization/88c1eee4-a5e2-11e4-9771-bb010e0210e2",
                        "note": "registrant"
                    },
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/{{house uuid}}",
                        "name": "US HOUSE OF REPRESENTATIVES",
                        "note": "lobbied"
                    }
                ],
                "agenda": [
                    {
                        "description": "lobbying issues covered",
                        "subjects": [
                            "MMM"
                        ],
                        "media": None,
                        "notes": [
                            "Proposed rule regarding durable medical equipment reimbursement definition of routinely purchased."
                        ],
                        "related_entities": []
                    }
                ]
            },
            {
                "id": "ocd-event/10629c86-a5f2-11e4-9771-bb010e0210e2",
                "classification": "report",
                "name": "DRINKER BIDDLE & REATH - Lobbying Report, TAX for client Smith & Nephew (2013Q3)",
                "start_time": "2013-07-01",
                "timezone": "America/New_York",
                "all_day": False,
                "end_time": "2013-09-30",
                "status": "",
                "description": "",
                "location": None,
                "media": None,
                "documents": filing_documents,
                "links": "",
                "participants": [
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/b82bca00-a5e8-11e4-9771-bb010e0210e2",
                        "name": "Smith & Nephew, Inc.",
                        "note": "client"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jodie Curtis",
                        "note": "lobbyist"
                    },
                    {
                        "entity_type": "organization",
                        "name": "DRINKER BIDDLE & REATH, LLP",
                        "id": "ocd-organization/88c1eee4-a5e2-11e4-9771-bb010e0210e2",
                        "note": "registrant"
                    },
                ],
                "agenda": [
                    {
                        "description": "lobbying issues covered",
                        "subjects": [
                            "ECN"
                        ],
                        "media": None,
                        "notes": [
                            "Global Investment in American Jobs Act (H.R. 2052, S. 1023)."
                        ],
                        "related_entities": [
                            {
                                "entity_type": "bill",
                                "entity_name": "S 1023",
                                "id": "ocd-bill/{{bill uuid}}",
                                "title": "Global Investment in American Jobs Act",
                                "related_bills": [
                                    {
                                        "identifier": "HR 2052"
                                    }
                                ]
                            },
                            {
                                "entity_type": "bill",
                                "entity_name": "HR 2052",
                                "id": "ocd-bill/{{bill uuid}}",
                                "title": "Global Investment in American Jobs Act",
                                "related_bills": [
                                    {
                                        "identifier": "S 1023"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "id": "ocd-event/c3a740b8-a5f1-11e4-9771-bb010e0210e2",
                "classification": "registration",
                "name": "DRINKER BIDDLE & REATH - Lobbying Report, TAX for client Smith & Nephew (2013Q3)",
                "start_time": "2013-07-01",
                "timezone": "America/New_York",
                "all_day": False,
                "end_time": "2013-09-30",
                "status": "",
                "description": "",
                "location": None,
                "media": None,
                "documents": filing_documents,
                "links": "",
                "participants": [
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jim Twaddell",
                        "note": "lobbyist-added",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/f07f0666-a5ec-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Arlen Specter",
                                },
                                "post": {
                                    "id": "ocd-post/e9b95034-a5ec-11e4-9771-bb010e0210e2",
                                    "role": "legal aide",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/f07f0666-a5ec-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Arlen Specter",
                                },
                                "post": {
                                    "id": "ocd-post/12008148-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "deputy communications director",
                                }
                            }
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Jeremy Scott",
                        "note": "lobbyist-added",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/471f0282-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Mike DeWine",
                                },
                                "post": {
                                    "id": "ocd-post/8355a260-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "staff assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/471f0282-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Mike DeWine",
                                },
                                "post": {
                                    "id": "ocd-post/12008148-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "legal correspondent",
                                }
                            }
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/e47bebbc-a5ed-11e4-9771-bb010e0210e2",
                        "name": "Ilsa Halpern Paul",
                        "note": "lobbyist-added",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/d10ea088-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Dianne Feinstein",
                                },
                                "post": {
                                    "id": "ocd-post/f87a5b12-a5ed-11e4-9771-bb010e0210e2",
                                    "role": "staff assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/d10ea088-a5ed-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Dianne Feinstein",
                                },
                                "post": {
                                    "id": "ocd-post/3a10bc24-a5ee-11e4-9771-bb010e0210e2",
                                    "role": "legal correspondent",
                                }
                            },
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/b5e9e3d8-a5ef-11e4-9771-bb010e0210e2",
                        "name": "Rebecca McGrath",
                        "note": "lobbyist-added",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/d2ad924e-a5ef-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Chris Dodd",
                                },
                                "post": {
                                    "id": "ocd-post/d95fab7c-a5ef-11e4-9771-bb010e0210e2",
                                    "role": "legal assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/d2ad924e-a5ef-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Senator Chris Dodd",
                                },
                                "post": {
                                    "id": "ocd-post/15c99e60-a5f0-11e4-9771-bb010e0210e2",
                                    "role": "scheduler",
                                }
                            },
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Julie Hyams",
                        "note": "lobbyist-added",
                        "memberships": [
                            {
                                "organization": {
                                    "id": "ocd-organization/8218c230-a5f0-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Representative Louis Stokes",
                                },
                                "post": {
                                    "id": "ocd-post/89b84e8e-a5f0-11e4-9771-bb010e0210e2",
                                    "role": "legal assistant",
                                }
                            },
                            {
                                "organization": {
                                    "id": "ocd-organization/8218c230-a5f0-11e4-9771-bb010e0210e2",
                                    "classification": "staff",
                                    "name": "Staff, Representative Louis Stokes",
                                },
                                "post": {
                                    "id": "ocd-post/a39a5bbc-a5f0-11e4-9771-bb010e0210e2",
                                    "role": "staff assistant",
                                }
                            }
                        ]
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/53a6918a-a5ea-11e4-9771-bb010e0210e2",
                        "name": "Erin Morton",
                        "note": "lobbyist-added"
                    },
                    {
                        "entity_type": "organization",
                        "name": "DRINKER BIDDLE & REATH, LLP",
                        "id": "ocd-organization/88c1eee4-a5e2-11e4-9771-bb010e0210e2",
                        "note": "registrant"
                    },
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/b82bca00-a5e8-11e4-9771-bb010e0210e2",
                        "name": "Smith & Nephew, Inc.",
                        "note": "client"
                    }
                ]
            },
            {
                "id": "ocd-event/c3a740b8-a5f1-11e4-9771-bb010e0210e2",
                "classification": "registration",
                "name": "DRINKER BIDDLE & REATH - Registration Update for client Smith & Nephew (2013Q3)",
                "start_time": "2013-07-01",
                "timezone": "America/New_York",
                "all_day": False,
                "end_time": "2013-09-30",
                "status": "",
                "description": "removing lobbyist(s)",
                "location": None,
                "media": None,
                "documents": filing_documents,
                "links": "",
                "participants": [
                    {
                        "entity_type": "organization",
                        "name": "DRINKER BIDDLE & REATH, LLP",
                        "id": "ocd-organization/88c1eee4-a5e2-11e4-9771-bb010e0210e2",
                        "note": "registrant"
                    },
                    {
                        "entity_type": "organization",
                        "id": "ocd-organization/b82bca00-a5e8-11e4-9771-bb010e0210e2",
                        "name": "Smith & Nephew, Inc.",
                        "note": "client"
                    },
                    {
                        "entity_type": "person",
                        "id": "ocd-person/32d71548-a5f3-11e4-9771-bb010e0210e2",
                        "name": "Andrew Bowman",
                        "note": "lobbyist-removed"
                    }
                ]
            }
        ],
        "extras": {
            "sopr_ld2_fields": {
                "self_employed_individual": False,
                "general_description": "Public Affairs and Communications",
                "signatures": [
                    {
                        "signature_date": "2013-05-28T14:29:38Z",
                        "signature": "Digitally Signed By: Blake Johnson"
                    },
                ],
                "expenses": {
                    "expense_amount": None,
                    "expense_method_a": False,
                    "expense_method_c": False,
                    "expense_method_b": False,
                    "expense_less_than_five_thousand": False,
                    "expense_five_thousand_or_more": False
                },
                "income": {
                    "income_less_than_five_thousand": False,
                    "income_amount": 50000.0,
                    "income_five_thousand_or_more": True
                },

            }
        }
    }
