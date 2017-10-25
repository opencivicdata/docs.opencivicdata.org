
==============
OCDEP: Division Identifier Governance
==============

:Created: 2017-10-24
:Author: Donny Bridges
:Status: Proposed

Overview
========

A formalized governance model for the creation, acceptance, and upkeep of Open Civic Data Division Identifiers (OCDIDs).

Rationale
=========

Recently, a number of civic data organizations, tech companies, and US state governments have expressed interest in taking a greater role in the creation, upkeep, and wider adoption of OCDIDs. Currently, the governance structure for division IDs  as defined in OCDEP2 is "informal... led by the project’s early contributors and informed by the Open Civic Data Google Group." Increased adoption and interest makes this informality untenable for reasons including:

* Bottlenecks arising when large amounts of new identifiers are proposed but only a few people have permission to review and approve pull requests.
* Subject-matter experts and organizations that have extensive experience working with OCDIDs are willing to take greater responsibility, but currently do not have a formal path for doing so.
* Government entities and other local experts who may wish to contribute to the OCDID repository do not have a clear idea of how the process for contirbution works, making it more difficult for them to justify contributing.

We propose to formalize this structure in order to relieve some of the burden on those currently responsible for maintaining the repository, as well as allowing those whose work depends on OCDIDs to have more direct control on their upkeep.


Implementation
==============

Roles & Responsibilities
------------------------
``User``
~~~~~~~~
Anyone using OCDIDs may contribute through Slack/Google group discussion, reporting issues, or assisting with subject-matter expertise.
These channels for communication will be publicaly displayed on the Open Civic Data website.

``Contributor``
~~~~~~~~~~~~~~~
Any individual or organization ``user`` may become a ``contributor`` by submitting a pull request adding, correcting, or aliasing jurisdictional OCDIDs.
First time ``contributors`` will be advised to consult with an existing ``committer`` before submitting their first PR.

``Committer`` 
~~~~~~~~~~~~~
``Committers`` have the ability to approve and commit pull requests from ``contributors`` and other ``committers``. 
An initial cohort of ``committers`` will be determined by current project contributors.
Any individual or organization who is a ``contributor`` and who agrees to the repsonsibilities listed here may apply to become a ``committer``. 
* There will be a two month period where existing ``committers`` may raise objections to an applicant, otherwise the applying organization/individual will be considered approved.
* In the case that an objection is raised, a discussion and vote will be had amongst existing ``committers``, with a simple majority necessary for approval.
``Committers`` will be approved on an organizational basis, unless explicitly noted for an individual.
* Multiple members of an organization may have committing ability, but the organization itself will be counted for all voting and approval processes.
* Organizations will be asked to designate a primary point of contact who will act on behalf of the organization in procedural matters.
``Committers`` are expected to participate in approval, support, maintenance, and other community related activities or may have their ``committer`` status revoked. 
* ``Committers`` will have their status reviewed on a calendar year basis. 

Contribution Process
--------------------
General contributions
~~~~~~~~~~~~~~~~~~~~~
Any ``contributor`` may create a pull request for generative IDs, corrections, aliases, etc. 

* A pull request from a ``contributor`` will be considered accepted when reviewed by and approved by two ``committers``.
* If the contribution is from a current ``committer`` in good standing, only one additional ``committer`` review is necessary.
* No two members of the same organization may be involved in the acceptance of a pull request.

Commits should be reviewed within 2 weeks of a pull request. Accellerated timeline needs should be communicated via Slack/email.

* If, after two months there is neither a formal approval or an ongoing conversation around a request, that request will be considered accepted.
* If a conversation around a request cannot reach consensus, after two months the ``contributor`` may request a final vote from the cohort of existing ``committers``.

Approval will be handled on a per-file, rather than a per-commit, basis.

New commits should include have a well-formed explanations, especially if generating new IDs or types.

Formalized guidelines for approval will be created for use by ``committers``. These guidelines will include:

* Syntax check guidelines
* Type check guidelines and a glossary of existing types
* Dupe check guidelines
* Instructions for including and checking for correct sameAs aliasing
* Differentiating standards of review between generative/corrective requests

Government contributions
~~~~~~~~~~~~~~~~~~~~~~~~
Should a government entity wish to contribute to the repository, they will initially be asked to work directly with an existing ``committer`` to prepare to integrate their identifier set.

* A second ``committer`` is still required for approving government contributions, even if a government contributor becomes a ``committer`` themselves.
* Even so, government contributors should be given wide deference within their geographic area.
* If, because of naming conventions, geographic edge cases, etc. a government contributor requests a deviation from existing OCDID nomenclature, the community will attempt to reasonably accommodate that request (e.g. using “police_jury” as a type in lieu of “county_council” for Louisiana's county legislative body)

Government entities (and the ``committers`` they work with) will be expected to reconcile and appropriately alias these cases with existing OCDIDs in order to ensure maximum compatibility.

Identifiers created by government officials that are used in official data will be marked as such in the repository, so that developers can quickly identify the preferred identifier in case of conflict. Caution should be used, and the orginal submitter consulted with if possible, before changing government submitted identifiers.

A section of documentatoin specifically aimed at government staff will be created, where they can learn more about the project and how to get involved, as well as how to reach out to the community to get help.

Support
--------
``Committers`` will be required to participate in a quarterly review of new OCDIDs in order to ensure quality on-going.
``Committers`` will be requested to contribute and maintain an ongoing style guide for creating new district types.
``Committers`` will be required to participate in > 60% of all formal votes/actions as announced.


Copyright
=========

This document has been placed in the public domain per the Creative Commons
CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).
