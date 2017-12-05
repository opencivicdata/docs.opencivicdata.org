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
   :status 429 Too Many Requests: Rate limiting

   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Balance: Balance between data added (search requests) and data searched (identifier post)
		       

   **Example request**:

   .. sourcecode:: http

      GET /search?jurisdiction_id=ocd-jurisdiction/country:us/state:il/place:chicago/government&name="Ed Burke" HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/json

      [{"best reference": {"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",  
                           "name": "Ed Burke",
                           "birth_date": null,
                           "post": {"role": "Alderman", "label": "Ward 3"}
                          },
	"ocd_id": "ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2",
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

   **Example request**:

   .. sourcecode:: http

      GET /identifier/ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2 HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/json

      {"references": [{"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",  
                       "name": "Ed Burke",
                       "birth_date": null,
                       "post": {"role": "Alderman", "label": "Ward 3"}
                       }],
       "ocd_id": "ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2"}


.. http:post:: /identifier

   Mint new ocd identifier 

   :form name: a name of the politician
   :form jurisdiction_id: an OCD id for the jurisdiction of the organization that the politician is seeking election into or is a member of
   :form post: (optional) a name of the office
   :form birth_date: (optional) the birth date of the politician
   :form active_date: (optional) a date, date range, year, year range when the politician was seeking or held this office
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: returns ocd_identifier
   :status 412 Precondition Failed: required information is missing or malformed
   :status 401 Unauthorized: missing or invalid authorization token

   **Example Request**:

   .. sourcecode:: http
			
      POST /identifier HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript
      Content-Type: application/json
      Authorization: "Authorization: credentials"

      {"name": "Danny Solis",
       "jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",
       "post": {"role": "Alderman", "label": "Ward 14"}}

   **Example Response**:
       
      HTTP/1.1 201 OK
      Vary: Accept
      Content-Type: text/json

      {"ocd_id": "ocd-person/v12caddf-gdag-2faf-147d-bfas84e096e2"}

.. http:put:: /identifier/(str:ocd_identifier)

   Add data about politician

   :param ocd_identifier: politician's OCD identifier
   :type ocd_identifier: str
   :form name: (optional) a name of the politician
   :form jurisdiction_id: an OCD id for the jurisdiction of the organization that the politician is seeking election into or is a member of
   :form office: (optional) a name of the office
   :form birth_date: (optional) the birth date of the politician
   :form active_date: (optional) a date, date range, year, year range when the politician was seeking or held this office
   :reqheader Authorization: OAuth token to authenticate		      
   :status 200 Created: return record

   **Example Request**:
			
   .. sourcecode:: http
			
      PUT /identifier/ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2 HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript
      Content-Type: application/json
      Authorization: "Authorization: credentials"

      {"name": "Edward Burke",
       "ocd-jurisdiction/country:us/state:il/place:chicago/government"}

   **Example Response**:
       
      HTTP/1.1 201 OK
      Vary: Accept
      Content-Type: text/json

      {"references": {109234: {"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",  
                               "name": "Ed Burke",
                               "birth_date": null,
                               "post": {"role": "Alderman", "label": "Ward 3"}
                               },
		      109236:  {"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",  
                                "name": "Edward Burke",
                                "birth_date": null,
                                "post": null
                                }},
       "ocd_id": "ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2"}			

.. http::delete:: /identifier/(str:ocd_identifier)

   Delete the record from politician id

   :reqheader Authorization: OAuth token to authenticate		      
   :status 204 No Content: delete identifier

.. http:post:: /merge

   Merges identifiers

   :form ids: array of ids to merge
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: returns surviving ocd_identifier 

   **Example Request**:
			
   .. sourcecode:: http
			
      POST /merge HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript
      Content-Type: application/json
      Authorization: "Authorization: credentials"

      ["ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2", "ocd-person/v12caddf-gdag-2faf-147d-bfas84e096e2"]

   **Example Response**:
       
      HTTP/1.1 201 OK
      Vary: Accept
      Content-Type: text/json

      {"references": {109234: {"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",  
                               "name": "Ed Burke",
                               "birth_date": null,
                               "post": {"role": "Alderman", "label": "Ward 3"}
                               },
		      109236: {"jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",  
                               "name": "Edward Burke",
                               "birth_date": null,
                               "post": null
                               },
		      109235: {"name": "Danny Solis",
                               "jurisdiction_id": "ocd-jurisdiction/country:us/state:il/place:chicago/government",
                               "post": {"role": "Alderman", "label": "Ward 14"}},
       "ocd_id": "ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2"}			
			
.. http:post:: /split/(str:ocd_identifier)

   Split identifiers. This will create new ids for both sides of the split.
   The old id will return a 300

   :param ocd_identifier: politician's OCD identifier
   :type ocd_identifier: str
   :form ids: array of reference ids to remove and turn into new id
   :reqheader Authorization: OAuth token to authenticate		      
   :status 201 Created: returns new ocd_identifiers for the split
			
   .. sourcecode:: http
			
      POST /split/ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2 HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript
      Content-Type: application/json
      Authorization: "Authorization: credentials"

      [109235]

   **Example Response**:
       
      HTTP/1.1 201 OK
      Vary: Accept
      Content-Type: text/json

      {"ocd_id": "ocd-person/912c8ddf-8d04-4f7f-847d-2daf84e096e2"}
 

Governance
__________

`mint`, `merge`, and `split` are powerful claims that should be reserved
to trusted publishers. 

Publishers will get notifications if the entities they uploaded are
changed by another publisher.


Bulk access
-----------

The underlying data for the service will be available as a daily backup


Copyright of OCD identifiers
----------------------------

They will be dedicated to the public domain

Publishers will need to agree that they will not upload data that is
under copyright, and agree to dedicate all data to the public domain. 


Copyright
=========
This document has been placed in the public domain per the Creative Commons CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).


