=============================
OCDEP 2: Division Identifiers
=============================

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

LobbyingRegistration
    A record of registration to engage in lobbying activity, submitted by a registrant ``organization`` or ``person`` to the ``organization`` responsible for collecting lobbying disclosures. An example is the `LD-1 form <http://soprweb.senate.gov/index.cfm?event=getFilingDetails&filingID=11886c30-f2fa-4994-8c05-575f715f614e&filingTypeID=1>`_, submitted to the United States Congress.

LobbyingReport
    A record submitted by a registrant ``organization`` or ``person``, reporting zero or more objects of type ``LobbyingActivity`` over some time interval. An example is the quarterly `LD-2 form <http://soprweb.senate.gov/index.cfm?event=getFilingDetails&filingID=670410d5-de38-43a7-b4b3-ab5760d47f6f&filingTypeID=69>`_, submitted to the United States congress.

LobbyingEvent
     A subtype of ``Event``. Contact with an official ``organization`` that constitutes lobbying as defined by the appropriate ``jurisdiction``. These are understood to have been carried out by a ``registrant`` on behalf of a ``client``.

ContributionsRegistration
    A record of an ``organization``'s registration as a contributor and/or reciepient of contributions. An example is `FEC Form 1 <http://docquery.fec.gov/cgi-bin/dcdev/forms/C00295527/245548/>`_, submitted to the United States Federal Elections Commission.

ContributionsReport
    A record of a registered ``organization``'s contributions, reciepts, disbursements, loans, expenditures and any other transactions it is required to disclose. An example is `FEC Form 3 <http://docquery.fec.gov/cgi-bin/dcdev/forms/C00431445/959763/>`_, submitted to the United States Federal Elections Commission.

ContributionsEvent
    A subtype of ``Event``. An itemized transaction representing a contribution, reciept, disbursement, loan, expenditure or any other transactions that must be disclosed by a registered ``organization``.

Rationale
=========

Legislative accountability requires full knowledge of the non-governmental actors who lobby representatives regarding the proposal and consideration of legislative actions. Where lobbying activity is disclosed, it should properly identify the officials, bodies of government and non-governmental organizations involved. It should also properly identify pieces of legislation discussed.

Implementation
==============

DisclosureAuthority
-------------------

The basis for the DisclosureAuthority is the Open Civic Data ``Organization`` type, as described in `OCDEP 5: People, Organizations, Posts, and Memberships <http://opencivicdata.readthedocs.org/en/latest/proposals/0005.html>`_.

disclosure_types
    A list of disclosure types that this authority is responsible for collecting and/or publishing. 
    
    identifier
        A unique identifier for this disclosure type.

    name
        The canonical name for this disclosure type.

    classification
        Choices are:
        
        * lobbying      - Disclosures related to lobbying
        * contributions - Disclosures related to political contributions

registration_types
    A list of sub-objects representing the types of registrations submitted to this authority

    identifier
        An identifier that uniquely identifies the registration type.

    name
        The canonical name of the registration type

    amends_type
        The identifier of the registration_type that this registration_type is able to amend. Can be the same as identifier
    
    classification
        **optional**
        The type of registration.

    amendment
        **optional**
        A boolean that is true if this is a registration type that is reserved for amending other registration types

    forms
        **optional**
        A list of identifiers for the forms associated with this report type. See ``Forms`` section below.

        identifier
            The identifier of the form

    schedules
        **optional**
        A list of identifiers for the schedules associated with this report type. See ``Schedules`` section below.

        identifier
            The identifier of the schedule

report_types
    A list of sub-objects representing the types of reports submitted to this authority

    identifier
        An identifier that uniquely identifies the report type.

    name
        The canonical name of the report type

    amends_type
        The identifier of the report_type that this report_type is able to amend. Can be the same as identifier
    
    classification
        **optional**
        The type of registration.

    amendment
        **optional**
        A boolean that is true if this is a registration type that is reserved for amending other registration types

    forms
        **optional**
        A list of identifiers for the forms associated with this report type. See ``Forms`` section below.

        identifier
            The identifier of the form

    schedules
        **optional**
        A list of identifiers for the schedules associated with this report type. See ``Schedules`` section below.

        identifier
            The identifier of the schedule

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

Form
~~~~
Object representing forms used for making disclosures

identifier
    An identifier that uniquely identifies the form

name
    The canonical name of the form

description
    description of the form

Schedule
~~~~~~~~
Object representing schedules used for making disclosures

identifier
    An identifier that uniquely identifies the schedule

name
    The canonical name of the schedule

description
    description of the schedule

LobbyingRegistration
--------------------

id
    Open Civic Data-style id, in the format ``ocd-disclosure/lobbying/registration/{{uuid}}``.

registrant, registrant_id
    The organization or individual who is registering.

authority, authority_id
    The organization that the registration is due to.

reporting_period
    The reporting period to which this registration was submitted.

registration_type
    The type of the registration, as categorized by the relevant authority

lobbyists
    Where the registrant is an organization and the registration lists that organization's lobbyists, a list of Open Civic Data people IDs, one for each lobbyist

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

LobbyingReport
--------------

id
    Open Civic Data-style id ``ocd-disclosure/lobbying/report/{{uuid}}``

document_id
    **optional**
    Upstream identifier of the associated document if one exists, such as the internal filing ID assigned by the Senate Office of Public Record

reporting_period
    The reporting period to which this report was submitted.

report_type
    The type of this report, as categorized by the relevant authority.

registrant, registrant_id
    The organization or individual who is registering.

authority, authority_id
    The organization that the registration is due to.

client, client_id
    The organization or individual on whose behalf the registrant is acting. May be the same organization or individual as the registrant.

document_id
    **optional**
    Upstream identifier of the associated document if one exists, such as the filing ID assigned by the Senate Office of Public Record

start_date
    Beginning of period covered by this report

end_date
    End of period covered by this report

submitted_date
    **optional**
    Date (and possibly time) when document was submitted.

lobbying_events
    A list of ``LobbyingEvent`` objects, described below.

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

LobbyingEvent
-------------
The basis for the LobbyingEvent is the Open Civic Data ``Event`` type, as described in `OCDEP 4: Events <http://opencivicdata.readthedocs.org/en/latest/proposals/0004.html>`_. Constraints on field values specified below

id
    Open Civic Data-style id in the format ``ocd-disclosure/lobbying/event/{{uuid}}``

classification
    As defined in the ``Event`` type, where values are extended to include ``lobbying-contact``

participants
    Participants associated with the event. Includes lobbyists, lobbied organizations and/or lobbied individuals, and bills.

    note
        As defined on the ``Event`` type, where values identifies the role of the participant. choices are:
        * lobbyist  - the participant is lobbying
        * lobbied   - the participant is being lobbied
        * regarding - the participant is the subject of lobbying

DefinedSchema
-------------

TODO
