API Search Endpoints
================

General information about search endpoints can be found at :ref:`search-endpoints` and :ref:`search-response`.

Information on common parameters can be found at :ref:`common-parameters`.

For advanced filtering refer to :ref:`parameters`, for looking up data by non-Open Civic Data IDs look at :ref:`id-operator`.

This page provides specific parameters and notes on which fields are included in the default response for each of the search endpoints.

.. _jurisdiction-search:

Jurisdiction Search
-------------------

**Endpoint:** ``/jurisdictions/``

**Default Fields:** All fields in :doc:`/data/jurisdiction` except for terms, session_details, and chambers.

**Sort Options:** Jurisdictions can only be sorted by name.

**Filter Parameters:** There are no filter parameters for jurisdictions.

.. _division-search:

Division Search
---------------

**Endpoint:** ``/divisions/``

**Default Fields:** `id`, `country`, and `display_name`

**Sort Options:** Divisions can only be sorted by their division ID.

**Filter Parameters:**

* `lat` & `lon` - Must be specified together.  The resulting divisions will all contain the specified point.
* `date` - For obtaining historical boundaries, divisions returned are based on boundaries at a given time. Must be specified in Y-m-d format.

.. _organization-search:

Organization Search
-------------------

**Endpoint:** ``/organizations/``

**Default Fields:** All fields in :doc:`/data/organization` except for contact_details, sources, posts,
founding_date, and dissolution_date.

**Sort Options:**

* `created_at` - Sort by time object was created, newest objects first. (default)
* `updated_at` - Sort by time object was updated, most recent first.

**Filter Parameters:**

* `classification`
* `founding_date`
* `dissolution_date`
* `jurisdiction_id`
* `parent_id`
* `division_id`
* `chamber`
* `name` - Exact match is not necessary, checks for case-insensitive substring matches.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.


.. _person-search:

Person Search
-------------

**Endpoint:** ``/people/``

**Default Fields:** All fields in :doc:`/data/person` except for contact_details, sources, extras,
links, birth_date, and death_date.

**Sort Options:**

* `created_at` - Sort by time object was created, newest objects first. (default)
* `updated_at` - Sort by time object was updated, most recent first.

**Filter Parameters:**

* `name`
* `gender`
* `birth_date`
* `death_date`
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.
* `member_of` - Parameter should be an Open Civic Data organization_id, will filter returned people
  to those that are a current member of the given organization.
* `ever_member_of` - Like member_of but checks all memberships, not only current ones.

.. _bill-search:

Bill Search
-----------

**Endpoint:** ``/bills/``

**Default Fields:** All fields in :doc:`/data/bill` except for sponsors, sources, actions, links,
versions, related_bills, summaries, other_titles, and documents.

**Sort Options:**

* `created_at` - Sort by time object was created, newest objects first. (default)
* `updated_at` - Sort by time object was updated, most recent first.

**Full Text Search:**

By specifying the `q` parameter a full text search can be performed against the text of the bill.

This parameter follows the following rules:

+----------------------+------------------------------------------------------------------------+
| search term          | result                                                                 |
+======================+============================+===========================================+
| `q=termA termB`      | termA and termB must be present                                        |
+----------------------+------------------------------------------------------------------------+
| `q=termA AND termB`  | termA and termB must be present, same as not specifying an operator    |
+----------------------+------------------------------------------------------------------------+
| `q=termA OR termB`   | termA or termB must be present                                         |
+----------------------+------------------------------------------------------------------------+
| `q="termA termB"`    | "termA termB" is interpreted as a single string that must be present   |
+----------------------+------------------------------------------------------------------------+
| `q=termA NOT termB`  | termA must be present without termB                                    |
+----------------------+------------------------------------------------------------------------+

Additionally, parentheses are allowed for grouping purposes.

**Filter Parameters:**

* `name`
* `chamber`
* `session`
* `jurisdiction_id`
* `type`
* `subject`
* `sponsors.id` - Open Civic Data person ID of a sponsor.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.

.. _vote-search:

Vote Search
-----------

**Endpoint:** ``/votes/``

**Default Fields:** All fields in :doc:`/data/vote` except for roll_call and sources.

**Sort Options:**

* `created_at` - Sort by time object was created, newest objects first. (default)
* `updated_at` - Sort by time object was updated, most recent first.
* `date` - Sort by date that the vote took place.

**Filter Parameters:**

* `jurisdiction_id`
* `date`
* `passed` - pass `true` to filter to only passed votes, pass `false` to get only failed votes
* `chamber`
* `session`
* `type`
* `bill.id` - Open Civic Data bill ID of bill vote is attached to.
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.


.. _event-search:

Event Search
------------

**Endpoint:** ``/events/``

**Default Fields:** All fields in :doc:`/data/event` except for sources.

**Sort Options:**

* `created_at` - Sort by time object was created, newest objects first. (default)
* `updated_at` - Sort by time object was updated, most recent first.
* `when` - Sort by when the event takes place.

**Filter Parameters:**

* `jurisdiction_id`
* `participants.id` - filter by Open Civic Data ID of a participant.
* `agenda.related_entities.id` filter by a related entity's Open Civic Data ID.
* `when`
* `updated_at` - See :ref:`timestamp-parameters`.
* `created_at` - See :ref:`timestamp-parameters`.


General Notes
-------------

.. _parameters:

Operators
~~~~~~~~~

All filter parameters are interpreted as direct lookups against the database unless otherwise noted.

Additionally, operators are available.  You can apply an operator by appending ``__op`` to the filter, so ``birth_date`` would become ``birth_date__gt`` if you wanted to use the greater than operator.

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
only return one item.)


.. _timestamp-parameters:

updated_at & created_at
~~~~~~~~~~~~~~~~~~~~~~~

These parameters are stored in the system as UTC timestamps, not strings.  The following formats are accepted:

* Y-m-d
* Y-m
* Y
* Y-m-dTH:M
* Y-m-dTH:M:S
* Y-m-dTH:M:S.f
* ``now``        - Special input interpreted as the current time. Useful for asking for events that haven't happened yet.

For details on time formats see `Python strftime() and strptime() behavior <http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior>`_.
