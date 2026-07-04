# RoleRadar AI — First Greenhouse Collector Design

## 1. Collector Objective

The objective of the first RoleRadar AI collector is to retrieve the complete set of publicly available C3 AI job postings from the Greenhouse Job Board API.

The collector will preserve the received response without filtering or cleaning it, save it inside the approved timestamped raw-data directory, calculate collection metadata, and record every collection attempt in the collection manifest.

This first collector will support only one source:

- Provider: Greenhouse
- Company: C3 AI
- Source ID: SRC-010
- Board identifier: c3iot
- Resource type: jobs

The collector is intended to establish a reliable foundation for later parsing, analysis, machine learning, automation, and agentic AI components.

---

## 2. Collector Input

The collector will use the following configuration:

| Configuration field | Value |
|---|---|
| Source ID | SRC-010 |
| Company name | C3 AI |
| ATS provider | Greenhouse |
| Board identifier | c3iot |
| Source tier | A |
| Resource type | jobs |
| Expected response type | JSON |
| Collector version | 0.1.0 |
| Approval status required | Approved |

The source configuration will be read from:

`configs/source_registry.csv`

The collector must not proceed if the source is missing or is not marked as Approved.

---

## 3. Request Behaviour

The collector will perform the following operations:

1. Locate the C3 AI row in `configs/source_registry.csv`.
2. Confirm that the source ID is `SRC-010`.
3. Confirm that the ATS provider is Greenhouse.
4. Confirm that the board identifier is `c3iot`.
5. Confirm that the approval status is Approved.
6. Build the public Greenhouse jobs request URL.
7. Request the complete set of published jobs, including full job content.
8. Record the UTC time immediately before the request.
9. Use a reasonable request timeout.
10. Send a descriptive project request header.
11. Record the UTC completion time.
12. Avoid repeated or uncontrolled retries.

The initial collector will make one request per manual execution.

A failed request will be recorded as a failed collection attempt rather than retried continuously.

---

## 4. Response Validation

A response will be considered valid only when all of the following checks pass:

1. An HTTP response is received.
2. The HTTP response status indicates success.
3. The response content type is compatible with JSON.
4. The response can be decoded as JSON.
5. The top-level JSON value is an object.
6. The response contains a `jobs` field.
7. The `jobs` field contains a list.
8. The response contains a `meta` field.
9. The total number of jobs can be obtained from `meta.total` or calculated from the length of the jobs list.
10. The response contains a sensible number of job records.

The collector will validate only the overall response structure.

Validation of individual jobs will be implemented later during the parsing and data-validation phases.

### Response status rules

The collector will use the following collection statuses:

- `success`: A valid response was received and its content differs from the previous response.
- `unchanged`: A valid response was received, but its content hash matches the previous successful or unchanged response.
- `invalid_response`: A response was received, but it did not match the expected Greenhouse structure.
- `failed`: The request, file-writing process, or another required operation failed.

---

## 5. Raw File Storage

Valid responses will be saved under the following directory structure:

`data/raw/greenhouse/c3ai/YYYY/MM/DD/`

The year, month, and day folders will be based on the UTC collection timestamp.

The filename convention will be:

`greenhouse_c3ai_jobs_YYYYMMDDTHHMMSSZ.json`

Example:

`greenhouse_c3ai_jobs_20260705T153000Z.json`

The collector must:

- create missing year, month, and day folders automatically;
- preserve the response before filtering or cleaning;
- save one timestamped file per valid collection attempt;
- avoid overwriting existing raw files;
- use UTC timestamps;
- store the relative raw-file path in the manifest.

The raw response must not be manually modified after storage.

---

## 6. Content Hash Behaviour

The collector will calculate a SHA-256 hash from the exact received response content.

The content hash will be used to determine whether the Greenhouse response changed between collection runs.

The process will be:

1. Receive the response content.
2. Calculate its SHA-256 content hash.
3. Find the most recent successful or unchanged C3 AI manifest entry.
4. Compare the current hash with the previous hash.
5. Mark the current run as `success` when the hashes differ.
6. Mark the current run as `unchanged` when the hashes match.
7. Store the current hash in the collection manifest.

The content hash will not be used as an individual job identifier.

Individual jobs will later be identified using their Greenhouse source job IDs.

---

## 7. Manifest Behaviour

Every collection attempt will create exactly one row in:

`data/raw/collection_manifest.csv`

This rule applies to:

- successful requests;
- unchanged responses;
- invalid responses;
- network failures;
- file-writing failures;
- configuration failures;
- deliberately skipped collections.

### Fields recorded after a successful or unchanged request

The manifest row will contain:

- run ID;
- source ID;
- provider;
- company name;
- board identifier;
- resource type;
- request URL;
- request-start time in UTC;
- completion time in UTC;
- HTTP status;
- collection status;
- raw-file path;
- response content type;
- response size in bytes;
- returned job count;
- SHA-256 content hash;
- collector version;
- error type, when applicable;
- error message, when applicable;
- notes.

### Fields recorded after a failed request

A failed request will still record:

- run ID;
- source ID;
- provider;
- company;
- board identifier;
- resource type;
- request URL;
- request-start time;
- completion time;
- collection status;
- collector version;
- error type;
- error message.

The raw-file path, response size, record count, and content hash may remain empty if no valid response was saved.

---

## 8. Collection Run Identifier

Each collection attempt will receive a unique run ID.

The format will be:

`RUN-YYYYMMDD-SEQUENCE`

Examples:

- `RUN-20260705-0001`
- `RUN-20260705-0002`
- `RUN-20260705-0003`

The date portion will use the UTC date.

The sequence number will increase for every attempt made on the same UTC date.

Failed attempts will also consume a sequence number so that each run remains uniquely traceable.

The initial collector will determine the next sequence by checking existing manifest entries for the current UTC date.

---

## 9. Error Handling

The collector will use controlled error categories.

| Error type | Meaning |
|---|---|
| configuration_error | Source configuration is missing, malformed, or incomplete |
| source_not_approved | The source is not marked Approved |
| connection_error | A network connection could not be established |
| timeout_error | The request exceeded the allowed timeout |
| http_error | The server returned a non-success HTTP status |
| json_decode_error | The response could not be decoded as JSON |
| schema_error | The JSON structure did not contain the expected fields |
| file_write_error | The raw response could not be saved |
| manifest_error | The collection manifest could not be updated |
| unexpected_error | An unclassified error occurred |

The collector will store the controlled error category separately from the complete technical error message.

The collector must not fail silently.

---

## 10. Logging

The collector will display a readable terminal summary after every run.

### Successful or unchanged run output

The terminal summary should report:

- run ID;
- source ID;
- company;
- provider;
- HTTP status;
- collection status;
- number of jobs returned;
- response size;
- saved raw-file path;
- shortened content hash;
- whether the source content changed.

### Failed run output

The terminal summary should report:

- run ID;
- source;
- stage at which failure occurred;
- error category;
- error message;
- whether the failure was written to the manifest.

Dedicated log files will be introduced in a later phase.

---

## 11. Collector Non-Goals

Collector version `0.1.0` will not:

- filter jobs by title;
- retain only Data Science roles;
- retain only fresher roles;
- clean job descriptions;
- remove HTML;
- normalise locations;
- extract experience requirements;
- identify technical skills;
- classify role families;
- determine fresher suitability;
- determine India eligibility;
- insert jobs into PostgreSQL;
- train machine-learning models;
- use an LLM;
- use an AI agent;
- send alerts;
- schedule itself;
- collect multiple companies;
- automatically retry requests repeatedly.

These capabilities will be implemented in later project phases.

---

## 12. Acceptance Criteria

The first C3 AI collector will be considered complete when all of the following conditions are satisfied:

1. The collector reads the C3 AI source configuration.
2. It locates the source using source ID `SRC-010`.
3. It refuses collection when the source is not Approved.
4. It builds the correct Greenhouse jobs request.
5. It includes complete job content in the request.
6. It records request-start and completion timestamps in UTC.
7. It validates the overall JSON response structure.
8. It saves valid responses under the correct date directory.
9. It uses the approved timestamped filename convention.
10. It does not overwrite historical raw responses.
11. It calculates the response size in bytes.
12. It determines the returned job count.
13. It calculates a SHA-256 content hash.
14. It compares the hash with the previous C3 AI collection.
15. It marks changed content as `success`.
16. It marks identical content as `unchanged`.
17. It creates exactly one manifest row per collection attempt.
18. It records controlled error categories.
19. It records failed attempts without silently terminating.
20. It does not clean, normalise, or filter the raw response.
21. It does not require an API key or password.
22. It can later be tested against a saved JSON fixture.

---

## 13. First Collector Execution Flow

The planned execution sequence is:

1. Start the collector.
2. Create a unique run ID.
3. Read the source registry.
4. Locate source `SRC-010`.
5. Validate its required configuration.
6. Confirm that its status is Approved.
7. Construct the Greenhouse request URL.
8. Record the UTC request-start time.
9. Send the request.
10. Record the UTC request-completion time.
11. Validate the HTTP response.
12. Validate the JSON structure.
13. Calculate the job count.
14. Calculate the response size.
15. Calculate the SHA-256 hash.
16. Compare the hash with the previous run.
17. Create the raw storage directory.
18. Save the raw response.
19. Append one manifest row.
20. Display the terminal summary.
21. End the run.