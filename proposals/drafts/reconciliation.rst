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

Different publishers of civic data often release data about the same
people or organizations. However, the data almost never use the same
identifiers. An end user who wants to use multiple data sources--say
researching the relation between campaign finances and electoral
success--has to do all the work of figuring out which records are
about the same people and organizations.

This record linkage task acts as major obstacle between the civic data
and the ultimate task that data users want to accomplish.

A reconciliation service would allow data publishers to coordinate, in
a loosely coupled way, to use the same identifiers to refer the same
people and organizations--removing this barrier for our data users.


Implementation
==============

Scope
-----

Let's start with politicians. Let's define a politician as someone who
has ever run elected office. (We need a tighter definition of "run for elected office")

API
---

match
_____

match endpoint can takes 1 or more match fields and returns possible matches with identifiers

GET

id
___

for a specific id return all the information we associated

if the id has been subsumed, 302 to the correct place

GET

mint
____

Submit minimum data fields for new entity return new id

maybe require a token from match?
 

merge
_____
submit identifiers, returns new identifier

POST


split
_____

submit arrays of reference identfiers from within a id and split into new ids, return new ids

POST

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

publishers will get notifications if the entities they uploaded are changed by another publisher, and can take action?


Bulk access
-----------

The underlying data for the service will be available as a daily backup

Backend
-------
The reconcilliation engine supporting this API will be unspecified.


Copyright of OCD identifiers
----------------------------

They will be dedicated to the public domain

Publisshers will need to agree that they will not upload data that is under copyright.










- https://web.archive.org/web/20161108220043/https://www.newschallenge.org/challenge/elections/entries/politician-reconciliation-service
- https://web.archive.org/web/20130609195642/https://www.newschallenge.org/open/open-government/submission/civic-data-standardization-bootstrapper/
- https://github.com/newsdev/nyt-entity-service
- https://github.com/pudo/nomenklatura
- google refine reconcilliation and freebase


Copyright
=========
This document has been placed in the public domain per the Creative Commons CC0 1.0 Universal license (http://creativecommons.org/publicdomain/zero/1.0/deed).


