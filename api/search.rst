Search Endpoints
================

.. caution::
    The OCD API is in beta and under very active development during 2015. Endpoints and queries may be added, altered, or removed.

This page describes each search endpoint, listing its parameters and noting which fields are included by default.

General information about search endpoints can be found at :ref:`endpoints` and :ref:`search-response`. Information on common parameters can be found at :ref:`common-parameters`.

For advanced filtering refer to :ref:`parameters`, for looking up data by non-Open-Civic-Data IDs look at :ref:`id-operator`.


.. _jurisdiction-search:

Jurisdiction Search
-------------------

**Endpoint:** ``/jurisdictions/``

**Default Fields:** `id`, `name`, `division`, `classification`, `url`, and `feature_flags`.

**Sort Options:** None; jurisdictions can only be sorted by name.

**Filter Parameters:** None.

.. _division-search:

Division Search
---------------

**Endpoint:** ``/divisions/``

**Default Fields:** `id`, `country`, and `name`.

**Sort Options:** None; divisions can only be sorted by division ID.

**Filter Parameters:**

* `lat` & `lon` - All divisions will contain the specified point. Must be specified together.

.. _organization-search:

Organization Search
-------------------

**Endpoint:** ``/organizations/``

**Default Fields:** `id`, `name`, `jurisdiction`, `classification`, `parent`, and `image`.

**Sort Options:** None.

**Filter Parameters:**

* `classification`
* `founding_date`
* `dissolution_date`
* `jurisdiction_id`
* `parent_id`
* `name` - Searches for case-insensitive substring matches.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.

.. _person-search:

Person Search
-------------

**Endpoint:** ``/people/``

**Default Fields:** `id`, `name`, `sort_name`, `memberships`, `gender`, and `image`.

**Sort Options:** None.

**Filter Parameters:**

* `name`
* `gender`
* `birth_date`
* `death_date`
* `member_of` - Parameter should be an Open Civic Data organization ID.
* `ever_member_of` - Like ``member_of`` but checks all memberships, not just current ones.
* `lat` & `lon` - Returns any people holding a post whose division's boundary contains the point. Must be specified together.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.

.. _bill-search:

Bill Search
-----------

**Endpoint:** ``/bills/``

**Default Fields:** `id`, `identifier`, `title`, `classification`, and `from_organization`.

**Sort Options:** None.

**Full Text Search:**

.. caution::
    As of May 2015, full text search is being written, but is not yet available.

By specifying the `q` parameter a full text search can be performed against the text of the bill.

This parameter follows the following rules:

+----------------------+------------------------------------------------------------------------+
| search term          | result                                                                 |
+======================+============================+===========================================+
| `q=termA termB`      | termA and termB must be present                                        |
+----------------------+------------------------------------------------------------------------+
| `q=termA AND termB`  | termA and termB must be present; same as not specifying an operator    |
+----------------------+------------------------------------------------------------------------+
| `q=termA OR termB`   | termA or termB must be present                                         |
+----------------------+------------------------------------------------------------------------+
| `q="termA termB"`    | "termA termB" is interpreted as a single string that must be present   |
+----------------------+------------------------------------------------------------------------+
| `q=termA NOT termB`  | termA must be present without termB                                    |
+----------------------+------------------------------------------------------------------------+

Additionally, parentheses are allowed for grouping purposes. For example, `q=(termA OR termB) NOT termC`.

**Filter Parameters:**

* `identifier`
* `chamber`
* `session`
* `jurisdiction_id`
* `classification`
* `subject`
* `sponsorships__person__id` - Open Civic Data person ID of a sponsor.
* `sponsorships__organization__id` - Open Civic Data organization ID of a sponsor.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.

.. _vote-search:

Vote Search
-----------

**Endpoint:** ``/votes/``

**Default Fields:** `id`, `bill`, `motion_text`, `motion_classification`, `result`, `counts`, `organization`, `start_date`, `created_at`, `updated_at`, and `extras`

**Sort Options:** None.

**Filter Parameters:**

* `jurisdiction_id`
* `start_date`
* `result` - Status of passage, including ``pass`` and ``fail``.
* `chamber`
* `session`
* `motion_classification`
* `bill_id` - Open Civic Data bill ID of bill this vote is attached to.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.


.. _event-search:

Event Search
------------

**Endpoint:** ``/events/``

**Default Fields:** `id`, `name`, `description`, `agenda`, `start_time`, `timezone`, `all_day`, `status`, and `classification`

**Sort Options:** None.

**Filter Parameters:**

* `participants_id` - filter by Open Civic Data ID of a participant.
* Filter by related entities by Open Civic Data ID
    * `agenda__related_entities__bill_id` - Filter by bill.
    * `agenda__related_entities__organization_id` - Filter by organization.
    * `agenda__related_entities__person_id` - Filter by person.
    * `agenda__related_entities__vote_id` - Filter by vote.
* `start_time`
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.


General Notes
-------------

.. _parameters:

Operators
~~~~~~~~~

All filter parameters are interpreted as direct lookups against the database unless otherwise noted.

Additionally, operators are available.  You can apply an operator by appending ``__operator`` to the filter, so ``birth_date`` would become ``birth_date__gt`` if you wanted to use the greater than operator.

Available operators are:

+----------+--------------------------------------------------------------------------------------+
| Operator | Function                                                                             |
+==========+======================================================================================+
| __gt     | Greater than.                                                                        |
+----------+--------------------------------------------------------------------------------------+
| __gte    | Greater than or equal to.                                                            |
+----------+--------------------------------------------------------------------------------------+
| __lt     | Less than.                                                                           |
+----------+--------------------------------------------------------------------------------------+
| __lte    | Less than or equal to.                                                               |
+----------+--------------------------------------------------------------------------------------+
| __ne     | Not equal to.                                                                        |
+----------+--------------------------------------------------------------------------------------+
| __all    | Content is split by ``,`` - filter ensures all values provided are in the object.    |
+----------+--------------------------------------------------------------------------------------+
| __in     | Content is split by ``,`` - filter includes objects with any of the values provided. |
+----------+--------------------------------------------------------------------------------------+
| __nin    | Content is split by ``,`` - filter excludes objects with any of the values provided. |
+----------+--------------------------------------------------------------------------------------+

.. _id-operator:

External IDs
~~~~~~~~~~~~

In addition to the Open Civic Data ID for an object, it is sometimes necessary to look up an object
by an external ID.  As objects are pulled into the system from other sources
(for example `Open States <http://openstates.org>`) we preserve their old IDs in the ``identifiers``
attribute on the object.  It is possible to query within this object by using ``id__<scheme>=<identifier>``
as a filter on any query.  For example ``/people/id__openstates=AKL000001`` would return the person that
had the Open States ID AKL000001.

(This typically shouldn't be combined with other filters since it should always
only return one item, similar to an object lookup.)


.. _timestamp-parameters:

updated_at & created_at
~~~~~~~~~~~~~~~~~~~~~~~

All objects have these fields, although by default they may not be in responses. These parameters are stored in the system as UTC timestamps, not strings, and can be denoted in any of these formats:

* Y-m-d
* Y-m
* Y
* Y-m-dTH:M
* Y-m-dTH:M:S
* Y-m-dTH:M:S.f
* ``now``        - Special input interpreted as the current datetime. Useful for asking for events that haven't happened yet.

For details on time formats see `Python strftime() and strptime() behavior <http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior>`_.
