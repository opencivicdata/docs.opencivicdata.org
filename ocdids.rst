.. _ocdid:

===============
OCD Identifiers
===============

Open Civic Data Identifiers (or OCD IDs) are a common Identifier format used
in the OpenCivicData projects, in a defined format, ripe for reuse with
any legislative dataset.

Creating a new OCD ID
---------------------

Consensus on IDs is needed for a few of the types, but other IDs may be
issued without any concern at all. The following is a helpful table of when
it's OK (and not OK) to create new IDs without reaching rough consensus.

+-----------------+-------------------------------+
| OCD ID Type     | Can issue new ID              |
+=================+===============================+
| person          | Yes (UUID1)                   |
+-----------------+-------------------------------+
| organization    | Yes (UUID1)                   |
+-----------------+-------------------------------+
| division        | No (Needs to undergo a review |
|                 | and survey of entries at that |
|                 | geopolitical level)           |
+-----------------+-------------------------------+
| jurisdiction    | No (needs to undergo a review |
|                 | to ensure we have consistent  |
|                 | names for legislative bodies  |
+-----------------+-------------------------------+

If you need to create a new ID that requires rough consensus, emailing the
`OpenCivic Data Mailing List <https://groups.google.com/forum/#!forum/open-civic-data>`_
with as much detail regarding the situation as you can generally proves
to be the best way to solicit feedback.

General Format
--------------

OCD IDs have the general format of:

``ocd-${type}/${data}``. Some valid types are ``division``, ``jurisdiction``,
and ``person``. Each type has its own format (for the data half of the ID),
and a brief overview can be found below.


Division IDs
------------

Division IDs are one of the more common OpenCivic identifiers. Division IDs
denote a particular geopolitical division. Information regarding valid
Division IDs can be found in the
`ocd-division-ids repo <https://github.com/opencivicdata/ocd-division-ids>`_.

The general format is:

``ocd-division/country:<country_code>[/<type>:<type_id>]+``.

``country_code`` must be a valid ISO 3166-1 alpha-2 code for the country.
``type`` shall be the type of boundary (such as ``country``, ``state``,
``city``), while ``type_id`` shall be the unique ID for the entity at this
level.

For more information on what exactly is correct in this format, please
do take a look at the
`ocd-division-ids repo <https://github.com/opencivicdata/ocd-division-ids>`_.


Jurisdiction IDs
----------------

Jurisdiction IDs are based on the Division IDs, but have a slightly adjusted
format. The ``type`` shall be set to ``jurisdiction``, and the data half of the
ID shall have a trailing ``type``, which matches the jurisdiction type. Currently,
the only used types are ``legislature`` and ``council``.

The ID looks something like
``ocd-jurisdiction/country:us/state:ex/place:example``.

This format isn't fully formalized yet, so please take care when using
these.


Person IDs, Org IDs
-------------------

The valid types are ``person`` for a Person, and ``organization`` for an
Organization.

Person and Org IDs contain a UUID for the data-part, created by pupa
using ``uuid.uuid1``.

An example of a valid OCD Person ID is
``ocd-person/ebaff054-05df-11e3-a53b-f0def1bd7298``.
