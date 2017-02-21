====================
OCDEP: Elections
====================

:Created: 2016-12-28
:Author: James Gordon, Forest Gregg, `California Civic Data Coalition <http://www.californiacivicdata.org/>`_
:Status: Proposed

Overview
========

Definition of data types to model elections and political contests they are held in order to decided.

The proposed data types are:

* ``Election``
* ``Contest``, a base class for:

    - ``BallotMeasureContest``
    - ``CandidateContest``
    - ``PartyContest``
    - ``RetentionContest``

* ``Candidacy``
* ``Party``
* ``BallotSelection``, a base class for:

    - ``BallotMeasureSelection``
    - ``CandidateSelection``
    - ``PartySelection``

Supplements the "Campaign Finance Filings" proposal prepared by Abraham Epton.

Definitions
===========

Ballot
    An official form containing all available selections in each contest in which a voter may vote in an election.

Ballot Measure
    A proposition (aka, "question") included on the ballot of an election so as to be approved or rejected directly by voters. These propositions include:

    * The enactment or repeal of a statute, constitutional amendment or other form of law.
    * Approval or rejection of a new tax or additional spending of public funds.
    * The recall or retention of a previously elected public office holder.

Candidacy
    The condition of a person being a candidate. A single person may have multiple candidacies if:

    * The person competed to hold multiple public offices, even in the same election.
    * The person competed to hold the same public office in more than one election. This includes:

        - A person who is elected to a public office, serves a full term and runs for re-election as an incumbent candidate.
        - A person who wins a contest to become a nominee for a public office (known as a "primary election" in U.S. politics) who advances to the final contest of candidates (aka, the "general election").

Candidate
    A person competing to be elected to hold a particular public office.

Contest
    A specific decision with a set of predetermined options (aka, "selections") put before voters via a ballot in an election. These contests include the selection of a person from a list of candidates to hold a public office or the approval or rejection of a ballot measure.

Election
    A collection of political contests decided in parallel through a process of compiling official ballots cast by voters and adding up the total votes for each selection in each contest.

Election Day
    The final or only date when eligible voters may cast their ballots in an election. Typically this is also the same date when results of the election's contests are first publicly reported.

Incumbent
    The candidate for a public office who also currently holds that public office.

Party
    A political organization to which public office holders and candidates can be affiliated.

Public Office
    A position within a governmental body which is filled through an election contest.

Runoff Contest
    A contest conducted to decide a previous contest in which no single selection received the required number of votes to decide the contest.

Selection
    A predetermined option that voters could select on a ballot in an election contest.

Term of Office
    The period of time a person elected to a public office is expected retain the position before being re-elected or replaced.

    For a variety of reasons, an office holder may vacate an elected office before serving a full term. This is known as an "unexpired term", a situation which could require an additional contest (known as a "Special Election" in U.S. politics) to fill the empty public office.

Ticket
    Two or more allied candidates competing together in the same contest fill two or more public offices. For example, in U.S. politics, candidates for President and Vice President run together on the same ticket, with the President at the top of the ticket.

Vote
    A specific selection selected by a voter on a ballot in an election contest.

Voter
    A person who is eligible to vote in an election.

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

Each of the data types described in this proposal corresponds to an element described in the VIP's current `XML format specification <http://vip-specification.readthedocs.io/en/vip5/xml/index.html#elements>`_. While interoperability with VIP data is a goal of this proposal, there is not a one-to-one mapping between the tags within a VIP element and the properties of its corresponding data type in this OCDEP.

Important differences between the proposed OCD data type and its corresponding VIP element, if any, are noted in each data type's "Mapping to VIP" subsection in Implementation_.

One general note: VIP describes `<InternationalizedText> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html>`_ and `<LanguageString> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html#languagestring>`_ elements for the purposes of representing certain texts in multiple languages, e.g., the English and Spanish translations of the ``support_statement`` and ``oppose_statement`` of a ``BallotMeasureContest``. In this proposal, these data types are described as simple strings.

Implementation
==============

Election
---------

A collection of political contests set to be decided on the same date.

id
    Open Civic Data-style id in the format ``ocd-election/{{uuid}}``.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the election if any exist, such as those assigned by a Secretary of State, county or city elections office.

name
    Common name for the election. Typically describes roughly when the election occurred and the scope of the contests to be decided, e.g., "2014 Primaries", "2015 Boone County Elections" or "2016 General Elections" (string).

date
    Date on which the election is set to be decided (aka, Election Day). This tends to be the last day when voters can cast their ballots and the first day when the election's results a publicly reported (date).

    This date is considered to be in the timezone local to the election's division.

division_id
    Reference to the OCD ``Division`` that defines the broadest geographical scope of any contest to be decided by the election. For example, an election that includes a contest to elect the governor of California would include the division identifier for the entire state of California.

administrative_organization_id
    **optional**
    Reference to the OCD ``Organization`` that administers the election and publishes the official results.

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


Sample Election
+++++++++++++++


.. code:: javascript

    {
        "id": "ocd-election/4c25d655-c380-46a4-93d7-28bc0c389629",
        "identifiers": [
            {
                "scheme": "calaccess_election_id",
                "identifier": "65"
            }
        ],
        "name": "2016 GENERAL",
        "date": "2016-11-08",
        "division_id": 'ocd-division/country:us/state:ca/'
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

    - ``<Name>`` is not required on VIP, but ``name`` is required on OCD's ``Event``.
    - ``<StateId>``, which is a required reference to a VIP `<State> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/state.html>`_ element, maps to ``division_id``. If ``<IsStatewide>`` is true on the VIP election, then ``division_id`` will reference the same state. Otherwise, it should reference one of the state's subdivisions.

* OCD fields not implemented in VIP:

    - ``administrative_organization_id`` is optional.

* VIP fields not implemented in this OCDEP:

    - ``<ElectionType>``, which is an optional string that conflates the level of government to which a candidate might be elected (e.g., "federal", "state", "county", etc.) with the point when the election occurs in the overall cycle (e.g., "general", "primary", "runoff" and "special").
    - ``<HoursOpenId>``, which is an optional reference to a VIP `<HoursOpen> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/hours_open.html>`_ element that represents when polling locations for the election are generally open.
    - ``<IsStatewide>``, which is an optional boolean.
    - ``<RegistrationInfo>``, which is an optional string.
    - ``<RegistrationDeadline>`, which is an optional date.
    - ``<HasElectionDayRegistration>``, which is an optional boolean.
    - ``<AbsenteeBallotInfo>``, which is an optional string.
    - ``<AbsenteeRequestDeadline>``, which is an optional date.
    - ``<ResultsUri>``, which is optional.


Contest
-------

A base class representing a specific decision set before voters in an election. Includes properties shared by all contest types: ``BallotMeasureContest``, ``CandidateContest``, ``PartyContest`` and ``RetentionContest``.

id
    Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the contest if any exist, such as those assigned by a Secretary of State, county or city elections office.

name
    Name of the contest, not necessarily as it appears on the ballot (string).

division_id
    Reference to the OCD ``Division`` that defines the geographical scope of the contest, e.g., a specific Congressional or State Senate district. The ``Division`` referenced by each ``Contest`` should be a subdivision of the ``Divsion`` referenced by its ``Election``.

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
        "election_id": "ocd-election/4c25d655-c380-46a4-93d7-28bc0c389629",
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

    - ``<ElectoralDistrictId>``, which is an optional reference to a VIP `<ElectoralDistrict> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/electoral_district.html>`_ element, is replaced by ``division_id``, which is a required reference to an OCD ``Division``.

* OCD fields not implemented in VIP:

    - ``election_id`` is a required reference to an OCD ``Election``.

* VIP fields not implemented in this OCDEP:

    - ``Abbreviation``, which is an optional string.
    - ``<BallotSelectionIds>``, which is an optional single element that contains a set of references to ballot selections for the contest. Instead, ``BallotSelection`` includes a single, required ``contest_id``.
    - ``<ElectorateSpecification>``, which an optional string.
    - ``<HasRotation>``, which is an optional boolean.
    - ``<BallotSubTitle>``,  which is an optional string.
    - ``<BallotTitle>``,  which is an optional string.
    - ``<SequenceOrder>``,  which is an optional integer.
    - ``<VoteVariation>``,  which is an optional reference to a VIP `<VoteVariation> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/vote_variation.html>`_.
    - ``<OtherVoteVariation>``, which is an optional string.


BallotMeasureContest
--------------------

A subclass of ``Contest`` for representing a ballot measure before the voters, including summary statements on each side. Inherits all of the required and optional properties of ``Contest``.


summary
    **optional**
    Short summary of the ballot measure that is on the ballot, below the title, but above the text.

text
    **optional**
    The full text of the ballot measure as it appears on the ballot (string).

support_statement
    **optional**
    A statement in favor of the ballot measure. It does not necessarily appear on the ballot (string).

oppose_statement
    **optional**
    A statement in opposition to the ballot measure. It does not necessarily appear on the ballot (string).

effect_of_abstain
    **optional**
    Specifies the effect abstaining from voting on the ballot measure, i.e., whether abstaining is considered a vote against it (string).

requirement
    **optional**
    The threshold of votes the ballot measure needs in order to pass (string). The default is a simple majority, i.e., "50% plus one vote". Other common thresholds are "three-fifths" and "two-thirds".

classification
    **optional**
    Describes the origin and/or potential outcome of the ballot measure, e.g., "initiative statute", "legislative constitutional amendment" (string).


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
        "election_id": "ocd-election/4c25d655-c380-46a4-93d7-28bc0c389629",
        "created_at": "2017-02-07T07:17:59.818Z",
        "updated_at": "2017-02-07T07:17:59.818Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-07",
                "url": "http://cal-access.ss.ca.gov/Campaign/Measures/Detail.aspx?id=1376195&session=2015"
            }
        ],
        "extras": {},
        "support_statement": "",
        "oppose_statement": "",
        "effect_of_abstain": "",
        "text": "",
        "requirement": "50% plus one vote",
        "summary": "Requires adult film performers to use condoms during filming of sexual intercourse. Requires producers to pay for performer vaccinations, testing, and medical examinations. Requires producers to post condom requirement at film sites. Fiscal Impact: Likely reduction of state and local tax revenues of several million dollars annually. Increased state spending that could exceed $1 million annually on regulation, partially offset by new fees",
        "classification": "initiative statute"
    }


Mapping to VIP
++++++++++++++

``BallotMeasureContest`` corresponds to VIP's `<BallotMeasureContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<ConStatement>`` maps to ``oppose_statement``.
    - ``<ProStatement>`` maps to ``support_statement``.
    - ``<PassageThreshold>`` maps to ``requirement``.
    - ``<Type>``, which is an optional reference to a VIP `<BallotMeasureType> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/ballot_measure_type.html#multi-xml-ballot-measure-type>`_ maps to ``classification`` which is a simple string.

* VIP fields not implemented in this OCDEP:

    - ``<InfoUri>``, which is optional.
    - ``<OtherType>``, which is optional.

CandidateContest
----------------

A subclass of ``Contest`` for repesenting a contest among candidates competing for election to a public office. Inherits all of the required and optional properties of ``Contest``.

filing_deadline
    **optional**
    Specifies the date and time when a candidate must have filed for the contest for the office (datetime). This date is considered to be in the timezone local to the contest's division.

is_unexpired_term
    Indicates that the former public office holder vacated the post before serving a full term (boolean).

number_elected
    **optional**
    Number of candidates that are elected in the contest, i.e. 'N' of N-of-M (integer).

post_ids
    **repeated**
    Lists each identifier of an OCD ``Post`` representing a public office for which the candidates are competing in the contest. Has the following properties:

        post_id
            Reference to an OCD ``Post``.

        sort_order
            **optional**
            Useful for sorting posts in contests where two or more public offices are at stake, e.g., in a U.S. presidential contest, the President post would have a lower sort order than the Vice President post.

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
        "election_id": "ocd-election/4c25d655-c380-46a4-93d7-28bc0c389629",
        "created_at": "2017-02-07T07:18:05.438Z",
        "updated_at": "2017-02-07T07:18:05.442Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-08",
                "url": "http://cal-access.ss.ca.gov/Campaign/Candidates/list.aspx?view=certified&electNav=65"
            }
        ],
        "extras": {},
        "filing_deadline": 2016-06-07,
        "posts": [
            {
                "id": "ocd-post/f204b117-24af-42fd-a3fc-c5772533fdf5",
                "sort_order": 0
            }
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

    - ``<OfficeIds>``, which is an optional set of references to VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ elements, is replaced by ``post_ids``, which is a repeated field that requires at least one reference to an OCD ``Post``. In VIP, the primary office should be listed first. In OCD, the primary post should have ``is_primary`` set to true.

* OCD fields not implemented in VIP:

    - required:

        + ``is_unexpired_term`` could be inferred from ``<Name>`` or ``<ElectionType>`` tags (e.g., for U.S. elections, these tags would likely include "special") or from the date of the election.

    - optional:

        + ``filing_deadline`` is stored in the `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element in VIP.
        + ``runoff_for_contest_id`` is the id of the ``CandidateContest`` with the same ``post_ids`` and ``party_id`` values occurring on the previous election date.

* VIP fields not implemented in this OCDEP:

    - ``<VotesAllowed>``, which is an optional integer.


PartyContest
------------

A subclass of ``Contest`` which represents a contest in which the possible ballot selections are all political parties. These could include contests in which straight-party selections are allowed, or party-list contests (although these are more common outside of the United States). Inherits all of the required and optional properties of ``Contest``.

Mapping to VIP
++++++++++++++

``PartyContest`` corresponds to VIP's `<PartyContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party_contest.html>`_ element. The two have no significant differences.


RetentionContest
----------------

A subclass of ``BallotMeasureContest`` that represents a contest where a person is retains or loses a public office, e.g. a judicial retention or recall election. Inherits all of the required and optional properties of ``BallotMeasureContest``.

membership_id
    Reference to the OCD ``Membership`` that represents the tenure of a particular person (i.e., OCD ``Person`` object) in a particular public office (i.e., ``Post`` object).


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
        "election_id": "ocd-election/3f904160-d304-4753-a542-578cfcb86e76",
        "created_at": "2017-02-07T07:18:00.555Z",
        "updated_at": "2017-02-07T07:18:00.555Z",
        "sources": [
            {
                "note": "Last scraped on 2017-02-07",
                "url": "http://cal-access.ss.ca.gov/Campaign/Measures/Detail.aspx?id=1256382&session=2003"
            }
        ],
        "extras": {},
        "support_statement": "",
        "oppose_statement": "",
        "effect_of_abstain": "",
        "requirement": "",
        "summary": "SHALL GRAY DAVIS BE RECALLED (REMOVED) FROM THE OFFICE OF GOVERNOR?",
        "text": "",
        "classification": "recall",
        "other_type": "",
        "membership_id": "ocd-membership/181a0826-f458-403f-ae65-e1ce97b8dd34"
    }


Mapping to VIP
++++++++++++++

``RetentionContest`` corresponds to VIP's `<RetentionContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/retention_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<CandidateId>``, which is a required reference to a VIP `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ element, and ``<OfficeId>``, which is an optional reference to a VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element, are replaced by ``membership_id``, which is a required reference to an OCD ``Membership`` representing a particular person's tenure in a particular public office.

* VIP fields not implemented in this OCDEP:

    - ``<OfficeId>``, which is an optional reference to a VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_. VIP's ``<Office>`` element corresponds to OCD's ``Post`` data type. In this proposal, a candidate's ``post_id`` is stored on ``Candidacy``, including .


Candidacy
---------

Represents a person who is a candidate in a particular ``CandidateContest``. If a candidate is running in multiple contests, each contest must have its own ``Candidate`` object. ``Candidate`` objects may not be reused between contests.

id
    Open Civic Data-style id in the format ``ocd-candidacy/{{uuid}}``.

ballot_name
    The candidate's name as it will be displayed on the official ballot, e.g. "Ken T. Cuccinelli II" (string).

person_id
    Reference to an OCD ``Person`` who is the candidate.

post_id
    References the ``Post`` that represents the public office for which the candidate is competing.

committee_id
    **optional**
    Reference to the OCD ``Committee`` (see OCDEP: Campaign Finance Filings) that represents the candidate's campaign committee for the contest.

filed_date
    **optional**
    Specifies when the candidate filed for the contest (date). This is considered to be in the timezone local to contest's division.

is_incumbent
    **optional**
    Indicates whether the candidate is the incumbent for the office associated with the contest (boolean).

party_id
    **optional**
    Reference to and OCD ``Party`` with which the candidate is affiliated.

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
        "ballot_name": "ROWEN, ROBERT J.",
        "person_id": "ocd-person/edfafa56-686d-49ea-80e5-64bc795493f8",
        "post_id": "ocd-post/0f169eea-0ad6-48c2-8bc5-ca86e08643d0",
        "committee_id": null,
        "filed_date": 2016-03-10,
        "ballot_selection_id": "ocd-ballotselection/d2716878-99fa-467b-b3b6-d28862a6802f",
        "is_incumbent": false,
        "party_id": 'ocd-party/866e7266-0c21-4476-a7a7-dc11d2ae8cd1',
        "created_at": "2017-02-08T04:17:30.818Z",
        "updated_at": "2017-02-08T04:17:30.818Z",
        "sources": [],
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``Candidacy`` corresponds to VIP's `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ element.

* Important differences between corresponding fields:

    - ``party_id`` is an optional reference an OCD ``Party``, not a VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ element.
    - ``person_id`` is a required reference an OCD ``Person``, not a VIP `<Person> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/person.html>`_ element.

* OCD fields not implemented in VIP:

    - required:
      
        + ``post_id`` is required to link the candidate to the public office for which they are competing. In VIP, this is represented as an `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element, which is stored on the ``<CandidateContest>`` element.

    - optional:
      
        + ``committee_id``

* VIP fields not implemented in this OCDEP:

    - ``<ContactInformation>`` refers to an element that describes the contact of physical address information for the candidate or their campaign. On and OCD ``Candidacy``, this information would be found on the associated ``Person`` or ``Committee`` object.
    - ``<PostElectionStatus>``, which is an optional reference to a VIP `<CandidatePostElectionStatus> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_post_election_status.html>`_.
    - ``<PreElectionStatus>``, which is an optional reference to a VIP `<CandidatePreElectionStatus> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_pre_election_status.html>`_.
    - ``<IsTopTicket>``, which is an optional boolean indicating the candidate is the top of a ticket that includes multiple candidates. OCD relies on the ``candidacies`` property of ``CandidateSelection`` to represent the ticket and the ``sort_order`` property of each ``post_id`` listed on ``CandidateContest`` to indicate which candidates are running and the top of their respective tickets.


Party
-----

Political organization with which office holders and candidates may be affiliated.

id
    Open Civic Data-style id in the format ``ocd-party/{{uuid}}``.

name
    The name of the party (string).

abbreviation
    **optional**
    An abbreviation for the party name (string).

color
    **optional**
    Six-character hex code representing an HTML color string. The pattern is ``[0-9a-f]{6}``.

is_write_in
    **optional**
    Indicates that the party is not officially recognized by a local, state, or federal organization but, rather, is a "write-in" in jurisdictions which allow candidates to free-form enter their political affiliation (boolean).

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


Sample Party
++++++++++++


.. code:: javascript

    {
        "id": "ocd-party/866e7266-0c21-4476-a7a7-dc11d2ae8cd1"
        "name": "DEMOCRATIC",
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

    - ``name`` is required.

* VIP fields not implemented in this OCDEP:
  
    - ``logo_uri``, which is optional.


BallotSelection
---------------

A base class representing a predetermined option on a ballot that voters could select in an election contest. Includes the properties shared by all ballot selection types: ``BallotMeasureSelection``, ``CandidateSelection`` and ``PartySelection``.

id
    Open Civic Data-style id in the format ``ocd-ballotselection/{{uuid}}``.

created_at
    Time that this object was created at in the system.

updated_at
    Time that this object was last updated in the system.

extras
    Common to all Open Civic Data types, the value is a key-value store suitable for storing arbitrary information not covered elsewhere.


Sample BallotSelection
++++++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-ballotselection/d2716878-99fa-467b-b3b6-d28862a6802f"
        "created_at": "2017-02-08T04:17:30.817Z",
        "updated_at": "2017-02-08T04:17:30.817Z",
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``BallotMeasureSelection`` corresponds to VIP's `<BallotSelectionBase> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_selection_base.html>`_ element.

* OCD fields not implemented in VIP:

    - ``contest_id`` is required in order to link the selection to its associated contest. In VIP, this link is stored in `<OrderedContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ordered_contest.html>`_, which allows for modeling ballot layouts that vary between electoral districts, but is outside the scope of this proposal.

* Other VIP fields not implemented in this OCDEP:

    - ``<SequenceOrder>``, which is an optional integer.


BallotMeasureSelection
----------------------

A subclass of ``BallotSelection`` representing an option that voters could select on a ballot in a ballot measure contest, e.g., "yes" or "no". Inherits all of the required and optional properties of ``BallotSelection``.

selection
    Selection text for the option on the ballot, e.g., "Yes", "No", "Recall", "Don't recall" (string).

contest_id
    References the ``BallotMeasureContest`` in which the ballot selection is an option.


Sample BallotMeasureSelection
+++++++++++++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-ballotselection/85399ed5-b91d-4a7c-a868-dd152ce28ed4",
        "contest_id": "ocd-contest/2ce7e19b-3feb-4318-9908-eb3fdf456fb0",
        "selection": "Yes",
        "created_at": "2017-02-08T04:17:24.486Z",
        "updated_at": "2017-02-08T04:17:24.486Z",
        "extras": {}
    }


Mapping to VIP
++++++++++++++

``BallotMeasureSelection`` corresponds to VIP's `<BallotMeasureSelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html>`_ element. There are no significant differences between the two.


CandidateSelection
------------------

A subclass of ``BallotSelection`` representing an option that voters could select on a ballot in a candidate contest, e.g., a particular candidate or "ticket". Inherits all of the required and optional properties of ``BallotSelection``.

id
    Open Civic Data-style id in the format ``ocd-candidateselection/{{uuid}}``.

contest_id
    References the ``CandidateContest`` in which the ballot selection is an option.

candidacy_ids
    **repeated**
    Lists each identifier of an OCD ``Candidacy`` associated with the ballot selection. Requires at least one ``candidacy_id``, but the number of candidates is unbounded in cases where the ballot selection is for a ticket, e.g. "President/Vice President", "Governor/Lt Governor".

endorsement_party_ids
    **optional**
    **repeated**
    Lists each identifer of an OCD ``Party`` that is endorsing the candidates associated with the selection. The number of parties is unbounded in cases where multiple parties endorse a single candidate/ticket.

is_write_in
    **optional**
    Indicates that the particular ballot selection allows for write-in candidates. If true, one or more write-in candidates are allowed for this contest (boolean).


Sample CandidateSelection
+++++++++++++++++++++++++


.. code:: javascript

    {
        "id": "ocd-ballotselection/d2716878-99fa-467b-b3b6-d28862a6802f"
        "contest_id": "ocd-contest/eff6e5bd-10dc-4930-91a0-06e2298ca15c",
        "candidacy_ids": [
            "ocd-candidacy/054f0a6e-9c06-4611-8c2c-3e143843c9d8"
        ],
        "is_write_in": false,
        "created_at": "2017-02-08T04:17:30.817Z",
        "updated_at": "2017-02-08T04:17:30.817Z",
        "extras": {},
    }


Mapping to VIP
++++++++++++++

``CandidateSelection`` corresponds to VIP's `<CandidateSelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate_selection.html>`_ element.

* Important differences between corresponding fields:

    - ``<CandidateIds>``, which is an optional set of references to VIP `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ elements, is replaced by ``candidacy_ids``, which is a repeating field that requires at least one reference to an OCD ``Candidacy``.
    - ``<EndorsementPartyIds>``, which is an optional set of references to VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ elements, is replaced by ``endorsement_party_ids``, which is an optional repeating field that list references to each OCD ``Party`` endorsing the candidate(s).


PartySelection
--------------

A subclass of ``BallotSelection`` representing an option that voters could select on a ballot in a party contest. Inherits all of the required and optional properties of ``BallotSelection``.

id
    Open Civic Data-style id in the format ``ocd-partyselection/{{uuid}}``.

party_ids
    **repeated**
    Lists each identifier of an OCD ``Party`` associated with the ballot selection. Requires at least one ``party_id``.

Mapping to VIP
++++++++++++++

``PartySelection`` corresponds to VIP's `<PartySelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party_selection.html>`_ element.

* Important differences between corresponding fields:

    - ``<PartyIds>``, which is an optional, set of references to VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ elements, is replaced by ``endorsement_party_ids``, which is an optional repeating field that list references to each OCD ``Party`` associated with the selection.


Copyright
=========

This document has been placed in the public domain per the `Creative Commons CC0 1.0 Universal license <http://creativecommons.org/publicdomain/zero/1.0/deed>`_.