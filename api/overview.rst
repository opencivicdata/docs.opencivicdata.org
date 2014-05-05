API Overview
============

The Open Civic Data API is a JSON API that provides search and lookup across all information
captured by the project.

Basics
------

* All responses are JSON unless otherwise specified.
* Errors will be returned with 400 status code and a JSON object containing an 'error' key with a
  human-readable description of the error that occured.
* An API key is required, it should be passed as the parameter ``apikey`` or the header ``X-APIKEY``.  A key can be obtained at `https://sunlightfoundation.com/api/ <https://sunlightfoundation.com/api/>`_.
* All changes to the API will be announced on the `Open Civic Data Google Group <https://groups.google.com/forum/?fromgroups#!forum/open-civic-data>`_.

.. _endpoints:

Endpoints
---------

The Open Civic Data API consists of two types of endpoints, search and object lookup.

.. _object-endpoints:

Object Lookup Endpoints
~~~~~~~~~~~~~~~~~~~~~~~

Object lookup endpoints can be thought of as permanent URIs for objects, they take the form ``https://api.opencivicdata.org/<ocd-id>`` and return a single JSON object.

.. note:
    A plain HTTP endpoint is also available, but HTTPS is considered the default.

.. _search-endpoints:

Search Endpoints
~~~~~~~~~~~~~~~~

Search endpoints are in the form ``https://api.opencivicdata.org/<type>/?<parameters>``.

(For example: ``https://api.opencivicdata.org/people/?name=Obama`` would return legislators named 'Obama'.)

The search endpoints are:

+----------------------+----------------------------+-------------------------------+
| Search Endpoint      | Object Description         | Details                       |
+======================+============================+===============================+
| ``/jurisdictions/``  | :doc:`../data/jurisdiction`| :ref:`jurisdiction-search`    |
+----------------------+----------------------------+-------------------------------+
| ``/divisions/``      | :doc:`../data/division`    | :ref:`division-search`        |
+----------------------+----------------------------+-------------------------------+
| ``/organizations/``  | :doc:`../data/organization`| :ref:`organization-search`    |
+----------------------+----------------------------+-------------------------------+
| ``/people/``         | :doc:`../data/person`      | :ref:`person-search`          |
+----------------------+----------------------------+-------------------------------+
| ``/bills/``          | :doc:`../data/bill`        | :ref:`bill-search`            |
+----------------------+----------------------------+-------------------------------+
| ``/votes/``          | :doc:`../data/vote`        | :ref:`vote-search`            |
+----------------------+----------------------------+-------------------------------+
| ``/events/``         | :doc:`../data/event`       | :ref:`event-search`           |
+----------------------+----------------------------+-------------------------------+

.. _search-response:

Search Response Format
~~~~~~~~~~~~~~~~~~~~~~

All search endpoints return paginated responses in the following format:

.. code-block:: javascript

    {
        "meta": {
            "count": 100,           // number of items on current page
            "per_page": 100,        // max number of items per page
            "page": 0,              // current page number (0-indexed)
            "max_page": 1,          // maximum ?page=<page> parameter
            "total_count": 180,     // total number of objects returned by query
        },
        "results": [ ... ]          // list of result objects
    }

.. _common-parameters:

Common Parameters
-----------------

The following (optional) parameters are common across API endpoints:

**fields**
    The fields parameter can be used to specify which fields you want to be returned in the
    response.  Specifying the desired fields is a useful tool for cutting down on bandwidth,
    especially for mobile applications.

    By default, search responses return a somewhat minimal representation of each object, that
    subset can be shrunk or expanded via fields.  Similarly, an object lookup response returns
    the complete object, but if only a subset is needed ``fields`` can be used to scale down
    the response size.

    Examples:

    * specifying ``?fields=name`` will only return the ``name`` field (and any required fields,
      like ``id``)
    * specifying ``?fields=created_at,memberships.organization_id`` would just include
      the three fields ``created_at`` and ``memberships.organization_id``.
      Note that ``memberships`` may not be included in the default search response but fields is
      used here to grab a superset (and in this case, a portion of an object as well).

    Note: some fields (such as ``id``) are required and will always be returned regardless of
    their inclusion in ``fields``.

**callback**
    The callback parameter is used for making `JSONP <https://en.wikipedia.org/wiki/JSONP>`_
    requests.

**sort**
    Change the sort order of objects returned via a search endpoint.  See :doc:`search` for
    available values for each endpoint
**page**
    Select a page (0-``meta.max_page``) from the result set in a search endpoint.
**per_page**
    Select a number of items per page (1-100) from the result set in a search endpoint.
