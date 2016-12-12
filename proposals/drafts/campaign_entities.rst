====================
OCDEP: Campaign Entities
====================

:Created: 
:Author: Abraham Epton
:Status: Draft

Overview
========

Definition of the ``Candidate`` and ``Election`` types and associated other
types to model campaign finance filings with a regulator. Supplements Campaign
Finance Filings proposal.

Definitions
-----------

Campaign Finance regulator
    Any government agency (Regulator) in charge of gathering information and
    enforcing transparency laws against political committees (Committees).

Person
    The Person entity here will refer to many entities that are actually
    corporations or other nonhuman entities. It's meant to refer to whoever or
    whatever is taking a specific action, or having an action disclosed in which
    they're involved. It will mostly be people but not always, and as lovely as
    it would be to have some way to disambiguate the two I'm not optimistic that
    will be possible anytime soon.

Rationale
=========

In order to model campaign finance disclosures, we need some notion of who is
running for which office, and in which election. This runs up against other
domains with interest in similar topics, and so discussion of these types is
moved out of the campaign finance domain for general critique and improvement.

Implementation
==============

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

Jurisdiction
------------

Uses the proposal from OCDEP 3.

Office
------

OCD Post model.

Party
-----

OCD Organization model.