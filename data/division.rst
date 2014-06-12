Division Objects
================

.. warning::
    Parts of Open Civic Data underwent a large refactor as of mid-2014, some information on this
    page may be out of date.   We're working on updating this documentation as soon as possible.

    We'll remove these messages from pages as they're updated and vetted.

Basic Details
-------------

**id**
    Open Civic Data division ID.

**country**
    Two-letter `ISO-3166 alpha-2 <http://en.wikipedia.org/wiki/ISO_3166-1>`_ country code.
    (e.g. 'us', 'ca')

**display_name**
    Human-readable name for division.

Additional Fields
-----------------

**geometries**
    A list of associated geometries, each of which has the following fields:

    **start**
        Best approximation of date boundary became effective.
    **end**
        Best approximation of date boundary was replaced or made obsolete (null for current boundaries).
    **boundary**
        Boundary object- fields are determined from underlying data source, but always provides:

        **centroid**

        Object containing the centroid, not guaranteed to be within the object.

        Example::

            { "type": "Point", "coordinates": [-176.59989528409687, 51.88215100813731] }

        **extent**

        Object describing the extents.  [left-most, lower-most, right-most, upper-most]

        Example::

            [ -176.71309799999997, 51.80080899999999, -176.46673599999997, 51.95761899999999 ]


**children**
    A list of child jurisdiction ids.
