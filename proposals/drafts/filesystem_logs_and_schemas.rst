=======================================================
OCDEP: Open Civic Data Filesystem Logs and Schemas
=======================================================
:Created: 2025-12-11
:Author: Tamara Dowis, Sartaj Chowdhury
:Status: Draft

Abstract
========

This proposal describes a filesystem-based representation for legislative datasets, including append-only log records and JSON Schemas used to validate each file type.

Specifically, the proposal outlines:

#. A canonical path structure for organizing legislative data
#. A self-contained log entry format that remains interpretable when extracted from its original path context
#. JSON Schemas corresponding to each standardized file type

The goal is to support bulk access, reproducibility, and file-based analytics workflows (for example, using tools such as DuckDB), while remaining aligned with existing OCD identifiers and object models.

Non-goals
=========

The following items are intentionally out of scope for this proposal. These boundaries reflect a design choice to focus on durable data representation and long-term reuse rather than higher-level interpretation or analysis.

This proposal does not attempt to define or standardize:

#. A canonical tagging, classification, or ontology system for legislative data
#. Scoring, ranking, or importance metrics for bills, actions, or events
#. An API layer, database schema, or query interface

Motivation
==========

Legislative data is commonly distributed through APIs or large database dumps. While effective for transactional access, these approaches can make it harder to:

* Perform bulk or historical analysis
* Track changes over time
* Diff datasets across updates
* Analyze data without standing up a database server

In practice, many analytical workflows focus primarily on event and action logs rather than full object snapshots. These logs tend to be the most information-dense artifacts for understanding legislative activity, trends, and process dynamics.

A filesystem-based dataset with stable paths, self-contained log records, and explicit schemas supports:

* Efficient extraction of log files for standalone analysis
* Deterministic ingestion into file-native analytics engines
* Clear provenance and auditability
* Compatibility with distributed storage and versioning systems

By representing legislative activity as append-only, self-contained log files addressable via stable filesystem paths, this approach also helps lower the barrier to participation for downstream users. Datasets can be cloned, forked, filtered, and reinterpreted without requiring access to a central database or API service.

This makes it possible for multiple analytical perspectives to coexist without overwriting or replacing a single canonical interpretation of the data, while preserving a shared, auditable record of events.

Specification
=============

Overview
--------

The dataset is represented as a directory tree rooted in an OCD-style jurisdiction namespace.

Legislative entities (such as bills and events) are stored as JSON files, with one file per entity record.

Discrete actions associated with those entities (such as bill actions or vote events) are represented as append-only log records, with one file per log entry.

In practice, many analytical workflows operate primarily on bill action logs and vote event logs. Event files are included for completeness and interoperability, but are not required for most analytical use cases.

Paths and Identifiers
----------------------

Top-level directories use OCD-style identifiers::

  country:{country_code}/
  state:{jurisdiction_code}/
  sessions/
  {session_id}/

Directory names are expected to be stable and deterministic.

Bills
-----

Bill records are stored under::

  country:{country_code}/state:{jurisdiction_code}/sessions/{session_id}/bills/{bill_id}/

A bill directory is expected to contain:

* `metadata.json`: the canonical bill record, conforming to the OCD Bill schema (with optional namespaced extensions)

A bill directory MAY contain:

* `files/`: source documents and derived artifacts (non-normative)
* `logs/`: append-only log entries related to the bill

Log Entries
-----------

Log entries represent discrete chronological records such as bill actions or vote events.

Each log entry must:

* Be stored as a separate JSON file
* Be immutable once written
* Include all context required for independent analysis

The JSON object serves as the authoritative source of identity and context. Filenames are auxiliary and non-authoritative.

Replayability and Derived Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some implementations may treat entity snapshots (for example, bill
`metadata.json` files) as materialized views derived from the underlying log
stream.

In these cases, log entries must contain sufficient information to
deterministically reconstruct derived views using the set of log files and
stable entity identifiers (such as bill identifier and session).

This proposal does not require that all entity snapshots be reconstructable
from logs alone. Instead, it allows designs where logs serve as the primary
source of truth and snapshots are regenerated as needed.

Note: Some entity files may be included for completeness or interoperability
rather than analysis (for example, event records). This proposal does not
prescribe how consumers must use each entity type.

Log Entry Schema (Core Requirements)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every log entry JSON object must include the following top-level fields:

* `id`: stable identifier for the log entry
* `occurred_at`: RFC 3339 UTC timestamp
* `jurisdiction_id`: OCD-style jurisdiction identifier
* `session_id`: legislative session identifier
* `entity_type`: type of entity the log refers to (e.g., `bill`, `event`)
* `entity_id`: stable identifier of the related entity
* `kind`: classification of the log entry (e.g., `action`, `vote_event`)
* `payload`: object containing the domain-specific data for the log entry

Vote Events
-----------

Vote events are represented as log entries derived from upstream vote event objects. Implementations should use `kind: vote_event` for these entries.

The log entry payload should conform to the OCD Vote schema (or a compatible subset). Vote event logs are retained to support downstream analysis such as determining voting outcomes and participation without requiring reconstruction from bill snapshots.


Vote Event Log Payload Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For `kind: vote_event` entries, the `payload` object should contain the upstream vote event object as captured from the source, without adding derived or synthetic fields.

At minimum, the payload must include sufficient information to support roll-call analysis, including:

* `motion_text`
* `result`
* `start_date` (or equivalent source timestamp)
* `votes` (the per-person vote list)
* `counts` (aggregate totals, if provided by the source)
* `sources` (one or more provenance URLs, if provided by the source)

Additional OCD Vote fields may be included when present upstream (for example, organization fields, bill linkage fields, or extras).

This proposal does not define a separate filesystem location or standalone file format for vote events.Instead, vote data is captured as append-only log records and may be used to reconstruct vote event views or standalone vote files as a derived representation.

If an implementation chooses to materialize vote event files, those files are considered derived views and should not be treated as authoritative sources.


Events
------

Event records (for example, hearings) are stored under::

  country:{country_code}/state:{jurisdiction_code}/sessions/{session_id}/events/

Each event is stored as a separate JSON file and is expected to conform to the OCD Event schema. Event files are included primarily for completeness and interoperability and may not be required for most analytical workflows.

Schemas
=======

This proposal defines a set of JSON Schemas used to validate standardized file types.

Implementations are expected to provide schemas for at least:

* Bill `metadata.json`
* Log entry JSON files
* Event JSON files

Examples
========

The following examples illustrate **self-contained log entries** that remain analyzable even when extracted from their original directory context.

Example: Action Log Entry
--------------------------

::

  {
    "id": "ocd-log/usa-119-hr1-20250520T040000Z-calendar",
    "occurred_at": "2025-05-20T04:00:00Z",
    "jurisdiction_id": "ocd-jurisdiction/country:us/state:usa",
    "session_id": "119",
    "entity_type": "bill",
    "entity_id": "HR1",
    "kind": "action",
    "payload": {
      "description": "Placed on the Union Calendar, Calendar No. 78."
    }
  }

Example: Vote Event Log Entry
------------------------------

::

  {
    "id": "ocd-log/usa-119-hr1-20250522T105400Z-vote-145",
    "occurred_at": "2025-05-22T00:00:00Z",
    "jurisdiction_id": "ocd-jurisdiction/country:us/state:usa",
    "session_id": "119",
    "entity_type": "bill",
    "entity_id": "HR1",
    "kind": "vote_event",
    "payload": {
      "motion_text": "On Passage",
      "result": "pass",
      "start_date": "2025-05-22",
      "votes": [
        {
          "voter_name": "Doe, Jane",
          "voter_id": "ocd-person/123",
          "option": "yes"
        },
        {
          "voter_name": "Smith, John",
          "voter_id": "ocd-person/456",
          "option": "no"
        }
      ],
      "counts": [
        { "option": "yes", "value": 218 },
        { "option": "no", "value": 210 },
        { "option": "not voting", "value": 4 }
      ],
      "sources": [
        { "url": "https://example.gov/votes/2025/hr1" }
      ]
    }
  }

These examples use the same log entry envelope with different payload shapes determined by the `kind` field. Full payload schemas are defined separately.

Backward Compatibility
======================

This proposal is additive and does not modify existing OCD object models.

It defines an optional filesystem representation and log format distributing OCD data, without affecting existing data consumers or APIs.
