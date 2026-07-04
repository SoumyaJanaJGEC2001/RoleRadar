# RoleRadar AI — Raw Data Storage Design

## Purpose

The raw-data storage layer preserves every response collected from an approved job source before filtering, parsing, cleaning, or normalisation.

Every successful response will be stored as an immutable historical record. A collection manifest will record every request attempt and link it to its saved raw file.

## Storage Directory Structure

Raw responses will be organised using the following hierarchy:

provider / company / year / month / day

Example:

data/raw/greenhouse/c3ai/2026/07/05/

This organisation prevents files from different providers, companies, or collection dates from being mixed together.

## Filename Convention

Raw files will use the following pattern:

provider_company_resource_timestampUTC.json

Example:

greenhouse_c3ai_jobs_20260705T153000Z.json

The filename contains:

- source provider;
- company identifier;
- resource type;
- UTC collection timestamp;
- original response format.

Historical files will not be overwritten.

## UTC Timestamp Policy

All collection timestamps will be stored in UTC.

UTC timestamps will use ISO 8601 format.

Example:

2026-07-05T15:30:00Z

The letter Z indicates UTC.

Local time may be displayed in the dashboard later, but storage and pipeline timestamps will remain in UTC.

## Collection Run Identifier

Every collection attempt will receive a unique run identifier.

Format:

RUN-YYYYMMDD-SEQUENCE

Examples:

RUN-20260705-0001
RUN-20260705-0002

Failed and skipped attempts will also receive run identifiers.

## Collection Manifest Fields

The collection manifest will contain:

- run identifier;
- source identifier;
- provider;
- company name;
- board identifier;
- requested resource;
- request URL;
- request start time;
- completion time;
- HTTP status;
- collection status;
- raw file path;
- content type;
- response size;
- number of records;
- content hash;
- collector version;
- error type;
- error message;
- notes.

## Collection Status Values

The permitted collection statuses are:

- success — valid response received and saved;
- partial — response received but expected information was incomplete;
- failed — request or file-saving operation failed;
- skipped — collection was deliberately not attempted;
- unchanged — response matched the previous collected response;
- invalid_response — a response arrived but did not match the expected structure.

## Content Hash Policy

Every successfully saved response will receive a content hash.

The hash acts as a fingerprint of the response. It allows the pipeline to identify whether two collection runs returned identical content.

A content hash will not be used as the job identifier. Individual jobs will continue to use their source job IDs.

## Raw Data Immutability

Raw response files must never be manually edited.

The raw layer must not:

- rename source fields;
- remove irrelevant jobs;
- filter roles;
- clean descriptions;
- normalise locations;
- infer experience;
- add calculated fields.

All parsing and cleaning will occur in later data layers.

## Failed Collection Handling

Every failed request will still be recorded in the collection manifest.

When a request fails:

- collection status will be marked as failed;
- the error type will be recorded;
- the error message will be recorded;
- the raw file path may remain empty;
- the request must not be retried continuously.

## Raw Data Retention Policy

All raw responses will be retained during the MVP.

New collection runs will create new timestamped files rather than overwriting older responses.

Storage optimisation, compression, and cloud lifecycle rules may be introduced later if the volume becomes large.

## Example C3 AI Collection

Provider: Greenhouse  
Company: C3 AI  
Source ID: SRC-010  
Board identifier: c3iot  
Resource type: jobs  

Example directory:

data/raw/greenhouse/c3ai/2026/07/05/

Example filename:

greenhouse_c3ai_jobs_20260705T153000Z.json

The corresponding collection-manifest row will store the request URL, collection timestamps, HTTP status, raw file path, record count, response size, and content hash.