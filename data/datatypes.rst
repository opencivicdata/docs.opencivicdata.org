Data Types
========== 

.. warning::
    Parts of Open Civic Data underwent a large refactor as of mid-2014, some information on this
    page may be out of date.   We're working on updating this documentation as soon as possible.

    We'll remove these messages from pages as they're updated and vetted.

The Open Civic Data specifications define the following core types:

**division**
    A political geography such as a state, county, or congressional district.  May have multiple
    boundaries over their lifetime. 

    Division IDs take the form ``ocd-division/country:<country_code>[<type>:type_id>]+``.  The canonical repository of division IDs is `opencivicdata/ocd-division-ids <https://github.com/opencivicdata/ocd-division-ids>`_ You can also look up a division id using `the Open Civic Data editor and lookup tool <http://editor.opencivicdata.org/geo/select/>`_.
    
**jurisdiction**
    A governing body that exists within a division.
    While 'Florida' would be a division, the Florida State Legislature would be a jurisdiction.

    Jurisdictions IDs take the form ``ocd-jurisdiction/<jurisdiction_id>/<jurisdiction_type>`` where ``jurisdiction_id`` is the ID for the related division without the `ocd-division/` prefix and ``jurisdiction_type`` is `council`, `legislature`, etc.

**person**
    A person, typically a politician or government official.

    The `Popolo person schema <http://popoloproject.com/specs/person.html>`_ is used to represent
    person data.

**organization**
    A group of people, such as a city council, state senate, or committee.

    The `Popolo organization schema <http://popoloproject.com/specs/organization.html>`_ is used to
    represent organization data.

**bill**
    A legislative document and its history, may technically be a resolution, appointment, or contract
    so long as it has a name and would be considered to have a legislative history.

    See :doc:`bill` for details.

**vote**
    The record of a vote taken on a motion, such as a confirmation or passage of a bill.
    May contain individual legislator's yay/nay votes or just an outcome.

    See :doc:`vote` for details.

**event**
    A legislative event, such as a meeting or hearing.

    See :doc:`event` for details.
