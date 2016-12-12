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
    Open Civic Data-style id in the format ``ocd-cf-committee/{{uuid}}``

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

This system assumes that each Person will be generated from a specific line item
in a Filing. As such, we may know nothing about the Person but their name. Also,
sometimes and as far as I can see inevitably, some Persons (many in fact) will
be corporations or other distinctly non-human entities, Supremes Court
notwithstanding.

id
    Open Civic Data-style id in the format ``ocd-cf-person/{{uuid}}``

first_name
    **optional**
    String

middle_name
    **optional**
    String

last_name
    **optional**
    String

name_prefix
    **optional**
    String

name_suffix
    **optional**
    String

name_full
    Fully-concatenated name with all prefix, suffix, etc

street_address_1
    **optional**
    String

street_address_2
    **optional**
    String

city
    **optional**
    String

state
    **optional**
    String

country
    **optional**
    String

zip
    **optional**
    String

coordinates
    **optional**
    Geocoded address coordinates (WGS 84)

employer
    **optional**
    String

occupation
    **optional**
    String

Contribution (Section)
----------------------

id
    Open Civic Data-style id in the format ``ocd-cf-contribution/{{uuid}}``

is_loan
    Whether the contribution is a loan. (This type of contribution could
    potentially merit its own Section.)

is_inkind
    Whether the contribution is in-kind. (This type of contribution could
    potentially merit its own Section.)

contribution_amount
    Amount in Decimal of contribution.

donor
    Person making contribution.

date
    Date reported for contribution.

description
    String (may simply need repeated "notes" fields for items of this type).

memo
    String (may simply need repeated "notes" fields for items of this type).

Expenditure (Section)
---------------------

id
    Open Civic Data-style id in the format ``ocd-cf-expenditure/{{uuid}}``

is_transfer
    Whether this expenditure is a transfer to another committee. (This type of
    expenditure could potentially merit its own Section.)

amount
    Amount in Decimal of expenditure.

vendor
    Person receiving expenditure.

date
    Date reported for expenditure.

description
    String (may simply need repeated "notes" fields for items of this type).

memo
    String (may simply need repeated "notes" fields for items of this type).

Amendment (Section)
-------------------

id
    Open Civic Data-style id in the format ``ocd-cf-amendment/{{uuid}}``

filing_to_amend
    Filing

invalidates_prior_finding
    Whether this amendment renders all content in the filing_to_amend invalid
    (which is almost always the case IMHO) or merely appends to it or somesuch.

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

Candidate
---------

This is not necessarily a Person: for instance, "yes" or "no" to a ballot
measure.

id
    Open Civic Data-style id in the format ``ocd-cf-candidate/{{uuid}}``

election
    Election this Candidate is contesting.

party
    **optional**
    Party this Candidate is aligned with.

office
    Office for which this Candidate is running.

regulator
    **repeated**
    **optional**
    Any applicable Regulators who have jurisdiction over this Candidate. For
    example, FEC and PDC have jurisdiction over different candidates in WA
    on a given election day. I suppose it's possible some Candidates won't have
    Regulators (God help us all).

Jurisdiction
------------

id
    Open Civic Data-style id in the format ``ocd-cf-jurisdiction/{{uuid}}``

name
    Name to use for this Jurisdiction.

geography
    **optional**
    Geography object containing the boundaries of this Jurisdiction. Reluctantly
    optional.

government_level
    **repeated**
    Government Level with...jurisdiction over this Jurisdiction.

Office
------

id
    Open Civic Data-style id in the format ``ocd-cf-office/{{uuid}}``

name
    Name of the Office.

government_level
    Government Level that this Office belongs to.

Party
-----

id
    Open Civic Data-style id in the format ``ocd-cf-party/{{uuid}}``

name
    Name of the Party.

Regulator
---------

id
    Open Civic Data-style id in the format ``ocd-cf-regulator/{{uuid}}``

name
    Name of the Regulator.

url
    **optional**
    URL associated with the Regulator; this should probably either not be part
    of the spec, or associated with a much more rigorous system of URL prefixes
    for different report types, etc.

government_level
    Government Level that this Regulator belongs to.

Election
--------

id
    Open Civic Data-style id in the format ``ocd-cf-election/{{uuid}}``

date
    Date of the Election.

jurisdiction
    Jurisdiction with at least one race occurring on this Election date.

is_primary
    Whether this Election is a primary race or not for this Jurisdiction.

primary_parties_involved
    **repeated**
    **optional**
    If this is a primary, each Party involved in this Election.

GovernmentLevel
---------------

id
    Open Civic Data-style id in the format ``ocd-cf-governmentlevel/{{uuid}}``

name
    Name of the Government Level.
