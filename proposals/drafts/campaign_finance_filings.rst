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


Implementation
==============

Filing
------

id
    Open Civic Data-style id in the format ``ocd-cf-filing/{{uuid}}``

filing_type
    **optional**
    FilingType (jurisdiction-specific)

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

filing_regulator
    Regulator

filing_url
    **optional**
    Wish it wasn't optional.

filing_relevant_election_date
    Date of (nearest? next?) relevant election.

filing_person
    **optional**
    Person responsible for the filing.

Committee
---------

id
    Open Civic Data-style id in the format ``ocd-cf-filingcommittee/{{uuid}}``

name
    Name of the Committee

candidate
    **optional**
    If Committee is a candidate committee, this is the Candidate; if not a
    candidate committee, this field is null

officers
    List of Persons who are the committee officers (maybe needs indication of
    their ranks?)

status
    Current status of the Committee.

purpose
    **optional**
    Purpose of the Committee if any is given.

Person
------

id

name

first

middle

last

prefix

suffix

full_legal

full_colloquial

address

street_1

street_2

city

state

country

zip

coordinates

employer

occupation

Contribution (Section)
----------------------

id
    Open Civic Data-style id in the format ``ocd-cf-committeecontribution/{{uuid}}``

filing
    Filing

is_loan
    Whether the contribution is a loan.

contribution_amount
    Amount in Decimal of contribution.

is_inkind

donor

date

description

memo

Expenditure (Section)
---------------------

id

filing

is_transfer

amount

vendor

date

description

memo

Amendment (Section)
-------------------

filing_to_amend

invalidates_prior_finding

CommitteeStatusUpdate (Section)
-------------------------------

new_status

description

CommitteeAttributeUpdate (Section)
----------------------------------

attribute_to_update

new_attribute_value

Candidate
---------

election

party

office

regulator

Jurisdiction
------------

id

name

geography

government_level

Office
------

id

name

government_level

Party
-----

id

name

Regulator
---------

id

name

url

government_level

Election
--------

date

jurisdiction

is_primary

primary_parties_involved

GovernmentLevel
---------------

id

name
