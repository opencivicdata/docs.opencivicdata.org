Open Civic Data API Overview
============================

.. caution::
    The OCD API is in beta and under very active development during 2015. Endpoints and queries may be added, altered, or removed.

The Open Civic Data API is a JSON API that provides search and lookup across all information
captured by the project.

Basics
------

* All responses are JSON unless otherwise specified.
* Errors will be returned with 400 status code and a JSON object containing an 'error' key with a
  human-readable description of the error that occured.
* An API key is required, it should be passed as the parameter ``apikey`` or the header ``X-APIKEY``.  A key can be obtained at `https://sunlightfoundation.com/api/ <https://sunlightfoundation.com/api/>`_.
* Major changes to the API will be announced on the `Open Civic Data Google Group <https://groups.google.com/forum/?fromgroups#!forum/open-civic-data>`_.

.. _endpoints:

Endpoints
---------

The Open Civic Data API consists of two types of endpoints: search, and object lookup.

Object lookup endpoints can be thought of as permanent URIs for objects, they take the form ``https://api.opencivicdata.org/<ocd-id>`` and return a single JSON object.

Search endpoints are in the form ``https://api.opencivicdata.org/<type>/?<parameters>``. For example: ``https://api.opencivicdata.org/people/?name__contains=Obama`` would return a list of all legislators named 'Obama'.

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

.. note::
    Plain HTTP endpoints are available, but HTTPS is recommended and considered the default.

.. _search-response:

Search Response Format
~~~~~~~~~~~~~~~~~~~~~~

All search endpoints return paginated responses in the following format:

.. code-block:: javascript

    {
        "meta": {
            "count": 100,           // number of items on current page
            "per_page": 100,        // max number of items per page
            "page": 1,              // current page number (1-indexed)
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
    The ``fields`` parameter can be used to specify which fields you want to be returned in the
    response.  Requesting only specific fields is a useful tool for cutting down on bandwidth,
    especially for mobile applications.

    An object lookup returns all of that object's fields, but if only a subset is needed ``fields`` can be used to limit these. Search endpoint responses return only a few fields by default, but that subset can be shrunk or expanded via ``fields``.

    Examples:

    * Specifying ``?fields=name`` will only return the ``name`` field.
    * Specifying ``?fields=created_at,memberships__organization_id`` will only include
      the fields ``created_at`` and ``memberships__organization_id``. Note that ``memberships`` cannot be included normally, but ``fields`` is used here to perform a join.

**sort**
    Change the sort order of objects returned via a search endpoint.  See :doc:`search` for
    available values for each endpoint.

**page**
    Select a page (1-``meta.max_page``) from the result set in a search endpoint.

**per_page**
    Select a number of items per page (1-100) from the result set in a search endpoint.
