====================
OCDEP: Campaign Finance Filings
====================

:Created:
:Author: Abraham Epton
:Status: Draft

Overview
========

Definition of the Campaign Finance Filing type and associated other types to
model campaign finance filings with a regulator.

Definitions
-----------

Campaign Finance Regulator (Regulator)
    Any government agency in charge of gathering information and enforcing
    transparency laws against political committees (Committees).

Campaign Finance Filing (Filing)
    Any single document filed with a Regulator.

Jurisdiction
    OCD Jurisdiction indicating the region covered by an office, or for which an
    Election is being held.

Section
    A container for a unit of meaning inside a Filing, that isn't inherent to
    the basic process of filing a document with an agency.

Ballot Measure
    A proposition or question with two or more predetermined options that voters may select as part of an election. These include:

    * The enactment or repeal of a statute, constitutional amendment or other form of law.
    * Approval or rejection of a new tax or additional spending of public funds.
    * The recall or retention of a previously elected public office holder.

Candidacy
    The condition of a person competing to hold a public office for defined term of office.

Contest
    A specific decision with a set of predetermined options put before voters in an election. These contests include the selection of a person from a list of candidates to hold a public office or the approval or rejection of a ballot measure.


Rationale
=========

Political committees file statements with their regulators in order to disclose
funders, expenditures, organizational ties and other financial details. Filings
encapsulate some number of possible specific disclosures, and some filings can
contain more than one type of disclosure, so this proposed option is to consider
each actual filing as an object and then each specific disclosed piece of
information as associated with that object. So a committee name change would be
associated with a Filing, along with a committee address change and a committee
officer addition. A series of committee contributions and committee expenses
would be attached to one Filing. This way we don't need to model the specific
disclosure forms in each state, and just directly extract the most meaningful
parts of the filing.

We want to make it easy for people to do manipulations on top of this data,
while ensuring that this system itself does as little manipulation as possible
to the underlying data from reports filed. For instance, many records include
Person entities - these are deterministically extracted from just the available
filing data, e.g. an address, employer, occupation and name are all extracted
for each contribution. Deduplication can then happen with each of these
entities, but they are themselves totally reproducible from just the filing
information.

This model entails that Filings have Sections - a Filing can, and often will,
have multiple Sections. As much of the specific logic as possible should be
pushed down into Sections, which offer flexibility by allowing us to compose
them together to reproduce the data from state-specific reports. We can model
a particular state filing form as a Filing with a specific set of expected
Sections to be present. Some attributes that might make sense as properties of a
Filing, such as Amendments, are here presented as Sections; the line between the
two is muddy, but this proposal tries to keep Filings as minimal as possible.

Finally, the different entity types presented here present either current or
likely future conflicts with other entities in the Open Civic Data namespace, so
this proposal doesn't make any attempt to resolve those conflicts since they
seem ancillary for now.

Questions to answer
-------------------
* How to model Committee Status and Committee Purpose inside of OCD Organization
  models?
      Just add additional fields for those. Not sure why this was ever a question.
* How to reconcile multiple reports that describe the same contribution,
  expenditure or other event?
      Same transactions should have same IDs. Multiple filings can point to one
      transaction. How to handle this for jurisdictions where no transaction IDs
      are provided by the regulator will be...very dependent on that jurisdiction.
* How should amendments work? Should there be some notion of versions of
  filings? Should all data from a given filing, even if 99% is redundant with a
  prior version of same filing, be stored, or should we store a diff?
      We should use filings and filing_actions for this. The implementing
      system is responsible for determining what's current, using the is_current
      and supersedes_prior_versions fields of the Filing filing_action.
* Should we make/preserve the distinction FEC makes between contributions and
  receipts (every contribution is a receipt; not every receipt is a
  contribution)? How do we handle presumably-unique transaction IDs that
  nevertheless have to get versioned somehow?
      This is handled acceptably by Transactions and specifically,
      the classification field. Versioning is tricky - we could pack it into the
      transaction ID somehow; or use the filing_action; or not care about
      versions at all and just represent the current state of the world. I vote
      for using the filing_action for this - makes it easy to find all versions
      of a given transaction, and does the least-weird thing.

Implementation
==============

Campaign Finance Filing
-----------------------

id
    Open Civic Data-style ID in the format
    ``ocd-campaign-finance-filing/{{uuid}}``.

identifiers
    **optional**
    Upstream IDs of the disclosure if any exist, such as the filing ID assigned
    by the Senate Office of Public Record.

classification
    **optional**
    Filing Type (jurisdiction-specific).

filer
    Committee making the Filing.

coverage_start_date
    **optional**
    Date when filing period of coverage begins.

coverage_end_date
    **optional**
    Date when filing period of coverage ends.

recipient
    OCD Organization indicating the regulator to which the Filing was submitted.

sources
    **optional**
    **repeated**
    List of sources used in assembling this object. Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

actions
    A list of objects representing individual actions that take place on a
    filing, such as initial filing, amendments, withdrawals, etc. Actions
    consist of the following properties:

    id
        Open Civic Data-style ID in the format
        ``ocd-campaign-finance-filing-action/{{uuid}}``.

    description
        Description of the action.

    date
        The date the action occurred.

    classification
        **repeated**
        A list of classifications for this action, such as "amendment" or
        "revocation" - allows for consolidating different jurisdictional
        amendment schemes into standard types.

    agent
        **optional**
        **repeated**
        Person responsible for the action, usually the filer of the amendment or
        withdrawal. Theoretically this could be an Organization of some kind as
        well.

    supersedes_prior_versions
        Boolean indicating whether this action renders everything contained
        in previous versions of this Filing invalid.

    transactions
        List of the Transactions attached to this version of the Filing.

    is_current
        Boolean indicating whether data from this action (primarily the
        transaction list) should be considered current or not.

totals
    **optional**
    **repeated**
    A list of totals or other aggregations reported in this filing, often summing up different
    sections. These can sometimes be correctly imputed from the transactions associated with this
    filing.

    description
        String containing a description of the total.

    value
        Actual decimal amount of transaction.

    currency
        Currency denomination of transaction.

designation
    **repeated**
    **optional**
    Election(s) or other jurisdictionally-specific events relevant to this filing. This is the
    upcoming Election for which a donation is being disclosed; a recently-passed Election
    for which a Committee is announcing the closing of its books; an inauguration for which campaign
    funds can be used; or some other event or cause for which this filing is being generated. The
    exact nature of these will depend on the jurisdiction, but the intent is for referring to, say,
    a specific year's party primary in a jurisdiction or that party's inauguration festivities.

created_at
    Time that this object was created at in the system, not to be confused with the date of introduction.
updated_at
    Time that this object was last updated in the system, not to be confused with the last action.
extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.


Committee
---------

Subclass of Popolo Organization.

id
    Open Civic Data-style ID in the format
    ``ocd-campaign-finance-committee/{{uuid}}``.

committee_type
    Type of the Committee, as a string. Presumably unique within the namespace of this Committee's
    geographic area (opengov:area).

statuses
    Current status of the Committee. List of date ranges and status types
    (active, inactive, contesting election, not contesting election, etc)
    describing the time period at which a given status applied to the Committee.

    start_date
        First date at which the status applied (inclusive).

    end_date
        **optional**
        Last date at which the status applied (inclusive). In many cases, the
        current status won't have a known end_date associated with it, so this
        is optional to reflect that.

    note
        Description of the status.

    classification
        **repeated**
        A list of classifications for this status, such as "active" or
        "contesting election" - allows for consolidating different
        jurisdictional status schemes into standard types.

candidacy_designations
    **optional**
    **repeated**
    List of the candidacies for which the committee has declared a position (e.g., support or oppose) or has otherwise focused its activity. Has the following properties:

    candidacy_id
        Reference to an OCD ``Candidacy``.

    designation
        Enumerated among "supports", "opposes", "primary vehicle for", "surplus account for", "independent expenditure" and other relationship types.

ballot_measure_options_supported
    **optional**
    **repeated**
    List of the ballot measure contests in which the committee has declared support for a specific option. Has the following properties:

    ballot_measure_contest_id
        Reference to an OCD ``BallotMeasureContest``.

    option
        The specific ballot measure option supported by the committee, which are enumerated in ``BallotMeasureContest.options``.


Candidate Designation
---------------------

A Committee may have no relation to any specific Candidate, but if they do have
such a relationship, the options are complex. Hence this type.

id
    Open Civic Data-style ID in the format ``ocd-campaignfinance-candidateorientation/{{uuid}}``

candidate
    OCD Person indicating the candidate

designation
    Enumerated among "supports", "opposes", "primary vehicle for", "surplus
    account for", "independent expenditure" and other relationship types.

Person
------

This system assumes that each Person will be generated from a specific line item
in a Filing. As such, we may know nothing about the Person but their name. Also,
sometimes and as far as I can see inevitably, some Persons (many in fact) will
be corporations or other distinctly non-human entities, Supremes Court
notwithstanding.

This type is an OCD Person.

Filing Type
-----------

id
    Open Civic Data-style ID in the format
    ``ocd-campaign-finance-filing-type/{{uuid}}``.

name
    Name of filing type - "Last Minute Contributions", etc.

code
    Code for the form associated with the Filing - "A1", etc.

jurisdiction
    OCD Jurisdiction for which the Filing Type is relevant.

Transaction (Section)
---------------------

id
    Open Civic Data-style ID in the format
    ``ocd-campaign-finance-transaction/{{uuid}}``.

filing_action
    Reference to the ``Filing.action.id`` that a transaction is reported in.

identifier
    **optional**
    In some jurisdictions, the original jurisdictionally-assigned ID of a
    Transaction may be meaningful, so preserve it here.

sources
    **optional**
    **repeated**
    List of sources used in assembling this object. Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

classification
    Type of transaction - contribution, expenditure, loan, transfer, other
    receipt, etc. Enumerated field based on the jurisdiction of the Committee
    filing the Transaction.

amount
    Amount of transaction. This amount may be negative, often to indicate a returned contribution,
    but in such cases the is_rejected field should be omitted to avoid ambiguity.

    value
        Actual decimal amount of transaction.

    currency
        Currency denomination of transaction.

    is_in_kind
        Boolean indicating whether transaction is in-kind or not (in which case,
        it's probably cash).

    is_rejected
        **optional**
        Boolean indicating whether transaction has been rejected by the recipient (for example, a
        returned contribution).

sender
    This can be a person or some kind of organization or committee.

    entity_type
        Indicates whether this is an "organization" or "person".

    organization
        OCD Organization committing ("sending") this transaction (only if
        entity_type is "organization").

    person
        OCD Person making contribution, or paying for expenditure, etc. (only if
        entity_type is "person").

recipient
    This can be a person or some kind of organization or committee.

    entity_type
        Indicates whether this is an "organization" or "person".

    organization
        OCD Organization receiving this transaction (only if entity_type is
        "organization").

    person
        OCD Person receiving contribution, or being paid for an expenditure, etc.
        (only if entity_type is "person").

date
    **optional**
    Date reported for transaction.

notes
    **repeated**
    Strings containing notes, descriptions and other miscellaneous bits of text attached to this
    transaction.

Committee Attribute Update (Section)
------------------------------------

This includes updates in which committees are becoming active, inactive or
indicating whether they're participating in the Election or not.

id
    Open Civic Data-style ID in the format
    ``ocd-campaign-finance-committee-attribute-update/{{uuid}}``.

property
    Attribute in the Committee object to change.

value
    Value to set for the attribute in the Committee object.

description
    String containing whatever associated text we got along with the attribute
    change.

filing_action
    Reference to the ``Filing.action.id`` that an update is reported in.
