====================
OCDEP: Campaign Finance Filings
====================

:Created: 
:Author: Abraham Epton
:Status: Draft

Overview
========

Definition of the ``Filing`` type and associated other types to model campaign
finance filings with a regulator.

Definitions
-----------

Campaign Finance regulator
    Any government agency (Regulator) in charge of gathering information and
    enforcing transparency laws against political committees (Committees).

Filing
    Any single document filed with a Regulator.

Government Level
    The most common of these will be "state", "federal" and "city" or perhaps
    "local". But this allows for a distinction between city and county
    authorities, or federal and tribal.

Jurisdiction
    The region covered by an Office, or for which an Election is being held.

Person
    The Person entity here will refer to many entities that are actually
    corporations or other nonhuman entities. It's meant to refer to whoever or
    whatever is taking a specific action, or having an action disclosed in which
    they're involved. It will mostly be people but not always, and as lovely as
    it would be to have some way to disambiguate the two I'm not optimistic that
    will be possible anytime soon.

Section
    A container for a unit of meaning inside a Filing, that isn't inherent to
    the basic process of filing a document with an agency.

Rationale
=========

Political committees file statements with their regulators in order to disclose
funders, expenditures, organizational ties and other financial details.
Filings encapsulate some number of possible specific disclosures, and some
filings can contain more than one type of disclosure, so this proposed option is
to consider each actual filing as an object and then each specific disclosed
piece of information as associated with that object. So a CommitteeNameChange
would be associated with a Filing, along with a CommitteeAddressChange and a
CommitteeOfficerAddition. A series of CommitteeContributions and
CommitteeExpenses would be attached to one Filing. This way we don't need to
model the specific disclosure forms in each state, and just directly extract
the most meaningful parts of the filing.

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

TODO
----
* Make filing activity actions use same pattern as OCD bill actions (@aepton)

Questions to answer
-------------------
* How to model Committee Status and Committee Purpose inside of OCD Organization
  models?
* How to reconcile multiple reports that describe the same contribution,
  expenditure or other event?
* How to handle different types of Committees beyond just imputing their types
  based on (say) whether they are oriented toward more than one Candidate?
* How should amendments work? Should there be some notion of versions of
  filings? Should all data from a given filing, even if 99% is redundant with a
  prior version of same filing, be stored, or should we store a diff?
* Should we make/preserve the distinction FEC makes between contributions and
  receipts (every contribution is a receipt; not every receipt is a
  contribution)? How do we handle presumably-unique transaction IDs that
  nevertheless have to get versioned somehow?

Implementation
==============

Filing
------

id
    Open Civic Data-style id in the format ``ocd-cf-filing/{{uuid}}``

filing_type
    **optional**
    Filing Type (jurisdiction-specific)

filing_committee
    Committee

filing_date
    Date (and possibly time) when filing was submitted.

filing_coverage_begin_date
    **optional**
    Date (and possibly time) when filing period of coverage begins.

filing_coverage_end_date
    **optional**
    Date (and possibly time) when filing period of coverage ends.

from_organization
    Regulator to which the Filing was submitted.

filing_url
    **optional**
    Wish it wasn't optional.

sources
    **optional**
    **repeated**
    List of sources used in assembling this object. Has the following
    properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

filing_relevant_election_date
    Date of (nearest? next?) relevant election.

filing_person
    **optional**
    Person responsible for the filing.

Committee
---------

id
    Open Civic Data-style id in the format ``ocd-cf-committee/{{uuid}}``

name
    Name of the Committee

committee_type
    Committee Type

candidate orientations
    **optional**
    **repeated**
    What posture the Committee takes towards specific Candidates. Committee type
    can be imputed based on the number and nature of these orientations.

officers
    List of Persons who are the committee officers (maybe needs indication of
    their ranks?)

status
    Current status of the Committee.

purpose
    **optional**
    Purpose of the Committee if any is given.

Committee Type
--------------

id
    Open Civic Data-style id in the format ``ocd-cf-committeetype/{{uuid}}``

name
    Name of the Committee Type

jurisdiction
    Presumably a state, but: whatever jurisdiction the Committe Type is
    meaningful within. This allows us to have "Candidate Committee"s in 2
    different states that adhere to whatever different rules apply in those
    places.

Candidate Orientation
---------------------

A Committee may have no relation to any specific Candidate, but if they do have
such a relationship, the options are complex. Hence this type.

id
    Open Civic Data-style id in the format ``ocd-cf-candidateorientation/{{uuid}}``

candidate
    Candidate

orientation
    Enumerated among "supports", "opposes", "primary vehicle for", "surplus
    account for" and other relationship types.

Person
------

This system assumes that each Person will be generated from a specific line item
in a Filing. As such, we may know nothing about the Person but their name. Also,
sometimes and as far as I can see inevitably, some Persons (many in fact) will
be corporations or other distinctly non-human entities, Supremes Court
notwithstanding.

This type is an OCD Popolo Person.

Regulator
---------

OCD Organization model.

Amendment
---------

Need to figure out how this system should work. It probably shouldn't be a
Section.

Transaction Type
----------------

id
    Open Civic Data-style id in the format ``ocd-cf-transactiontype/{{uuid}}``

name
    Type of transaction - contribution, expenditure, loan, in-kind, transfer,
    other receipt, etc.

Filing Type
----------------

id
    Open Civic Data-style id in the format ``ocd-cf-filingtype/{{uuid}}``

name
    Name of filing type - "Last Minute Contributions", etc.

code
    Probably-more-cryptic code for the form associated with the Filing - "A1",
    etc.

jurisdiction
    Jurisdiction for which the Filing Type is relevant.

Transaction (Section)
---------------------

id
    Open Civic Data-style id in the format ``ocd-cf-transaction/{{uuid}}``

transaction_type
    From enumerated list of possible Transaction Types.

transaction_amount
    Amount in Decimal of transaction.

counterparty
    Person making contribution, or receiving expenditure, etc.

date
    Date reported for transaction.

description
    String (may simply need repeated "notes" fields for items of this type).

memo
    String (may simply need repeated "notes" fields for items of this type).

CommitteeStatusUpdate (Section)
-------------------------------

id
    Open Civic Data-style id in the format ``ocd-cf-committeestatusupdate/{{uuid}}``

new_status
    New status to set for Committee. This could be an enumerated type or a
    free-text field.

description
    String containing whatever associated text we got along with the status
    change.

CommitteeAttributeUpdate (Section)
----------------------------------

id
    Open Civic Data-style id in the format ``ocd-cf-committeeattributeupdate/{{uuid}}``

attribute_to_update
    Attribute in the Committee object to change.

new_attribute_value
    Value to set for the attribute in the Committee object.
