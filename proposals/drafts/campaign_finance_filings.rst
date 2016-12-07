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


Implementation
==============

Filing
------

id
    Open Civic Data-style id in the format ``ocd-cf-filing/{{uuid}}``

filing_type
    FilingType (jurisdiction-specific)

filing_committee
    FilingCommittee

filing_date
    Date (and possibly time) when filing was submitted.

filing_coverage_begin_date
    **optional**
    Date (and possibly time) when filing period of coverage begins.

filing_coverage_end_date
    **optional**
    Date (and possibly time) when filing period of coverage ends.

FilingCommittee
---------------

id
    Open Civic Data-style id in the format ``ocd-cf-filingcommittee/{{uuid}}``

name
    Name of the Committee

candidate
    If Committee is a candidate committee, this is the Candidate; if not a
    candidate committee, this field is null

officers
    list of CommitteeOfficers

CommitteeContribution
---------------------

id
    Open Civic Data-style id in the format ``ocd-cf-committeecontribution/{{uuid}}``

filing
    Filing

filing_date
    Date (and possibly time) when filing was submitted.

is_loan
    Whether the contribution is a loan.

contribution_amount
    Amount in Decimal of contribution.