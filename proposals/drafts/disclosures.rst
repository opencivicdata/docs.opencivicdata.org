====================
OCDEP: Disclosures
====================

:Created: 
:Author: Bob Lannon
:Status: Draft

Overview
========

Definition of the ``Disclosure`` type, a top-level type that models officially submitted disclosure records. In addition, the ``DisclosureAuthority`` and ``DisclosureEvent``.

Definitions
-----------

DisclosureAuthority
    The authority to which disclosures must be submitted.

Disclosure
    The act of disclosing information to a DisclosureAuthority.

DisclosureEvent
    The actual event being disclosed. Rather than employ a taxonomy of event types, events can be identified with one another to the extent that they share participant types and participant roles. Participant roles are expressed through the "note" field. A sufficiently expressive list of roles should allow full coverage of multiple disclosure authorities and jurisdictions without sacrificing comparability.

Rationale
=========

Legislative accountability requires full knowledge of the non-governmental actors who engage with policymakers, regulatory bodies, and other official sources. Disclosures should properly identify the parties engaging in disclosed acts, as well as the officials, bodies of government and non-governmental organizations contacted.

Implementation
==============

DisclosureAuthority
-------------------
The basis for the DisclosureAuthority is the Open Civic Data ``Organization`` type, as described in `OCDEP 5: People, Organizations, Posts, and Memberships <http://opencivicdata.readthedocs.org/en/latest/proposals/0005.html>`_.

disclosure_types
    A list of disclosure types that this authority is responsible for collecting and/or publishing. 

reporting_periods
    A list of the reporting periods defined by this authority

    id
        A unique id for the reporting period

    description
        Description of the reporting period

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

    disclosure_types
        disclosures accepted during the reporting period

Disclosure
----------

id
    Open Civic Data-style id in the format ``ocd-disclosure/{{this.disclosure_type.arena}}/{{uuid}}``

registrant, registrant_id
    The organization or individual who is registering.

authority, authority_id
    The organization that the registration is due to.

reporting_period, reporting_period_id
    The reporting period to which this registration was submitted.

disclosure_type
    the type of the disclosure. See ``DisclosureType`` section below.

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

Disclosure Type
~~~~~~~~~~~~~~~

id
    An id that uniquely identifies the disclosure type.

name
    The canonical name of the disclosure type

description
    Description of the disclosure type

action
    The action performed by this disclosure type. Current values include:
    
    * registration  - registers a person or organization with a DisclosureAuthority
    * report        - makes a periodic report to a DisclosureAuthority

classification
    The category of the disclosure type. Current values include:
        
    * lobbying      - Disclosures related to lobbying
    * contributions - Disclosures related to political contributions

amends_type
    The id of the disclosure type that this disclosure type is able to amend. Can be the same as id, where future submissions supercede past submissions.

amendment
    **optional**
    A boolean that is true if this is a registration type that is reserved for amending other registration types

DisclosedEvent
--------------
The basis for the DisclosedEvent is the Open Civic Data ``Event`` type, as described in `OCDEP 4: Events <http://opencivicdata.readthedocs.org/en/latest/proposals/0004.html>`_. Constraints on field values specified below

id
    An id that uniquely identifies the event.

classification
    As defined in the ``Event`` type, where values are extended to include:

    * lobbying
    * contribution

participants
    Participants associated with the event. 

    note
        As defined on the ``Event`` type, where values identifies the role of the participant. Choices include the following, and may be updated:
          * lobbyist      - (lobbying) person who actually did the lobbying
          * lobbied       - (lobbying) organizations and/or individuals that were lobbied
          * regarding     - (lobbying) bills, regulations or other matters that can be identified
          * contributor   - (contributions) the source of the transaction
          * recipient     - (contributions) the target of the contribution
          * lender        - (contributions) the source of a loan
          * borrower      - (contributions) the recipient of a loan
          * creditor      - (contributions) entity to which a debt is owed
          * debtor        - (contributions) entity which owes a debt


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

    disclosure_type_schema = {
        "properties": {
            "id": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "action": {
                "type": "string",
                "enum": disclosure_actions
            },
            "classification": {
                "type": "string",
                "enum": disclosure_classifications
            },
            "amends_type": {
                "type": "string"
            },
            "amendment": {
                "type": "boolean"
            }
        },
        "type": "object"
    }

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
            "disclosure_type": disclosure_type_schema,
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
