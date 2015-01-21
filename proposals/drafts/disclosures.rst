====================
OCDEP: Disclosures
====================

:Created: 
:Author: Bob Lannon
:Status: Draft

Overview
========

Definition of the `Disclosure` type, a top-level type that models officially submitted disclosure records. There may be subtypes, each corresponding to particular kinds of disclosure (eg, lobbying disclosure or campaign finance disclosure).

`Disclosure` subtypes dealing with lobbying include `LobbyingRegistration` and `LobbyingReport`. Individual instances of lobbying are `Events` of type `LobbyingEvent`.

`Disclosure` subtypes dealing with political contributions include `ContributionsRegistration` and `ContributionsReport`. Individual transactions are `Events` of type `ContributionsEvent`.

Definitions
-----------

DisclosureAuthority
    The authority to which disclosures must be submitted.

Disclosure
    The act of disclosing information to a DisclosureAuthority.

Form
    A form submitted as part of a disclosure

Field
    A field submitted as part of a form

Schedule
    A schedule submitted as part of a disclosure

Line
    A line item submitted as part of a schedule

Rationale
=========

Legislative accountability requires full knowledge of the non-governmental actors who engage with policymakers, regulatory bodies, and other official sources. Disclosures should properly identify the parties engaging in disclosed acts, as well as the officials, bodies of government and non-governmental organizations contacted.

Implementation
==============

DisclosureAuthority
-------------------
The basis for the DisclosureAuthority is the Open Civic Data ``Organization`` type, as described in `OCDEP 5: People, Organizations, Posts, and Memberships <http://opencivicdata.readthedocs.org/en/latest/proposals/0005.html>`_.

disclosure_classification
    A list of disclosure types that this authority is responsible for collecting and/or publishing. 
    
    identifier
        A unique identifier for this disclosure type.

    name
        The canonical name for this disclosure type.

    classification
        Choices are:
        
        * lobbying      - Disclosures related to lobbying
        * contributions - Disclosures related to political contributions

reporting_periods
    A list of the reporting periods defined by this authority

    identifier
        A unique identifier for the reporting period

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

    disclosures
        disclosures accepted during the reporting period

Disclosure
----------

id
    Identifier that uniquely identifies the disclosure.

registrant, registrant_id
    The organization or individual who is registering.

authority, authority_id
    The organization that the registration is due to.

reporting_period
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
        * sponsoring-organization

forms
    **optional**
    A list of forms associated with this report type. See ``Forms`` section below.

schedules
    **optional**
    A list of schedules associated with this report type. See ``Schedules`` section below.

document_id
    **optional**
    Upstream identifier of the associated document if one exists, such as the filing ID assigned by the Senate Office of Public Record

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

identifier
    An identifier that uniquely identifies the disclosure type.

name
    The canonical name of the disclosure type

classification
    The classification of the disclosure type. Current values include:
    
    * registration  - registers a person or organization with a DisclosureAuthority
    * report        - makes a periodic report to a DisclosureAuthority

amends_type
    The identifier of the disclosure type that this disclosure type is able to amend. Can be the same as identifier, where future submissions supercede past submissions.

amendment
    **optional**
    A boolean that is true if this is a registration type that is reserved for amending other registration types

Form
----
Object representing form used for making disclosures

identifier
    An identifier that uniquely identifies the form

form_type
    An identifier that points to the type of form

fields
    A list of sub-objects representing fields in the form. See ``Field`` section below

FormType
~~~~~~~~
The type of a form

identifier
    An identifier that uniquely identifies the form type

name
    The canonical name of the form

description
    description of the form

Field
-----
Object representing a field used in a disclosure form

identifier
    An identifier that uniquely identifies the field

field_type
    An identifier that points to the type of field

value
    The value of the field

FieldType
~~~~~~~~~
The type of a field

identifier
    An identifier that uniquely identifies the field type

name
    The canonical name of the field

description
    Description of the field

Schedule
--------
Object representing a schedule used for making disclosures

identifier
    An identifier that uniquely identifies the schedule

schedule_type
    An identifier that points to the schedule's type. See ``Type`` section below

lines
    A list of sub-objects representing lines in the schedule. See ``Line`` section below

ScheduleType
~~~~~~~~
The type of a schedule

identifier
    An identifier that uniquely identifies the schedule type

name
    The canonical name of the schedule type

description
    description of the schedule type

Line
----
Object representing line used to populate a schedule

identifier
    An identifier that uniquely identifies the line

line_type
    A identifier that points to the line's type. See ``LineType`` section below

value
    The value of the line

LineType
~~~~~~~~~
The type of a line

identifier
    An identifier that uniquely identifies the line type

name
    The canonical name of the line type

description
    description of the line type



DefinedSchema
-------------

TODO
