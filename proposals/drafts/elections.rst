====================
OCDEP: Elections
====================

:Created: 2016-12-28
:Author: James Gordon, Forest Gregg, `California Civic Data Coalition <http://www.californiacivicdata.org/>`_
:Status: Proposed

Overview
========

Definition of data types to model elections within which political contests are decided, including relationships to ballot measures and candidates competing for public office.

The proposed data types are:

* ``Election``
* ``ContestBase``, a base class for:

    - ``BallotMeasureContest``
    - ``CandidateContest``
    - ``PartyContest``
    - ``RetentionContest``

* ``Candidacy``
* ``Party``
* ``BallotSelectionBase``, a base class for:

    - ``BallotMeasureSelection``
    - ``CandidateSelection``
    - ``PartySelection``

Supplements the "Campaign Finance Filings" proposal being prepared by Abraham Epton.

Rationale
=========

Elections are a primary focal point of civic activity in which eligible voters cast ballots to determine the outcome of political contests, including:

* Who should hold a public office?
* Should a proposed change of law be implemented?

Modeling the potential outcomes of these contests is a service to voters who may cast their ballots in an impending election. Modeling the contests' actual outcomes legitimizes the election's results and enables historical electoral analysis.

This proposal is submitted in response to on-going discussion around a related OCDEP focused on campaign-finance disclosures. Representing elections and their contests is necessary for modeling these disclosures because they reveal money raised and spent in support or opposition to specific candidates and ballot measures. However, since notions of elections and their contests run up against other domains, we've separated the definition of these types.

The goal of this proposal is to cover the use cases related to the campaign finance domain while laying the foundation for models that will include election results (to be covered in a future OCDEP).

Our use cases require unique representations of both previous elections and contests as well as pending elections and contests. While honoring these requirements, we also aim for consistency with the Voting Information Project's `XML format specification <http://vip-specification.readthedocs.io/en/vip5/xml/index.html#elements>`_ so as to support a high degree of interoperability with that existing data standard.

VIP 5, the specification's current version, incorporates elements from the `Election Results Common Data Format Specification <https://www.nist.gov/itl/voting/nist-election-results-common-data-format-specification>`_ defined by the National Institute of Standard and Technology. As such, we have borrowed eagerly from NIST's current specification also.

Important differences between this proposal and the current VIP specification are noted below.

Questions
=========

* Does ``Election`` need one property (or two properties) to store the election type (e.g., general, primary, special) and/or election level (e.g., federal, state, county, local)? VIP's `<Election> <>`_ element has an `ElectionType` field, but this is just a string that you can apparently populate with whatever.
* Should ``Party`` be implemented as an ``Organization`` (or subclass)? If so, how do we handle national parties versus state parties (e.g., the DNC versus Missouri Democratic Party)? Would probably be more accurate to associate state and local candidates with state parties and federal candidates with the national parties. But would expect most users typically to want all Democrats to be grouped together regardless of the level of government, especially when analyzing election results.
* Should the proposed subclasses of OCD data types (e.g., ``Election``, ``BallotMeasureContest``,  ``CandidateContest``) each implement its own ID or should it just inherit the id field of the base class?


Implementation
==============

Election
--------

A collection of political contests set to be decided on the same date.

``Election`` is a subclass of OCD's ``Event`` data type, defined in `OCDEP 4: Events <http://opencivicdata.readthedocs.io/en/latest/proposals/0004.html>`_, which was accepted in June 2014. All of core and optional properties of ``Event`` are inherited by ``Election``.

The typical implementation will be an ``all_day`` event witht a "election" ``classification`` value and a ``start_time`` set to midnight of the observed election date.

id
    Open Civic Data-style id in the format ``ocd-election/{{uuid}}``.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the election if any exist, such as those assigned by a Secretary of State, county or city elections office.

administrative_org_id
    **optional**
    Reference to the ``Organization`` that administers the election.

state
    `FIPS code <https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code>`_ of the state where the election is being held. Recorded in the format ``st{{fips}}`` to match references to VIP `<State> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/state.html>`_  elements (string).

is_statewide
    **optional**
    Indicates whether the election is statewide (boolean).


ContestBase
-----------

A base class with the properties shared by all contest types: ``BallotMeasureContest``, ``CandidateContest``, ``PartyContest`` and ``RetentionContest``.

id
    Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.

identifiers
    **optional**
    **repeated**
    Upstream identifiers of the contest if any exist, such as those assigned by a Secretary of State, county or city elections office.

name
    Name of the contest, not necessarily as it appears on the ballot (string).

division_id
    Reference to the ``Division`` that defines the geographical scope of the contest, e.g., a specific Congressional or State Senate district.

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


BallotMeasureContest
--------------------

A subclass of ``ContestBase`` for representing a ballot measure before the voters, including summary statements on each side.

id
    Open Civic Data-style id in the format ``ocd-ballotmeasurecontest/{{uuid}}``

con_statement
    **optional**
    Specifies a statement in opposition to the ballot measure. It does not necessarily appear on the ballot (string).

effect_of_abstain
    **optional**
    Specifies the effect abstaining from voting on the ballot measure, i.e., whether abstaining is considered a vote against it (string).

full_text
    **optional**
    Specifies the full text of the ballot measure as it appears on the ballot (string).

passage_threshold
    **optional**
    Specifies the threshold of votes the ballot measure needs in order to pass. The default is a simple majority, i.e., "50% plus one vote". Other common thresholds are "three-fifths" and "two-thirds".

pro_statement
    **optional**
    Specifies a statement in favor of the referendum. It does not necessarily appear on the ballot (string).

summary_text
    **optional**
    Specifies a short summary of the ballot measure that is on the ballot, below the title, but above the text.

type
    **optional**
    Enumerated among:

    * ballot-measure: A catch-all for generic types of non-candidate-based contests.
    * initiative: These are usually citizen-driven measures to be placed on the ballot. These could include both statutory changes and constitutional amendments.
    * referendum: These could include measures to repeal existing acts of legislation, legislative referrals, and legislatively-referred state constitutional amendments.
    * other: Anything that does not fall into the above categories.

other_type
    **optional**
    Allows for cataloging a new type of ballot measure option, when type is specified as "other" (string).


CandidateContest
----------------

A subclass of ``ContestBase`` for repesenting a contest among candidates competing for election to a public office.

id
    Open Civic Data-style id in the format ``ocd-candidatecontest/{{uuid}}``.

filing_deadline
    **optional**
    Specifies the date and time when a candidate must have filed for the contest for the office (datetime).

is_runoff
    Indicates a contest to decide a prior contest that ended with no candidate receiving a majority of the votes (boolean).

is_unexpired_term
    Indicates that the former public office holder vacated the post before serving a full term (boolean).

number_elected
    **optional**
    Number of candidates that are elected in the contest, i.e. 'N' of N-of-M (integer).

post_ids
    **repeating**
    References to the OCD ``Posts`` representing the public offices for which the candidates are competing. If multiple, the primary post should be listed first, e.g., the id for the President post should be listed before the id for Vice-President.

party_id
    **optional**
    If the contest is among candidates of the same political party, e.g., a partisan primary election, reference to the OCD ``Party`` representing that political party.


PartyContest
------------

A subclass of ``ContestBase`` which describes a contest in which the possible ballot selections are all political parties. These could include contests in which straight-party selections are allowed, or party-list contests (although these are more common outside of the United States).

id
    Open Civic Data-style id in the format ``ocd-partycontest/{{uuid}}``.


RetentionContest
----------------

A subclass of ``BallotMeasureContest`` that represents a contest where a candidate is retained in a position, e.g. a judicial retention or recall election.

id
    Open Civic Data-style id in the format ``ocd-retentioncontest/{{uuid}}``.

candidacy_id
    Reference to the OCD ``Candidacy`` of the person who will either retain or lose a ``Post`` as a result of the contest.

post_id
    Reference to the OCD ``Post`` representing the public office the candidate will either retain or lose as a result of the contest.


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
    Specifics when the candidate filed for the contest (date).

is_incumbent
    **optional**
    Indicates whether the candidate is the incumbent for the office associated with the contest.

is_top_ticket
    **optional**
    Indicates that the candidate is the top of a ticket that includes multiple candidates (boolean). For example, the candidate running for President is consider the top of the President/Vice President ticket. In many states, this is also true of the Governor/Lieutenant Governor.

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


Party
-----

Political party with which candidates may be affiliated.

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


BallotSelectionBase
-------------------

A base class with the properties shared by all ballot selection types: ``BallotMeasureSelection``, ``CandidateSelection`` and ``PartySelection``.

id
    Open Civic Data-style id in the format ``ocd-ballotselection/{{uuid}}``.

contest_id
    References the ``BallotMeasureContest``, ``CandidateContest``, ``PartyContest`` or ``RetentionContest`` in which the ballot selection is an option.

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


BallotMeasureSelection
----------------------

A subclass of ``BallotSelectionBase`` representing a ballot option that a voter could select in a ballot measure contest.

id
    Open Civic Data-style id in the format ``ocd-ballotmeasureselection/{{uuid}}``.

selection
    Selection text for the option on the ballot , e.g., "Yes", "No", "Recall", "Don't recall" (string).


CandidateSelection
------------------

A subclass of ``BallotSelectionBase`` representing an option on the ballot that a voter could select in a candidate contest, e.g., a particular candidate or "ticket".

id
    Open Civic Data-style id in the format ``ocd-candidateselection/{{uuid}}``.

candidates
    **repeated**
    Lists each ``Candidate`` associated with the ballot selection. The number of candidates is unbounded in cases where the ballot selection is for a ticket, e.g. "President/Vice President", "Governor/Lt Governor". Has the following properties:

        candidate_id
            References the ``Candidate``.

        post_id
            References the ``Post`` that represents the public office for which the candidate is competing.

endorsement_party_ids
    **optional**
    **repeated**
    Lists each ``Party`` that endorsing the candidates associated with the selection. The number of parties is unbounded in cases where multiple parties endorse a single candidate/ticket.

is_write_in
    **optional**
    Indicates that the particular ballot selection allows for write-in candidates. If true, one or more write-in candidates are allowed for this contest (boolean).


PartySelection
--------------

A subclass of ``BallotSelectionBase`` representing an option on the ballot that a voter could select in a party contest.

id
    Open Civic Data-style id in the format ``ocd-partyselection/{{uuid}}``.

party_ids
    **repeated**
    Lists each ``Party`` associated with the ballot selection.


Differences with VIP
====================

Each of the data types described in this proposal corresponds to an element described in the VIP's current `XML format specification <http://vip-specification.readthedocs.io/en/vip5/xml/index.html#elements>`_. While interoperability with VIP data is a goal of this proposal, there is not a one-to-one mapping between the tags within a VIP element and the properties of its corresponding data type in this OCDEP.

First, a few general differences.

Our use cases require a model of public offices that persist from one election to the next. Thus, in place of VIP's `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element, this proposal describes reuse of OCD ``Post`` and ``Organization`` data types.

Similarly, this proposal swaps in OCD's ``Division`` type in place of the `<ElectoralDistrict> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/electoral_district.html>`_ and ``<GpUnit>`` (i.e., "Geo-political Unit") elements defined in the VIP and NIST specifications.

VIP describes `<InternationalizedText> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html>`_ and `<LanguageString> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/internationalized_text.html#languagestring>`_ elements for the purposes of representing certain texts in multiple languages, e.g., the English and Spanish translations of the ``pro_statement`` and ``con_statement`` of a ``BallotMeasureContest``. In this proposal, these data types are described as simple strings.

VIP describes an `<ExternalIdentifier> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/external_identifiers.html>`_ element, which allows connecting VIP data to external data sets. In place of this element, this proposal includes repeating ``indentifiers`` properties on data types that users may want to link to external data sets.

The detailed differences between VIP elements and their corresponding data type in this OCDEP are described below.

Election
--------

Corresponds to VIP's `<Election> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/election.html>`_ element.

* Important differences between corresponding fields:

    - ``<Name>`` is not required on VIP, but ``name`` is required on OCD's ``Event``.
    - ``<Date>`` is a typed as ``xs:date`` in VIP, but ``start_time`` is a datetime on OCD's ``Event``.

* OCD fields not implemented in VIP:

    - required:

        + ``classification`` inherited from ``Event`` and should always be "election".
        + ``timezone`` inherited from ``Event`` and should always be local to the state where the election occurs.

    - optional:

        + ``administrative_org_id``
        + ``description`` inherited from ``Event``
        + ``location`` inherited from ``Event``
        + ``all_day`` inherited from ``Event``
        + ``end_time`` inherited from ``Event``
        + ``status`` inherited from ``Event``
        + ``links`` inherited from ``Event``
        + ``participants`` inherited from ``Event``
        + ``documents`` inherited from ``Event``
        + ``media`` inherited from ``Event``

* VIP fields not implemented in this OCDEP:

    - ``<ElectionType>``, which is an optional string that conflates the level of government to which a candidate might be elected (e.g., "federal", "state", "county", etc.) with the point when the election occurs in the overall cycle (e.g., "general", "primary", "runoff" and "special"). If necessary, this could be stored in ``extras``.
    - ``<HoursOpenId>``, which is an optional reference to a VIP `<HoursOpen> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/hours_open.html>`_ element that represents when polling locations for the election are generally open. If necessary, this unique id and its associated VIP information could be stored in ``extras``.
    - ``<RegistrationInfo>``, which is an optional string. If the value is a URL, this could be stored in ``links`` or otherwise in ``extras``, if necessary.
    - ``<RegistrationDeadline>`, which is an optional date that could be stored in ``extras``, if necessary.
    - ``<HasElectionDayRegistration>``, which is an optional boolean that, if necessary, could be stored in ``extras``, if necessary.
    - ``<AbsenteeBallotInfo>``, which is an optional string. If the value is a URL, this could be stored in ``links`` or otherwise in ``extras``, if necessary.
    - ``<AbsenteeRequestDeadline>``, which is an optional date that, if necessary, could be stored in ``extras``, if necessary.
    - ``<ResultsUri>``, which is optional and could be stored in ``links`` or otherwise in ``extras``, if necessary.


ContestBase
-----------

Corresponds to VIP's `<ContestBase> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/contest_base.html>`_ element.

* Important differences between corresponding fields:

    - ``<ElectoralDistrictId>``, which is an optional reference to a VIP `<ElectoralDistrict> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/electoral_district.html>`_ element, is replaced by ``division_id``, which is a required reference to an OCD ``Division``. If necessary, VIP's ``<CandidateId>`` could be stored in ``extras``.

* OCD fields not implemented in VIP:

    - ``election_id`` is a required reference to an OCD ``Election``.

* VIP fields not implemented in this OCDEP:

    - ``Abbreviation``, which is an optional string that could be stored in ``extras``, if necessary.
    - ``<BallotSelectionIds>``, which is an optional single element that contains a set of references to ballot selections for the contest. Instead, ``BallotSelectionBase`` includes a single, required ``contest_id``.
    - ``<ElectorateSpecification>``, which an optional string that could be stored in ``extras``, if necessary.
    - ``<HasRotation>``, which is an optional boolean that could be stored in ``extras``, if necessary.
    - ``<BallotSubTitle>``,  which is an optional string that could be stored in ``extras``, if necessary.
    - ``<BallotTitle>``,  which is an optional string that could be stored in ``extras``, if necessary.
    - ``<SequenceOrder>``,  which is an optional integer that could be stored in ``extras``, if necessary.
    - ``<VoteVariation>``,  which is an optional reference to a VIP `<VoteVariation> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/vote_variation.html>`_ that could be stored in ``extras``, if necessary.
    - ``<OtherVoteVariation>``, which is an optional string that could be stored in ``extras``, if necessary.


BallotMeasureContest
--------------------

Corresponds to VIP's `<BallotMeasureContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_contest.html>`_ element.

* No important differences between corresponding fields.
* No other OCD fields not implemented in VIP.
* VIP fields not implemented in this OCDEP:
    
    - ``<InfoUri>``, which is optional and could be stored in in ``extras``, if necessary.


CandidateContest
----------------

Corresponds to VIP's `<CandidateContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<OfficeIds>``, which is an optional set of references to VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ elements, is replaced by ``post_ids``, which is a repeating field that requires at least one reference to an OCD ``Post``. If necessary, VIP's ``<OfficeIds>`` could be stored in ``extras``.

* OCD fields not implemented in VIP:

    - required:

        + ``is_runoff`` could be determined by the ``<ElectionType>`` or inferred from the date of the election.
        + ``is_unexpired_term`` could be determined by the ``<Name>`` or ``<ElectionType>`` (i.e., if either include the substring "special") or inferred from the date of the election.

    - optional:

        + ``filing_deadline`` is stored in the `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element in VIP.

* VIP fields not implemented in this OCDEP:

    - ``<VotesAllowed>``, which is an optional integer that could be stored in ``extras``, if necessary.


PartyContest
------------

Corresponds to VIP's `<PartyContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party_contest.html>`_ element.

* No important differences between corresponding fields.
* No other OCD fields not implemented in VIP.
* No other VIP fields not implemented in this OCDEP.


RetentionContest
----------------

Corresponds to VIP's `<RetentionContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/retention_contest.html>`_ element.

* Important differences between corresponding fields:

    - ``<CandidateId>``, which is a required reference to a VIP `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ element, is replaced by ``candidacy_id``, which is a required reference to an OCD ``Candidacy``. If necessary, VIP's ``<CandidateId>`` could be stored in ``extras``.
    - ``<OfficeId>``, which is an optional reference to a VIP `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_, is replaced by ``post_id``, which is a required reference to an OCD ``Post``. If necessary, VIP's ``<OfficeId>`` could be stored in ``extras``.

* No other OCD fields not implemented in VIP.
* No other VIP fields not implemented in this OCDEP.


Candidacy
---------

Corresponds to VIP's `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ element.

* Important differences between corresponding fields:

    - ``party_id`` is an optional reference an OCD ``Party``, not a VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ element. If necessary, VIP's ``<PartyId>`` could be stored in ``extras``.
    - ``person_id`` is a required reference an OCD ``Person``, not a VIP `<Person> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/person.html>`_ element. If necessary, VIP's ``<PersonId>`` could be stored in ``extras``.

* OCD fields not implemented in VIP:

    - required:
      
        + ``post_id`` is required to link the candidate to the public office for which they are competing. In VIP, this is represented as an `<Office> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/office.html>`_ element, which is stored on the ``<CandidateContest>`` element.

    - optional:
      
        + ``committee_id``

* VIP fields not implemented in this OCDEP:

    - ``<ContactInformation>`` refers to an element that describes the contact of physical address information for the candidate or their campaign. On and OCD ``Candidacy``, this information would be found on the associated ``Person`` or ``Committee`` object.
    - ``<PostElectionStatus>``, which is an optional reference to a VIP `<CandidatePostElectionStatus> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_post_election_status.html>`_ that could be stored in ``extras``, if necessary.
    - ``<PreElectionStatus>``, which is an optional reference to a VIP `<CandidatePreElectionStatus> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/enumerations/candidate_pre_election_status.html>`_ that could be stored in ``extras``, if necessary.


Party
-----

Corresponds to VIP's `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ element.

* Important differences between corresponding fields:

    - ``name`` is required.

* No other OCD fields not implemented in VIP.
* VIP fields not implemented in this OCDEP:
  
    - ``logo_uri``, which is optional and could be stored in in ``extras``, if necessary.


BallotSelectionBase
-------------------

Corresponds to VIP's `<BallotSelectionBase> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_selection_base.html>`_ element.

* No important differences between corresponding fields.
* OCD fields not implemented in VIP:

    - ``contest_id`` is required in order to link the selection to its associated contest. In VIP, this link is stored in `<OrderedContest> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ordered_contest.html>`_, which allows for modeling ballot layouts that vary between electoral districts, but is outside the scope of this proposal.

* Other VIP fields not implemented in this OCDEP:

    - ``<SequenceOrder>``, which is an optional integer that could be stored in in ``extras``, if necessary.


BallotMeasureSelection
----------------------

Corresponds to VIP's `<BallotMeasureSelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/ballot_measure_selection.html>`_ element.

* No important differences between corresponding fields.
* No other OCD fields not implemented in VIP.
* No other VIP fields not implemented in this OCDEP.


CandidateSelection
------------------

Corresponds to VIP's `<CandidateSelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate_selection.html>`_ element.

* Important differences between corresponding fields:

    - ``<CandidateIds>``, which is an optional set of references to VIP `<Candidate> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/candidate.html>`_ elements, is replaced by ``candidates``, which is a repeating field that requires at least one reference to an OCD ``Candidacy``. If necessary, VIP's ``<CandidateIds>`` could be stored in ``extras``.
    - ``<EndorsementPartyIds>``, which is an optional set of references to VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ elements, is replaced by ``endorsement_party_ids``, which is an optional repeating field that list references to each OCD ``Party`` endorsing the candidate(s). If necessary, VIP's ``<EndorsementPartyIds>`` could be stored in ``extras``.

* No other OCD fields not implemented in VIP.
* No other VIP fields not implemented in this OCDEP.


PartySelection
--------------

Corresponds to VIP's `<PartySelection> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party_selection.html>`_ element.

* Important differences between corresponding fields:

    - ``<PartyIds>``, which is an optional, set of references to VIP `<Party> <http://vip-specification.readthedocs.io/en/release/built_rst/xml/elements/party.html>`_ elements, is replaced by ``endorsement_party_ids``, which is an optional repeating field that list references to each OCD ``Party`` associated with the selection. If necessary, VIP's ``<PartyIds>`` could be stored in ``extras``.

* No other OCD fields not implemented in VIP.
* No other VIP fields not implemented in this OCDEP.


Copyright
=========

This document has been placed in the public domain per the `Creative Commons CC0 1.0 Universal license <http://creativecommons.org/publicdomain/zero/1.0/deed>`_.