====================
OCDEP: Elections
====================

:Created: 2016-12-28
:Author: James Gordon, Forest Gregg, `California Civic Data Coalition <http://www.californiacivicdata.org/>`_
:Status: Proposed

Overview
========

Definition of data types to model elections, candidacies for public office and ballot measures.

The proposed data types are:

* ``Election``
* ``Contest``, a base class for:

    - ``BallotMeasureContest``
    - ``CandidateContest``
    - ``PartyContest``
    - ``RetentionContest``

* ``Candidacy``
* ``OfficeTerm``
* ``Party``

Supplements the "Campaign Finance Filings" proposal prepared by Abraham Epton.

Definitions
===========

Ballot Measure
    A proposition or question with two or more predetermined options that voters may select as part of an election. These include:

    * The enactment or repeal of a statute, constitutional amendment or other form of law.
    * Approval or rejection of a new tax or additional spending of public funds.
    * The recall or retention of a previously elected public office holder.

Candidacy
    The condition of a person being a candidate. A single person may have multiple candidacies if:

    * The person competed to hold multiple public offices, even in the same election.
    * The person was elected to serve a term in a public office and later sought re-election to the same public office.

Candidate
    A person competing to serve a term in a public office.

Contest
    A specific decision with a set of predetermined options put before voters in an election. These contests include:

    * Selecting candidates to serve terms in public offices.
    * Selecting options set forth in a ballot measure.
    * Selecting a preferred political party to hold power.

Election
    A collection of political contests held within a political geography that are decided in parallel through a process of compiling official ballots cast by voters and adding up the total votes for each selection in each contest.

Election Day
    The final or only date when eligible voters may cast their ballots in an election. Typically this is also the same date when results of the election's contests are first publicly reported.

Incumbent
    The candidate for a public office who also currently holds that public office. Also applies to the political party that currently holds majority power.

Office Term
    The interval in which an elected candidate is expected to retain a public office before being re-elected or replaced.

    For a variety of reasons, an office holder may vacate an elected office before serving a full term. This is known as an "unexpired term", a situation which could require an additional contest (known as a "Special Election" in U.S. politics) to fill the empty public office.

Party
    A political organization to which public office holders and candidates can be affiliated. In some electoral systems, such as `party-list proportional representation <https://en.wikipedia.org/wiki/Party-list_proportional_representation>`_, voters may also directly elect political parties to hold power in lieu of or in addition to specific candidates endorsed by the political party.

Public Office
    A position within a governmental body which is filled through an election contest.

Runoff Contest
    A contest conducted to decide a previous contest in which no single option received the required number of votes to decide the contest.

Ticket
    Two or more allied candidates competing together in the same contest where terms in multiple related public offices are at stake. For example, in U.S. politics, candidates for President and Vice President run together on the same ticket, with the President at the top of the ticket.

    Note that candidates on the same ticket are not necessarily affiliated with the same political party.

Write-in
    A vote in a contest wherein the voter explicitly names a preferred selection for an election contest, rather than choosing from among the predetermined selections listed on the ballot.


Rationale
=========

Elections are a primary focal point of civic activity in which eligible voters cast ballots to determine the outcome of political contests, including:

* Who should hold a public office?
* Should a proposed change of law be implemented?

Modeling the potential outcomes of these contests is a service to voters who may cast their ballots in an impending election. Modeling the contests' actual outcomes legitimizes the election's results and enables historical electoral analysis.

This proposal is submitted in response to on-going discussion around a related OCDEP focused on campaign finance disclosures. Representing elections and their contests is necessary for modeling these disclosures because they reveal money raised and spent in support or opposition to specific candidates and ballot measures. However, since notions of elections and their contests run up against other domains, we've separated the definition of these types.

The goal of this proposal is to cover the use cases related to the campaign finance domain while laying the foundation for models that will include election results (to be covered in a future OCDEP).

Our use cases require unique representations of both previous elections and contests as well as pending elections and contests. While honoring these requirements, we also aim for consistency with the Voting Information Project's `XML format specification <http://vip-specification.readthedocs.io/en/vip5/xml/index.html#elements>`_ so as to support a high degree of interoperability with that existing data standard.

VIP 5, the specification's current version, incorporates elements from the `Election Results Common Data Format Specification <https://www.nist.gov/itl/voting/nist-election-results-common-data-format-specification>`_ defined by the National Institute of Standard and Technology. As such, we have borrowed eagerly from NIST's current specification also.

Differences from VIP
++++++++++++++++++++

The two major differences are:

1. VIP models a single election, whereas this proposal intends to model previous and pending elections. As such, certain OCD data types are independent of and linked to multiple elections and/or election contests, unlike their corresponding VIP elements. 
2. VIP models finer details about an election, including where voters can vote and the exact wording of their ballots. These details are beyond the scope of this proposal, which is more focused on representing the distinct election contests and their potential outcomes.

Important differences between the proposed OCD data type and its corresponding VIP element, if any, are noted in each data type's "Mapping to VIP" subsection in Implementation_.

Additionally, VIP describes `<InternationalizedText> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html>`_ and `<LanguageString> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html#languagestring>`_ elements for the purposes of representing certain texts in multiple languages, e.g., the English and Spanish translations of the ``support_statement`` and ``oppose_statement`` of a ``BallotMeasureContest``. In this proposal, these data types are described as simple strings.

Implementation
==============

Election
---------

A collection of political contests set to be decided on the same date within a political geography (aka, ``Division``).

``Election`` is a subclass of OCD's ``Event`` data type, defined in `OCDEP 4: Events <http://opencivicdata.readthedocs.io/en/latest/proposals/0004.html>`_, which was accepted in June 2014. All of the required and optional properties of ``Event`` are inherited by ``Election``. The typical implementation will be an ``all_day`` event with an "election" ``classification`` value and a ``start_time`` set to midnight of the observed election date.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the election if any exist, such as those assigned by a Secretary of State, county or city elections office.

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
        "id": "ocd-event/4c25d655-c380-46a4-93d7-28bc0c389629",
        "identifiers": [
            {
                "scheme": "calaccess_election_id",
                "identifier": "65"
            }
        ],
        "name": "2016 GENERAL",
        "description": "",
        "start_time": "2016-11-08T00:00:00Z",
        "end_time": null,
        "timezone": "US/Pacific",     
        "all_day": true,      
        "classification": "election",
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
        "extras": {},
    }


Mapping to VIP
++++++++++++++

``Election`` corresponds to VIP's `<Election> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/election.html>`_ element.

* Important differences between corresponding fields:

    - ``<Name>`` is not required on VIP's ``<Election>``, but ``name`` (inherited from OCD's ``Event``) is required.
    - ``<StateId>``, which is a required reference to a VIP `<State> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/state.html>`_ element, should map to an equivalent OCD ``division_id`` if ``<IsStatewide>`` is ``true``. Otherwise, ``division_id`` should reference the appropriate subdivision of the equivalent to ``<StateId>``.

* OCD fields not implemented in VIP:

    - ``administrative_organization_id`` is optional.
    - ``description`` (inherited from ``Event``) is optional.
    - ``location`` (inherited from ``Event``) is optional.
    - ``all_day`` (inherited from ``Event``) is optional.
    - ``end_time`` (inherited from ``Event``) is optional.
    - ``status`` (inherited from ``Event``) is optional.
    - ``links`` (inherited from ``Event``) is optional.
    - ``participants`` (inherited from ``Event``) is optional.
    - ``documents`` (inherited from ``Event``) is optional.
    - ``media`` (inherited from ``Event``) is optional.

* VIP fields not implemented in this OCDEP:

    - ``<ElectionType>``, which is an optional string that conflates the level of government to which a candidate might be elected (e.g., "federal", "state", "county", etc.) with the point when the election occurs in the overall cycle (e.g., "general", "primary", "runoff" and "special").
    - ``<HoursOpenId>``, which is an optional reference to a VIP `<HoursOpen> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/hours_open.html>`_ element that represents when polling locations for the election are generally open.
    - ``<RegistrationInfo>``, which is an optional string.
    - ``<RegistrationDeadline>``, which is an optional date.
    - ``<HasElectionDayRegistration>``, which is an optional boolean.
    - ``<AbsenteeBallotInfo>``, which is an optional string.
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
    Upstream identifiers of the contest if any exist, such as those assigned by a Secretary of State, county or city elections office.

name
    Name of the contest, not necessarily as it appears on the ballot (string).

division_id
    Reference to the OCD ``Division`` that defines the political geography of the contest, e.g., a specific Congressional or State Senate district. The ``Division`` referenced by each ``Contest`` should be a subdivision of the ``Division`` referenced by its ``Election``.

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

``Contest`` corresponds to VIP's `<ContestBase> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/contest_base.html>`_ element.

* Important differences between corresponding fields:

    - ``<ElectoralDistrictId>``, which is an optional reference to a VIP `<ElectoralDistrict> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/electoral_district.html>`_ element, can map to an equivalent OCD ``division_id``.

* OCD fields not implemented in VIP:

    - ``election_id`` is a required reference to an OCD ``Election``.

* VIP fields not implemented in this OCDEP:

    - ``<Abbreviation>``, which is an optional string.
    - ``<BallotSelectionIds>`` is an optional single element that contains a set of references to each selection (i.e., any extension of VIP's `<BallotSelectionBase> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_selection_base.html>`_) on any ballot that includes the contest. This proposal instead implements properties on the subclasses of ``Contest`` for storing the distinct options for each contest across all versions of the ballot (e.g., the ``BallotMeasureContest.options`` and ``CandidateContest.candidacies`` properties).
    - ``<ElectorateSpecification>``, which optional text.
    - ``<HasRotation>``, which is an optional boolean.
    - ``<BallotSubTitle>``,  which is optional text.
    - ``<BallotTitle>``,  which is optional text.
    - ``<SequenceOrder>``,  which is an optional integer.
    - ``<VoteVariation>``,  which is an optional reference to a VIP `<VoteVariation> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/vote_variation.html>`_.
    - ``<OtherVoteVariation>``, which is optional text.


BallotMeasureContest
--------------------

A subclass of ``Contest`` for representing a ballot measure before the voters, including options voters may select. Inherits all the required and optional properties of ``Contest``.

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

``BallotMeasureContest`` corresponds to VIP's `<BallotMeasureContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<PassageThreshold>`` maps to ``requirement``.
    - ``<Type>``, which is an optional reference to a VIP `<BallotMeasureType> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/ballot_measure_type.html#multi-xml-ballot-measure-type>`_ maps to ``classification`` which is a simple string.

* OCD fields not implemented in VIP:

    - ``options`` should list the distinct selections across all ballots that include the ``<BallotMeasureContest>`` (i.e., the ``<Selection>`` tag in the `<BallotMeasureSelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html>`_ element).

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

A subclass of ``Contest`` for repesenting a contest among candidates seeking for election to one or more public offices. Inherits all the required and optional properties of ``Contest``.

number_elected
    **optional**
    Number of candidates that are elected in the contest, i.e. 'N' of N-of-M (integer).

office_terms
    **repeated**
    List of references to each OCD ``OfficeTerm`` representing a term of public office for which the candidates in the contest are seeking election. Requires at least one. Has the following properties:

    office_term_id
        Reference to an OCD ``OfficeTerm``.

    sort_order
        **optional**
        Useful for sorting for contests where two or more public offices are at stake, e.g., in a U.S. presidential contest, the President post would have a lower sort order than the Vice President post.

candidacy_ids
    **repeated**
    List of references to each candidacy for one of the public office terms at stake in the contest. Requires at least one.

party_id
    **optional**
    If the contest is among candidates of the same political party, e.g., a partisan primary election, reference to the OCD ``Party`` representing that political party.

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
        "office_terms": [
            {
                "office_term_id": "ocd-officeterm/08d670db-72cb-495b-afdd-f7f91794ad8d",
                "sort_order": 0
            }
        ],
        "candidacy_ids": [
            "ocd-candidacy/153344e1-e533-4a05-880c-a332038cb785",
            "ocd-candidacy/e029a7a6-665a-4b7b-82f7-1ab554905518",
            "ocd-candidacy/355e4858-847c-4cf5-88d6-c8d1de167e07"
        ],
        "is_unexpired_term": false,
        "number_elected": 1,
        "party_id": null,
        "runoff_for_contest_id": null
    }


Mapping to VIP
++++++++++++++

``CandidateContest`` corresponds to VIP's `<CandidateContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<OfficeIds>``, which is an optional set of references to VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ elements, should each map to an OCD ``OfficeTerm``. The order in which the OfficeIds are listed should be preserved in ``sort_order``.

* OCD fields not implemented in VIP:

    + ``candidacy_ids`` should list the distinct candidate selections across all ballots that include the ``<CandidateContest>`` (i.e., each OCD ``Candidacy`` equivalent to each VIP ``<Candidate>`` referenced in the ``<CandidateIds>`` tag in the `<CandidateSelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html>`_ element).
    + ``runoff_for_contest_id`` is optional.

* VIP fields not implemented in this OCDEP:

    - ``<VotesAllowed>``, which is an optional integer.


PartyContest
------------

A subclass of ``Contest`` for representing a contest in which voters can vote directly for a political party in lieu of or in addition to candidates for public office endorsed by that party (as in the case of `party-list proportional representation <https://en.wikipedia.org/wiki/Party-list_proportional_representation>`_ ). Inherits all the required and optional properties of ``Contest``.

parties
    **repeated**
    List of references to each OCD ``Party`` for which a voter could vote in the election contest. Requires at list one. Has the following properties:

    party_id
        Reference to an OCD ``Party``.

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
        "name": "",
        "division_id": "ocd-division/country:us/state:ca/sldu:1",
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

``PartyContest`` corresponds to VIP's `<PartyContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party_contest.html>`_ element. 

* OCD fields not implemented in VIP:
    
    - ``parties`` should list the distinct party selections across all ballots that include the ``<PartyContest>`` (i.e., each OCD ``Party`` equivalent to each VIP ``<Party>`` referenced in the ``<PartyIds>`` tag in the `<PartySelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html>`_ element).
    - ``runoff_for_contest_id`` an optional field.


RetentionContest
----------------

A subclass of ``BallotMeasureContest`` that represents a contest where voters vote to retain or recall a current office holder, e.g. a judicial retention or recall election. Inherits all the required and optional properties of ``BallotMeasureContest``.

In a ``RetentionContest``, voters typically have two options (e.g., "yes" or "no", "recall" or "don't recall"), unlike in a ``CandidateContest`` where voters can choose from among multiple different candidates.

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

``RetentionContest`` corresponds to VIP's `<RetentionContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/retention_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<CandidateId>``, which is a required reference to a VIP `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ element, and ``<OfficeId>``, which is an optional reference to a VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element, should map to an equivalent OCD ``Membership`` representing a specific person's (i.e, an OCD ``Person`` object) tenure in a specific public office (i.e., an OCD ``Post`` object).

Candidacy
---------

A person competing to serve a term in a specific public office.

id
    Open Civic Data-style id in the format ``ocd-candidacy/{{uuid}}``.

person_id
    Reference to an OCD ``Person`` who is the candidate.

office_term_id
    Reference to the OCD ``OfficeTerm`` representing the term of public office for which the candidate is seeking election.

candidate_name
    **optional**
    For preserving the candidate's name as it was when the person sought election to hold the public office term, which may differ from the person's current name (string).

committee_id
    **optional**
    Reference to the OCD ``Committee`` (see OCDEP: Campaign Finance Filings) that represents the candidate's campaign committee for the contest.

filed_date
    **optional**
    Specifies when the candidate filed for the contest (date).

is_incumbent
    **optional**
    Indicates whether the candidate is seeking re-election a public office he/she currently holds (boolean).

party_id
    **optional**
    Reference to and OCD ``Party`` with which the candidate is affiliated.

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
        "candidate_name": "ROWEN, ROBERT J.",
        "person_id": "ocd-person/edfafa56-686d-49ea-80e5-64bc795493f8",
        "committee_id": null,
        "filed_date": 2016-03-10,
        "is_incumbent": false,
        "party_id": "ocd-organization/866e7266-0c21-4476-a7a7-dc11d2ae8cd1",
        "top_ticket_candidacy_id": null,
        "created_at": "2017-02-08T04:17:30.818Z",
        "updated_at": "2017-02-08T04:17:30.818Z",
        "sources": [],
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``Candidacy`` corresponds to VIP's `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ element.

* Important differences between corresponding fields:
  
    - ``<PartyId>``, which is an optional reference a VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ element, can map to an equivalent OCD ``Party``.
    - ``person_id`` , which is an optional reference a VIP `<Person> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/person.html>`_ element, can map to an equivalent OCD ``Person``.
    - ``<IsTopTicket>``, which is an optional boolean indicating the candidate is the top of a ticket that includes multiple candidates, is replaced by an optional ``top_ticket_candidacy_id``. 

* OCD fields not implemented in VIP:
      
    - ``committee_id`` is optional.

* VIP fields not implemented in this OCDEP:

    - ``<ContactInformation>`` refers to an element that describes the contact and physical address information for the candidate or their campaign. On and OCD ``Candidacy``, this information would be stored on the associated ``Person`` or ``Committee`` object.
    - ``<PostElectionStatus>``, which is an optional reference to a VIP `<CandidatePostElectionStatus> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_post_election_status.html>`_.
    - ``<PreElectionStatus>``, which is an optional reference to a VIP `<CandidatePreElectionStatus> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_pre_election_status.html>`_.


OfficeTerm
----------
The interval in which an elected candidate is expected to hold a public office before being re-elected or replaced.

id
    Open Civic Data-style id in the format ``ocd-officeterm/{{uuid}}``.

post_id
    Reference to the OCD ``Post`` representing the public office held for the interval.

start_date
    Date the office holder's term is expected to start. Not necessarily the same as the date when the person began serving in the office (as in the case of a re-election).

end_date
    Date the office holder's term is expected to end. Not necessarily the same as the date when the office holder vacated the office.

previous_term_unexpired
    Indicates the previous public office holder vacated the post before serving a full term (boolean).

filing_deadline
    **optional**
    Specifies the date and time by when persons must of official filed their candidacies for election or re-election (datetime).

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


Sample OfficeTerm
+++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-officeterm/08d670db-72cb-495b-afdd-f7f91794ad8d",
        "post_id": "ocd-post/f204b117-24af-42fd-a3fc-c5772533fdf5",
        "filing_deadline": "2016-09-01T01:01:00.000Z",
        "start_date": "2017-01-04",
        "end_date": "2021-01-04",
        "pervious_term_unexpired": false,
        "created_at": "2017-02-07T16:36:12.497Z",
        "updated_at": "2017-02-07T16:36:12.497Z",
        "sources": [],
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``Post`` and ``OfficeTerm`` correspond to VIP's `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ and `<Term> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html#term>`_ elements.

* Important differences between corresponding fields:
  
    - ``<Name>`` on VIP's ``<Office>`` maps to ``label`` on OCD's ``Post``.
    - ``<ElectoralDistrictId>`` on VIP's ``<Office>``, which is a required reference to a VIP `<ElectoralDistrict> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/electoral_district.html>`_ element, should map to an equivalent OCD ``division_id``.
    - ``<ContactInformation>`` on VIP's ``<Office>`` maps to the ``contact_details`` on OCD's ``Post``.
    - ``<OfficeHolderPersonIds>`` on VIP's ``<Office>`` is an optional single tag that contains a set of references  to each office holder represented, as a VIP `<Person> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/person.html>`_. Each of these can map to an equivalent OCD ``Membership`` (i.e., a combination of a ``Person``/``Post``/``Organization``).
    - A VIP ``<Office>`` can only have a single ``<Term>``, but an OCD ``Post`` can be linked to multiple OCD ``OfficeTerm`` objects.
    - ``<Start_Date>`` on VIP's ``<Term>`` maps to ``start_date`` on OCD's ``OfficeTerm``.
    - ``<End_Date>`` on VIP's ``<Term>`` maps to ``end_date`` on OCD's ``OfficeTerm``.
    - If ``<Type>`` on VIP's ``<Term>`` is "unexpired-term", then ``previous_term_unexpired`` on OCD's ``OfficeTerm`` should be ``true``. Otherwise, ``previous_term`` should be ``false``.

* VIP fields not implemented in this OCDEP:
  
  - ``<Description>`` on ``<Office>`` is optional text.
  - ``<IsPartisan>`` on ``<Office>`` is an optional boolean.


Party
-----

A political party with which office holders and candidates may be affiliated.

``Party`` is a subclass of OCD's ``Organization`` data type, defined in `OCDEP 5: People, Organizations, Posts, and Memberships <http://opencivicdata.readthedocs.io/en/latest/proposals/0005.html>`_, which was accepted in June 2014. All of required and optional properties of ``Organization`` are inherited by ``Party``.

abbreviation
    **optional**
    An abbreviation for the party name (string).

color
    **optional**
    Six-character hex code representing an HTML color string. The pattern is ``[0-9a-f]{6}``.

is_write_in
    **optional**
    Indicates that the party is not officially recognized by a local, state, or federal organization but, rather, is a "write-in" in jurisdictions which allow candidates to free-form enter their political affiliation (boolean).


Sample Party
++++++++++++


.. code:: javascript

    {
        "id": "ocd-organization/866e7266-0c21-4476-a7a7-dc11d2ae8cd1"
        "name": "DEMOCRATIC",
        "image": "",
        "parent": null,
        "jurisdiction": null,
        "classification": "party",
        "founding_date": null,
        "dissolution_date": null,
        "identifiers": [],
        "other_names": [],
        "contact_details": [],
        "links": [],
        "abbreviation": "D",
        "color": "1d0ee9",
        "is_write_in": false,
        "created_at": "2017-02-07T16:36:12.497Z",
        "updated_at": "2017-02-07T16:36:12.497Z",
        "sources": [],
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``Party`` corresponds to VIP's `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ element.

* Important differences between corresponding fields:

    - ``<Name>`` is not required on VIP's ``<Party>``, but ``name`` (inherited from OCD's ``Organization``) is required.

* OCD fields not implemented in VIP:

    - ``classification`` (inherited from ``Organization``) should be "party".
    - ``parent`` (inherited from ``Organization``) is optional.
    - ``jurisdiction`` (inherited from ``Organization``) is optional.
    - ``founding_date`` (inherited from ``Organization``) is optional.
    - ``dissolution_date`` (inherited from ``Organization``) is optional.
    - ``other_names`` (inherited from ``Organization``) is optional.
    - ``contact_details`` (inherited from ``Organization``) is optional.
    - ``links`` (inherited from ``Organization``) is optional.

* VIP fields not implemented in this OCDEP:
  
    - ``<LogoUri>``, which is optional.


Copyright
=========

This document has been placed in the public domain per the `Creative Commons CC0 1.0 Universal license <http://creativecommons.org/publicdomain/zero/1.0/deed>`_.