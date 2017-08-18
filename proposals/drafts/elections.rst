====================
OCDEP: Elections
====================

:Created: 2016-12-28
:Author: James Gordon, Forest Gregg, `California Civic Data Coalition`_
:Status: Proposed

Overview
========

Definition of data types to model elections, candidacies for public office and ballot measures.

The proposed data types are:

* ``Election`` [#]_
* ``Contest``, a base class for:

    - ``BallotMeasureContest``
    - ``CandidateContest``
    - ``PartyContest``
    - ``RetentionContest``

* ``Candidacy``

Supplements the :doc:`Campaign Finance Filings <campaign_finance_filings>` proposal prepared by Abraham Epton, and lays the foundation for a future proposal covering election results.

Definitions
===========

Ballot Measure
    A proposition or question with two or more predetermined options put before voters in an election. These include:

    * The enactment or repeal of a statute, constitutional amendment or other form of law.
    * Approval or rejection of a new tax or additional spending of public funds.
    * The recall or retention of a previously elected public office holder.

Candidacy
    The condition of a person being a candidate. A single person may have multiple candidacies if:

    * The person competed in multiple elections, even for the same office term. This includes a candidate in an initial or "primary" election who advances to be a candidate in the "general" election.
    * The person competed to hold multiple public offices, even in the same election.
    * The person was elected to serve a term in a public office and later sought re-election to the same public office.

Candidate
    A person competing to serve a term in a public office.

Contest
    A specific decision with a set of predetermined options put before voters in an election. These contests include:

    * Selecting candidates to hold public offices.
    * Selecting options set forth in a ballot measure.
    * Selecting a preferred political party to hold power.

Election
    A collection of political contests held within a political geography that are decided in parallel through a process of compiling official ballots cast by voters and adding up the total votes for each option in each contest.

Election Day
    The final or only date when eligible voters may cast their ballots in an election. Typically this is also the same date when results of the election's contests are first publicly reported.

Incumbent
    The candidate for a public office who also currently holds that public office. Also applies to the political party that currently holds majority power.

Office Term
    The interval in which an elected candidate is expected to retain a public office before being re-elected or replaced.

    For a variety of reasons, an office holder may vacate an elected office before serving a full term. This is known as an "unexpired term", a situation which could require an additional contest (known as a "Special Election" in U.S. politics) to fill the empty public office.

Party
    A political organization to which public office holders and candidates can be affiliated. In some electoral systems, such as `party-list proportional representation`_, voters may also directly elect political parties to hold power in lieu of or in addition to voting for specific candidates endorsed by the political party.

Public Office
    A position within a governmental body which is filled through an election contest.

Runoff Contest
    A contest conducted to decide a previous contest in which no single option received the required number of votes to decide the contest.

Ticket
    Two or more allied candidates competing together in the same contest where multiple related public offices are at stake. For example, in U.S. politics, candidates for President and Vice President run together on the same ticket, with the President at the top of the ticket.

    Note that candidates on the same ticket are not necessarily affiliated with the same political party.

Write-in
    A vote in a contest wherein the voter explicitly names a preferred option for an election contest, rather than choosing from among the predetermined options listed on the ballot.


Rationale
=========

Elections are a primary focal point of civic activity in which eligible voters cast ballots to determine the outcome of political contests, including:

* Who should hold a public office?
* Should a proposed change of law be implemented?

Modeling the potential outcomes of these contests is a service to voters who may cast their ballots in an impending election. Modeling the contests' actual outcomes legitimizes the election's results and enables historical electoral analysis.

This proposal is submitted in response to on-going discussion around a related OCDEP focused on campaign finance disclosures. Representing elections and their contests is necessary for modeling these disclosures because they reveal money raised and spent in support or opposition to specific candidates and ballot measures. However, since notions of elections and their contests run up against other domains, we've separated the definition of these types.

The goal of this proposal is to cover the use cases related to the campaign finance domain while laying the foundation for models that will include election results (to be covered in a future OCDEP).

Our use cases require unique representations of both previous elections and contests as well as pending elections and contests. While honoring these requirements, we also aim for consistency with the Voting Information Project's `XML format specification`_ so as to support a high degree of interoperability with that existing data standard.

VIP 5, the specification's current version, incorporates elements from the `Election Results Common Data Format Specification`_ defined by the National Institute of Standard and Technology. As such, we have borrowed eagerly from NIST's current specification also.

Differences from VIP
--------------------

The three major differences are:

1. VIP models a single election, whereas this proposal intends to model previous and pending elections. As such, certain OCD data types are independent of and linked to multiple elections and/or election contests, unlike their corresponding VIP elements. 
2. VIP models precise details about ballots, including the exact wording and order of the options (VIP refers to these as "selections") presented to voters in a given jurisdiction. These details are beyond the scope of this proposal.
3. VIP models details about polling locations, including their addresses and hours. These details are also beyond the scope of this proposal.

Important differences between the proposed OCD data type and its corresponding VIP element, if any, are noted in each data type's "Mapping to VIP" subsection in Implementation_.

Additionally, VIP describes `<InternationalizedText>`_ and `<LanguageString>`_ elements for the purposes of representing certain texts in multiple languages, e.g., the English and Spanish translations of the ``support_statement`` and ``oppose_statement`` of a ``BallotMeasureContest``. These are treated as strings in this proposal.

Implementation
==============

Election
--------

A collection of political contests set to be decided on the same date within a Division.    

id
    Open Civic Data-style id, in the format ocd-election/{{uuid}}.

name
    Name of the election.

date
    Final or only date when eligible voters may cast their ballots in the Election. Typically this is also the same date when results of the election's contests are first publicly reported.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the election, such as those assigned by a Secretary of State, county or city elections office.

    Each element in identifiers is an object with the following keys:

    scheme
        The name of the service that created the identifier.
    identifier
        A unique identifier developed by an upstream or third party source.

division_id
    Reference to the OCD ``Division`` that defines the broadest political geography of any contest to be decided by the election. For example, an election that includes a contest to elect the governor of California would include the division identifier for the entire state of California.

administrative_organization_id
    **optional**
    Reference to the OCD ``Organization`` that administers the election and publishes the official results.

sources
    **optional**
    **repeated**
    List of sources used in assembling this object. Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.


Sample Election
+++++++++++++++


.. code:: javascript

    {
        "id": "ocd-election/4c25d655-c380-46a4-93d7-28bc0c389629",
        "name": "2016 GENERAL",
        "date": "2016-11-08",
        "identifiers": [
            {
                "scheme": "calaccess_election_id",
                "identifier": "65"
            }
        ],
        "division_id": "ocd-division/country:us/state:ca/",
        "administrative_organization_id": "ocd-organization/436b4d67-b5aa-402c-9e20-0e56a8432c80",
        "created_at": "2017-02-07T07:17:58.874Z",
        "updated_at": "2017-02-07T07:17:58.874Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-08",
                "url": "http://cal-access.ss.ca.gov/Campaign/Candidates/list.aspx?view=certified&electNav=65"
            },
            {
                "note": "Last scraped on 2017-02-07",
                "url": "http://cal-access.ss.ca.gov/Campaign/Measures/list.aspx?session=2015"
            }
        ],
        "extras": {"calaccess_election_type": ["GENERAL"]},
    }


Mapping to VIP
++++++++++++++

``Election`` corresponds to VIP's `<Election>`_ element.

* Important differences between corresponding fields:

    - ``<Name>`` is not required on VIP's ``<Election>`` but is required in OCD.
    - ``<StateId>``, which is a required reference to a VIP `<State>`_ element, should map to an equivalent OCD ``division_id`` if ``<IsStatewide>`` is ``true``. Otherwise, ``division_id`` should reference the appropriate subdivision of the equivalent to ``<StateId>``.

* OCD fields not implemented in VIP:

    - ``administrative_organization_id`` is an optional reference to an OCD ``Organization`` that's equivalent to the ``<Department>`` tag in VIP's `<ElectionAdministration>`_ element.

* VIP fields not implemented in this OCDEP:

    - ``<ElectionType>``, which is optional for describing either the level of government to which a candidate might be elected (e.g., "federal", "state", "county", etc.) or the point when the election occurs in the overall cycle (e.g., "general", "primary", "runoff" and "special").
    - ``<HoursOpenId>``, which is an optional reference to a VIP `<HoursOpen>`_ element that represents when polling locations for the election are generally open.
    - ``<RegistrationInfo>``, which optional text.
    - ``<RegistrationDeadline>``, which is an optional date.
    - ``<HasElectionDayRegistration>``, which is an optional boolean.
    - ``<AbsenteeBallotInfo>``, which is optional text.
    - ``<AbsenteeRequestDeadline>``, which is an optional date.
    - ``<ResultsUri>``, which is optional.


Contest
-------

A base class for representing a specific decision set before voters in an election. Includes properties shared by all contest types: ``BallotMeasureContest``, ``CandidateContest``, ``PartyContest`` and ``RetentionContest``.

id
    Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the contest, such as those assigned by a Secretary of State, county or city elections office.

    Each element in identifiers is an object with the following keys:

    scheme
        The name of the service that created the identifier.
    identifier
        A unique identifier developed by an upstream or third party source.

name
    Name of the contest, not necessarily as it appears on the ballot (string).

division_id
    Reference to the OCD ``Division`` that defines the political geography of the contest, e.g., a specific Congressional or State Senate district. The ``Division`` referenced by each ``Contest`` should be a subdivision of the ``Division`` referenced by the contest's ``Election``.

election_id
    Reference to the OCD ``Election`` in which the contest is decided.

created_at
    Time that this object was created at in the system.

updated_at
    Time that this object was last updated in the system.

sources
    **optional**
    **repeated**
    List of sources used in assembling this object. Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.


Sample Contest
++++++++++++++


.. code:: javascript

    {
        "id": "ocd-contest/eff6e5bd-10dc-4930-91a0-06e2298ca15c"
        "identifiers": [],
        "name": "STATE SENATE 01",
        "division_id": "ocd-division/country:us/state:ca/sldu:1",
        "election_id": "ocd-event/4c25d655-c380-46a4-93d7-28bc0c389629",
        "created_at": "2017-02-07T07:18:05.438Z",
        "updated_at": "2017-02-07T07:18:05.442Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-08",
                "url": "http://cal-access.ss.ca.gov/Campaign/Candidates/list.aspx?view=certified&electNav=65"
            }
        ],
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``Contest`` corresponds to VIP's `<ContestBase>`_ element.

* Important differences between corresponding fields:

    - ``<ElectoralDistrictId>``, which is an optional reference to a VIP `<ElectoralDistrict>`_ element, can map to an equivalent OCD ``division_id``.

* OCD fields not implemented in VIP:

    - ``election_id`` is a required reference to an OCD ``Election``.

* VIP fields not implemented in this OCDEP:

    - ``<Abbreviation>``, which is optional text.
    - ``<BallotSelectionIds>`` is an optional single element that contains a set of references to each selection (i.e., any extension of VIP's `<BallotSelectionBase>`_) on any ballot that includes the contest. This proposal instead represents the distinct options for each contest across all versions of the ballot.
    - ``<ElectorateSpecification>``, which optional text.
    - ``<HasRotation>``, which is an optional boolean.
    - ``<BallotSubTitle>``,  which is optional text.
    - ``<BallotTitle>``,  which is optional text.
    - ``<SequenceOrder>``,  which is an optional integer.
    - ``<VoteVariation>``,  which is an optional reference to a VIP `<VoteVariation>`_.
    - ``<OtherVoteVariation>``, which is optional text.


BallotMeasureContest
--------------------

A contest in which voters select from among options proposed in a ballot measure.

``BallotMeasureContest`` inherits all the required and optional properties of ``Contest``.

options
    **repeated**
    List of the options voters may choose, e.g., "yes", "no", "recall", "no recall" (two or more required).

description
    **optional**
    Text describing the purpose and/or potential outcomes of the ballot measure, not necessarily as it appears on the ballot (string).

requirement
    **optional**
    The threshold of votes the ballot measure needs in order to pass (string). The default is a simple majority, i.e., "50% plus one vote". Other common thresholds are "three-fifths" and "two-thirds".

classification
    **optional**
    Describes the origin and/or potential outcome of the ballot measure, e.g., "initiative statute", "legislative constitutional amendment" (string).

runoff_for_contest_id
    **optional**
    If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that ``BallotMeasureContest``.


Sample BallotMeasureContest
+++++++++++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-contest/2ce7e19b-3feb-4318-9908-eb3fdf456fb0",
        "identifiers": [
            {
                "scheme": "calaccess_measure_id",
                "identifier": "1376195"
            }
        ],
        "name": "PROPOSITION 060- ADULT FILMS. CONDOMS. HEALTH REQUIREMENTS. INITIATIVE STATUTE."
        "division_id": "ocd-division/country:us/state:ca",
        "election_id": "ocd-event/4c25d655-c380-46a4-93d7-28bc0c389629",
        "created_at": "2017-02-07T07:17:59.818Z",
        "updated_at": "2017-02-07T07:17:59.818Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-07",
                "url": "http://cal-access.ss.ca.gov/Campaign/Measures/Detail.aspx?id=1376195&session=2015"
            }
        ],
        "extras": {},
        "options": [
            "yes",
            "no"
        ],
        "description": "Requires adult film performers to use condoms during filming of sexual intercourse. Requires producers to pay for performer vaccinations, testing, and medical examinations. Requires producers to post condom requirement at film sites. Fiscal Impact: Likely reduction of state and local tax revenues of several million dollars annually. Increased state spending that could exceed $1 million annually on regulation, partially offset by new fees",
        "requirement": "50% plus one vote",
        "classification": "initiative statute",
        "runoff_for_contest_id": null
    }


Mapping to VIP
++++++++++++++

``BallotMeasureContest`` corresponds to VIP's `<BallotMeasureContest>`_ element.

* Important differences between corresponding fields:

    - ``<PassageThreshold>`` maps to ``requirement``.
    - ``<Type>``, which is an optional reference to a VIP `<BallotMeasureType>`_ maps to ``classification`` which is a simple string.

* OCD fields not implemented in VIP:

    - ``options`` should list the distinct selections across all ballots that include the ballot measure (i.e., the distinct ``<Selection>`` tags in the `<BallotMeasureSelection>`_ element).

* VIP fields not implemented in this OCDEP:

    - ``<ConStatement>``, which is optional text.
    - ``<ProStatement>``, which is optional text.
    - ``<EffectOfAbstain>``, which is optional.
    - ``<FullText>``, which is optional text.
    - ``<SummaryText>``, which is optional text.
    - ``<InfoUri>``, which is optional.
    - ``<OtherType>``, which is optional text.


CandidateContest
----------------

A contest among candidates seeking election to one or more public offices. 

``CandidateContest`` inherits all the required and optional properties of ``Contest``.

posts
    **repeated**
    List of references to each OCD ``Post`` representing a public office for which the candidates in the contest are seeking election. Requires at least one. Has the following properties:

    post_id
        Reference to an OCD ``OfficeTerm``.

    sort_order
        **optional**
        Useful for sorting for contests where two or more public offices are at stake, e.g., in a U.S. presidential contest, the President post would have a lower sort order than the Vice President post.

party_id
    **optional**
    If the contest is among candidates of the same political party, e.g., a partisan primary election, reference to the OCD ``Organization`` representing that political party.

previous_term_unexpired
    Indicates the previous public office holder vacated the post before serving a full term (boolean).

number_elected
    Number of candidates that are elected in the contest, i.e. 'N' of N-of-M (integer). Default is 1.


runoff_for_contest_id
    **optional**
    If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that ``CandidateContest``.


Sample CandidateContest
+++++++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-contest/eff6e5bd-10dc-4930-91a0-06e2298ca15c",
        "identifiers": [],
        "name": "STATE SENATE 01",
        "division_id": "ocd-division/country:us/state:ca/sldu:1",
        "election_id": "ocd-event/4c25d655-c380-46a4-93d7-28bc0c389629",
        "created_at": "2017-02-07T07:18:05.438Z",
        "updated_at": "2017-02-07T07:18:05.442Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-08",
                "url": "http://cal-access.ss.ca.gov/Campaign/Candidates/list.aspx?view=certified&electNav=65"
            }
        ],
        "extras": {},
        "posts": [
            {
                "post": "ocd-post/f204b117-24af-42fd-a3fc-c5772533fdf5",
                "sort_order": 0
            }
        ],
        "previous_term_unexpired": false,
        "number_elected": 1,
        "party_id": null,
        "runoff_for_contest_id": null
    }


Mapping to VIP
++++++++++++++

``CandidateContest`` corresponds to VIP's `<CandidateContest>`_ element.

* Important differences between corresponding fields:

    - ``<OfficeIds>``, which is an optional set of references to VIP `<Office>`_ elements, correpsonds to ``posts``. Each ``<OfficeId>`` should map to an equivalent OCD ``Post`` and the order in which the ``<OfficeIds>`` are listed should be preserved in ``sort_order``.
    - ``<PrimaryPartyIds>`` is an optional set of references to each `<Party>`_ related to the contest. This proposal allows for a ``CandidateContest`` to be linked to a single equivalent OCD ``Organization``.
    - ``<NumberElected>`` is an optional integer in VIP but is required in OCD, where it defaults to 1.

* OCD fields not implemented in VIP:

    + ``previous_term_unexpired`` should be ``true`` if the ``<OfficeTermType>`` referenced by the ``<Term>`` tag in VIP's `<Office>`_ element is "unexpired-term". Otherwise, ``previous_term_unexpired`` should be ``false``.
    + ``runoff_for_contest_id`` is optional.

* VIP fields not implemented in this OCDEP:

    - ``<VotesAllowed>``, which is an optional integer.


PartyContest
------------

A contest in which voters can vote directly for a political party.

In these contests, voters can vote for a party in lieu of/in addition to voting for candidates endorsed by that party (as in the case of `party-list proportional representation`_). 

``PartyContest`` inherits all the required and optional properties of ``Contest``.

parties
    **repeated**
    List of references to each party for which a voter could vote in the contest. Requires at list one. Has the following properties:

    party_id
        Reference to an OCD ``Organization``, with the `"party"` classification.

    is_incumbent
        **optional**
        Indicates whether the party currently holds majority power (boolean).

runoff_for_contest_id
    **optional**
    If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that ``PartyContest``.


Sample PartyContest
+++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-contest/eff6e5bd-10dc-4930-91a0-06e2298ca15c",
        "identifiers": [],
        "name": "Elections for the 20th Knesset",
        "division_id": "ocd-division/country:il",
        "election_id": "ocd-event/4c25d655-c380-46a4-93d7-28bc0c389629",
        "created_at": "2017-02-07T07:18:05.438Z",
        "updated_at": "2017-02-07T07:18:05.442Z",
        "sources": [],
        "extras": {},
        "parties": [
            {
                "party_id": "ocd-organization/866e7266-0c21-4476-a7a7-dc11d2ae8cd1",
                "is_incumbent": false
            },
            {
                "party_id": "ocd-organization/b58f698e-a956-4bd5-8ca1-3b46c22c96b4",
                "is_incumbent": true
            },
        ],
        "runoff_for_contest_id": null
    }


Mapping to VIP
++++++++++++++

``PartyContest`` corresponds to VIP's `<PartyContest>`_ element. 

* OCD fields not implemented in VIP:
    
    - ``parties`` should list the distinct party selections across all ballots that include the ``<PartyContest>`` (i.e., each OCD ``Organization`` equivalent to each VIP ``<Party>`` referenced in the ``<PartyIds>`` tag in the `<PartySelection>`_ element).
    - ``runoff_for_contest_id`` an optional field.


RetentionContest
----------------

A contest where voters vote to retain or recall a current office holder.

These contests include judicial retention or recall elections.

``RetentionContest`` inherits all the required and optional properties of ``BallotMeasureContest``.

membership_id
    Reference to the OCD ``Membership`` that represents the tenure of a specific person (i.e., OCD ``Person`` object) in a specific public office (i.e., ``Post`` object).


Sample RetentionContest
+++++++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-contest/d0455060-44ee-4fbf-bc7e-7db86084a11e",
        "identifiers": [
            {
                "scheme": "calaccess_measure_id",
                "identifier": "1256382"
            }
        ],
        "name": "2003 RECALL QUESTION",
        "division_id": "ocd-division/country:us/state:ca",
        "election_id": "ocd-event/3f904160-d304-4753-a542-578cfcb86e76",
        "created_at": "2017-02-07T07:18:00.555Z",
        "updated_at": "2017-02-07T07:18:00.555Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-07",
                "url": "http://cal-access.ss.ca.gov/Campaign/Measures/Detail.aspx?id=1256382&session=2003"
            }
        ],
        "extras": {},
        "requirement": "50% plus one vote",
        "options": [
            "yes",
            "no"
        ],
        "description": "SHALL GRAY DAVIS BE RECALLED (REMOVED) FROM THE OFFICE OF GOVERNOR?",
        "classification": "recall",
        "other_type": "",
        "membership_id": "ocd-membership/181a0826-f458-403f-ae65-e1ce97b8dd34"
    }


Mapping to VIP
++++++++++++++

``RetentionContest`` corresponds to VIP's `<RetentionContest>`_ element.

* Important differences between corresponding fields:

    - ``<CandidateId>``, which is a required reference to a VIP `<Candidate>`_ element, and ``<OfficeId>``, which is an optional reference to a VIP `<Office>`_ element, should map to an equivalent OCD ``Membership`` representing a specific person's (i.e, an OCD ``Person`` object) tenure in a specific public office (i.e., an OCD ``Post`` object).

Candidacy
---------

A person competing in an election contest to hold a specific office for a term.

id
    Open Civic Data-style id in the format ``ocd-candidacy/{{uuid}}``.

person_id
    Reference to an OCD ``Person`` who is the candidate.

post_id
    Reference to the OCD ``Post`` representing the public office for which the candidate is seeking election.

contest_id
    Reference to an OCD ``CandidateContest`` representing the contest in which the candidate is competing.

candidate_name
    **optional**
    For preserving the candidate's name as it was of the candidacy. (string).

filed_date
    **optional**
    Specifies when the candidate filed for the contest (date).

registration_status
    **optional**
    Enumerated among:

    - *filed:* The candidate filed for office but is not qualified.
    - *qualified:* The candidate qualified for the contest.
    - *withdrawn:* The candidate withdrew from the contest (but may still be on the ballot).
    - *write-in:* While the candidate's name did not appear on the ballot, he or she nonetheless campaigned for voter to write in his or her name.

is_incumbent
    **optional**
    Indicates whether the candidate is seeking re-election to a public office he/she currently holds (boolean).

party_id
    **optional**
    Reference to an OCD ``Organzation`` with which the candidate is affiliated.

top_ticket_candidacy_id
    **optional**
    If the candidate is running as part of ticket, e.g., a Vice Presidential candidate running with a Presidential candidate, reference to candidacy at the top of the ticket.

created_at
    Specifies when this object was created in the system (datetime).

updated_at
    Specifies when this object was last updated in the system (datetime).

sources
    **optional**
    **repeated**
    List of sources used in assembling this object. Has the following properties:

    url
        URL of the resource.
    note
        **optional**
        Description of what this source was used for.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.


Sample Candidacy
++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-candidacy/054f0a6e-9c06-4611-8c2c-3e143843c9d8",
        "person_id": "ocd-person/edfafa56-686d-49ea-80e5-64bc795493f8",
        "post": "ocd-post/f204b117-24af-42fd-a3fc-c5772533fdf5",
        "contest_id": "ocd-contest/eff6e5bd-10dc-4930-91a0-06e2298ca15c",
        "candidate_name": "ROWEN, ROBERT J.",
        "filed_date": "2016-03-10",
        "is_incumbent": false,
        "registration_status": "qualified",
        "party_id": "ocd-organization/866e7266-0c21-4476-a7a7-dc11d2ae8cd1",
        "top_ticket_candidacy_id": null,
        "created_at": "2017-02-08T04:17:30.818Z",
        "updated_at": "2017-02-08T04:17:30.818Z",
        "sources": [],
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``Candidacy`` corresponds to VIP's `<Candidate>`_ element.

* Important differences between corresponding fields:
  
    - ``<PartyId>``, which is an optional reference a VIP `<Party>`_ element, can map to an equivalent OCD ``Organization``.
    - ``person_id`` , which is an optional reference a VIP `<Person>`_ element, can map to an equivalent OCD ``Person``.
    - ``<IsTopTicket>``, which is an optional boolean indicating the candidate is the top of a ticket that includes multiple candidates, is replaced by an optional ``top_ticket_candidacy_id``.
    - ``<PreElectionStatus>``, which is an optional reference to a VIP `<CandidatePreElectionStatus>`_ is replaced by an optional ``registration_status``.

* OCD fields not implemented in VIP:
      
    - ``contest_id`` is a required reference to an OCD ``CandidateContest`` which should be the equivalent of the VIP ``<CandidateContest>`` to which the equivalent VIP ``<Candidate>`` is linked.
    - ``committee_id`` is optional.

* VIP fields not implemented in this OCDEP:

    - ``<ContactInformation>`` refers to an element that describes the contact and physical address information for the candidate or their campaign. On and OCD ``Candidacy``, this information would be stored on the associated ``Person`` or ``Committee`` object.
    - ``<PostElectionStatus>``, which is an optional reference to a VIP `<CandidatePostElectionStatus>`_.


Copyright
=========

This document has been placed in the public domain per the `Creative Commons CC0 1.0 Universal license <http://creativecommons.org/publicdomain/zero/1.0/deed>`_.


.. [#] ``Election`` is conceptually similar to a couple of existing OCD data types: 1) ``Event`` which represents a hearing or opportunity for public testimony, as defined in :doc:`../0004`; and 2) ``VoteEvent`` which represents the event of a legislative vote taking place, as defined in :doc:`../0007`. A future OCDEP might define a base class with properties shared by all event-like data types, including a shared id format (e.g., ``ocd-event/{{uuid}}``).

.. _California Civic Data Coalition: http://www.californiacivicdata.org/
.. _party-list proportional representation: https://en.wikipedia.org/wiki/Party-list_proportional_representation
.. _XML format specification: http://vip-specification.readthedocs.io/en/vip5/xml/index.html#elements
.. _Election Results Common Data Format Specification: https://www.nist.gov/itl/voting/nist-election-results-common-data-format-specification
.. _<InternationalizedText>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html
.. _<LanguageString>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html#languagestring
.. _<Election>: <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/election.html
.. _<State>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/state.html
.. _<ElectionAdministration>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/election_administration.html
.. _<HoursOpen>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/hours_open.html 
.. _<ContestBase>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/contest_base.html
.. _<ElectoralDistrict>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/electoral_district.html
.. _<BallotSelectionBase>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_selection_base.html
.. _<VoteVariation>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/vote_variation.html
.. _<BallotMeasureContest>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_contest.html
.. _<BallotMeasureType>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/ballot_measure_type.html#multi-xml-ballot-measure-type
.. _<BallotMeasureSelection>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html
.. _<CandidateContest>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate_contest.html
.. _<Office>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html
.. _<Party>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html
.. _<PartyContest>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party_contest.html
.. _<PartySelection>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html
.. _<RetentionContest>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/retention_contest.html
.. _<Candidate>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html
.. _<CandidatePreElectionStatus>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_pre_election_status.html
.. _<CandidatePostElectionStatus>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_post_election_status.html
.. _<Person>: http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/person.html