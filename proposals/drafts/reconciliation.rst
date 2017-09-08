=============================
OCDEP: Reconciliation Service
=============================

:Created: 2016-12-28
:Author: Forest Gregg, `DataMade <http://datamade.us/>`_
:Status: Proposed

Overview
========

Technical specification for a entity reconciliation service for Open
Civic Data identifiers and governance for managing those identifiers.


Rationale
=========

Publishers of civic data often release data about the same set of
people and organizations. Different sources almost never use the same
identifiers, leaving it to end users to attempt to combine data.

This record linkage task is difficult and, at scale, is beyond the
ability and resources available to most data users.  This obstacle
prevents many of the uses that civic data publishers would like their
data to enable.

A reconciliation service would allow data publishers to coordinate, in
a loosely coupled way, to use the same identifiers to refer the same
people and organizations--removing obstacle for data users.


Implementation
==============

Scope
-----

This current proposal is limited to a service to support common
identifiers for politicians. In the future it may be extended to other
types of civic entities.

For our purposes, a politician is person who has formed a political
committee to pursue elected office. This definition should be adequate
for the current target set of publishers those who publish data on
campaign finance, electioneering, election results, and legislative
actions. Individual campaign donors, lobbyists, civil servants,
campaign operatives are currently not in scope.


Reconciliation Service
----------------------

The reconciliation service will be a web service that data publishers
will largely interact with through a REST API. 

While, the internal implementation details of the service are outside
of the scope of this proposal, this proposal will discuss data access
provisions necessary to allow for continuity if the service provider
is unable or unwilling to maintain the service.


API
---

.. http:get:: /search

   Attempts to find the ocd identifier for a politician

   :query name: a name of the politician
   :query jurisdiction_id: an OCD id for the jurisdiction of the organization that the politician is seeking election into or is a member of
   :query role: (optional) a name of the role associated with a post
   :query active_date: (optional) a date, date range, year, year range
                       when the politician was seeking or held this
                       role
   :query post_label: the label of the post
   :query birth_date: (optional) the birth date of the politician
   :status 200 OK: no error, returns a list of possible ids with match scores
   :status 404 Not Found: could not find any possible matches
   :status 402 Payment required: If the balance between data added (puts and posts on `/identifier`) and searches is out of wack. This reduce
   :status 429 Too Many Requests: Rate limiting

   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Balance: Balance between data added and data searched
		       

   **Example request**:

   .. sourcecode:: http

      GET /search?jurisdiction_id=ocd-jurisdiction/country:us/state:il/place:chicago/government&name="Ed Burke" HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [{"politician": {"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",
                      "name": "Ed Burke",
                      "ocd_id": "ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2"
                      "birth_date": null,
                      "posts": {"role": "Alderman", "label": "Ward 3"}
                      },
        "match_score": 0.74}
      ]			  

.. http:get:: /identifier/(str:ocd_identifier)

   Shows all existing records and linkage history for a politician

   :param ocd_identifier: politician's OCD identifier
   :type ocd_identifier: str
   :status 200 OK: no error
   :status 404 Not Found: no politician with that identifier found
   :status 301 Moved Permanently: if an ocd_identifier has been merged into another identifier, redirect to :http:get:`/identifier/(str:new_ocd_identifier)`
   :status 300 Multiple Choices: this id has split, return options				  

.. http:post:: /identifier

   Mint new ocd identifier 

   :form name: a name of the politician
   :form jurisdiction_id: an OCD id for the jurisdiction of the organization that the politician is seeking election into or is a member of
   :form office: (optional) a name of the office
   :form birth_date: (optional) the birth date of the politician
   :form active_date: (optional) a date, date range, year, year range when the politician was seeking or held this office
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: returns ocd_identifier

.. http:put:: /identifier/(str:ocd_identifier)

   Add data about politician

   :param ocd_identifier: politician's OCD identifier
   :type ocd_identifier: str
   :form name: a name of the politician
   :form jurisdiction_id: an OCD id for the jurisdiction of the organization that the politician is seeking election into or is a member of
   :form office: (optional) a name of the office
   :form birth_date: (optional) the birth date of the politician
   :form active_date: (optional) a date, date range, year, year range when the politician was seeking or held this office
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: return record id

.. http::delete:: /identifier/(str:ocd_identifier)

   Delete the record from politician id

.. http:post:: /merge

   Merges identifiers

   :form ids: array of ids to merge
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: returns surviving ocd_identifier 
			
.. http:post:: /split/(str:ocd_identifier)

   Split identifiers. This will create new ids for both sides of the split.
   The old id will return a 300

   :param ocd_identifier: politician's OCD identifier
   :type ocd_identifier: str
   :form ids: array of reference ids to remove and turn into new id
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: returns new ocd_identifiers for both sides of the split
			
 

Governance
__________

mint, merge, and split are powerful claims that can will affect other users.

proposed permission model

unprivileged

- match methods
- id methods

publisher

- mint method
- merge method
- split method

publishers will get notifications if the entities they uploaded are
changed by another publisher, and can take action.


Bulk access
-----------

The underlying data for the service will be available as a daily backup



Copyright of OCD identifiers
----------------------------

They will be dedicated to the public domain

Publisshers will need to agree that they will not upload data that is
under copyright, and agree to dedicate all data to the public domain. 









- http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414
- https://web.archive.org/web/20161108220043/https://www.newschallenge.org/challenge/elections/entries/politician-reconciliation-service
- https://web.archive.org/web/20130609195642/https://www.newschallenge.org/open/open-government/submission/civic-data-standardization-bootstrapper/
- https://github.com/newsdev/nyt-entity-service
- https://github.com/pudo/nomenklatura
- google refine reconcilliation and freebase


Copyright
=========
This document has been placed in the public domain per the Creative Commons CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).


