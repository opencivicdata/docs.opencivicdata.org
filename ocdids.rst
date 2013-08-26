
.. _ocdid:

OCD Identifiers
------------------------------------------

General Format
==============

OCD IDs have the general format of:

`ocd-${type}/${data}`. Some valid types are `division`, `jurisdiction`, and
`person`. Each type has it's own format (for the data half of the ID), and
a brief overview can be found below.


Division IDs
============

Division IDs are one of the more common OpenCivic identifiers. Division IDs
denote a particular geopolitical division. Information regarding valid
Division IDs can be found in the
`ocd-division-ids repo <https://github.com/opencivicdata/ocd-division-ids>`_.

The general format is:

`ocd-division/country:<country_code>[/<type>:<type_id>]+`.

`country_code` must be a valid ISO 3166-1 alpha-2 code for the country.
`type` shall be the type of boundary (such as `country`, `state`,
`city`), while `type_id` shall be the unique ID for the entity at this level.

For more information on what exactly is correct in this format, please
do take a look at the
`ocd-division-ids repo <https://github.com/opencivicdata/ocd-division-ids>`_.


Jurisdiction IDs
================

Jurisdiction IDs are based on the Division IDs, but have a slightly adjusted
format. The `type` shall be set to `jurisdiction`, and the data half of the
ID shall have a trailing `type`, which matches the jurisdiction type. Currently,
the only used types are `legislature` and `council`.

The ID looks something like
`ocd-jurisdiction/country:us/state:ex/place:example`.
