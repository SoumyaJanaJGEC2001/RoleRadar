# Greenhouse Job Board API — Field Mapping

## Source inspected

**Company:** C3 AI  
**Source ID:** SRC-010  
**ATS provider:** Greenhouse  
**Board token:** c3iot  
**Inspection date:** 2026-07-05  
**Sample file:** data/samples/greenhouse_c3ai_jobs_sample.json  
**API endpoint used:** Greenhouse Job Board API with `content=true`  
**Total jobs returned:** Dynamic — copy the current value from `meta.total` in the saved JSON response.

---

## Top-Level Response

| Greenhouse field | Observed | Description |
|---|---|---|
| jobs | Yes | Array containing C3 AI's currently published job postings |
| meta | Yes | Metadata about the API response |
| meta.total | Yes | Number of job postings returned during this collection run |

---

## Job Field Mapping

| Greenhouse field | RoleRadar field | Data layer | Required | Notes |
|---|---|---|---|---|
| id | source_job_id | Parsed | Yes | Unique identifier for the published Greenhouse job post |
| internal_job_id | source_internal_job_id | Parsed | No | Internal identifier for the underlying job; may differ from the public post ID |
| requisition_id | requisition_id_raw | Parsed | No | Employer-defined requisition identifier; may be null or absent |
| title | title_raw | Parsed | Yes | Preserve the C3 AI title exactly as published |
| company_name | company_name_raw | Parsed | Yes | Expected value: C3 AI or the company name supplied by the board |
| first_published | source_first_published_at | Parsed | No | Timestamp when the posting was first published |
| updated_at | source_updated_at | Parsed | No | Timestamp of the latest source-side update |
| location.name | location_raw | Parsed | No | Preserve values such as Redwood City, California, United States |
| absolute_url | job_url | Parsed | Yes | Public application or job-description URL |
| language | language_raw | Parsed | No | Expected to identify the language of the posting when supplied |
| content | description_html_raw | Parsed | Yes | Full description; may contain HTML and encoded characters |
| departments | departments_raw | Parsed | No | Array of department objects, such as Data Science or Engineering |
| offices | offices_raw | Parsed | No | Array of office objects; some jobs may be linked to multiple offices |
| metadata | source_metadata | Raw/Parsed | No | C3 AI or Greenhouse-specific custom fields exposed publicly |
| data_compliance | source_data_compliance | Raw/Parsed | No | Compliance-related information where included by Greenhouse |

---

## C3 AI Source Metadata

| Project field | Recorded value |
|---|---|
| Company name | C3 AI |
| Source ID | SRC-010 |
| ATS provider | Greenhouse |
| Board token | c3iot |
| Source tier | A |
| Public access | Yes |
| Login required for reading jobs | No |
| Primary role categories observed | Data Science, Engineering, Forward Deployed Engineering, Product Management, Pre-Sales |
| Locations observed | United States, United Kingdom, Europe, Mexico, India, Asia-Pacific, and Remote |
| India location observed | Bengaluru, India |
| Entry-career information observed | C3 AI has an Interns and Early Professionals section |
| Collection suitability | Suitable for MVP collection |
| Approval status | Approved |

---

## Fields Not Directly Available

| Required project field | Direct API field available | Later extraction needed | Notes |
|---|---|---|---|
| Company name | Usually Yes | No, unless missing | Can be taken from `company_name` or board-level information |
| Minimum experience | No | Yes | Must be extracted from the description |
| Maximum experience | No | Yes | Must be extracted from the description |
| Education requirement | No | Yes | Usually found under qualifications |
| Employment type | Not consistently | Yes | May appear in metadata or description |
| Salary minimum | Sometimes | Yes | Salary may be absent, embedded in content, or exposed through metadata |
| Salary maximum | Sometimes | Yes | Must preserve the original salary wording |
| Currency | Sometimes | Yes | Infer only when explicitly supported by salary text or location |
| Required skills | No structured list | Yes | Extract from responsibilities and qualifications |
| Preferred skills | No structured list | Yes | Must distinguish preferred from mandatory qualifications |
| Remote eligibility | Partially | Yes | Location may say Remote, but eligibility restrictions require description analysis |
| India eligibility | No | Yes | Must not assume India eligibility for every remote role |
| Fresher suitability | No | Yes | Requires experience, responsibility, and seniority analysis |
| Role family | Partially | Yes | Can use title and department but should be normalised |
| Role specialisation | No | Yes | Must be extracted from the title and description |
| Computer Vision relevance | No | Yes | Must be determined from skills, duties, and domain language |
| GenAI relevance | No | Yes | Must be identified from terms such as LLM, generative AI, RAG, or agentic AI |
| Entry-level authenticity | No | Yes | Requires comparison of title, experience, and responsibilities |

---

## Observations

### Fields consistently present

- Public Greenhouse job-post ID
- Job title
- Location object
- Public job URL
- Source update timestamp
- Full job description when `content=true` is used
- Department or office information for many postings

### Fields sometimes missing

- Requisition ID
- Salary details
- Employment type
- Posting deadline
- Explicit experience range
- Remote-eligibility restrictions
- Structured education requirements
- Custom metadata
- Office or department arrays for some records

### Fields embedded inside the description

- Required years of experience
- Minimum education
- Preferred education
- Technical skills
- Programming languages
- Machine-learning tools
- Cloud platforms
- Responsibilities
- Required qualifications
- Preferred qualifications
- Salary information
- Benefits
- Work-authorisation restrictions
- Remote-work restrictions
- Travel requirements

### Source-specific fields

- C3 AI role categories and departments
- Multiple C3 AI office locations
- Greenhouse internal job identifiers
- Greenhouse requisition identifiers
- Custom metadata selected by C3 AI for public exposure
- Job URLs hosted through the C3 AI careers website using a Greenhouse job ID

### Potential parsing difficulties

- The job description is HTML rather than clean plain text.
- HTML entities may need decoding.
- Headings and bullet lists must be preserved during text conversion.
- Some titles combine multiple seniority levels, such as Data Scientist/Senior Data Scientist.
- A single job may contain multiple locations or offices.
- “Remote” does not necessarily mean globally remote.
- Experience requirements may be written as ranges, alternatives, or degree-plus-experience combinations.
- Required and preferred skills may appear in separate sections.
- Salary details may only apply to particular locations.
- The title alone may not accurately indicate fresher suitability.
- Jobs mentioning AI may be business, sales, product, engineering, or research roles rather than data-science roles.

### Data-quality concerns

- Job postings can change after initial publication.
- The same underlying job may have multiple public posts for different locations.
- Similar titles may refer to significantly different responsibilities.
- Senior and junior variants may be combined in one posting.
- Missing salary information must remain missing rather than being guessed.
- Location strings require normalisation but the original text must be preserved.
- C3 AI may host its job description on its own website while Greenhouse supplies the job ID and application infrastructure.
- A posting should not be considered suitable for 0–2 years without checking its qualifications.
- Historical postings may disappear from the public API when closed.

---

## Manually Examined Relevant Posting

**Job ID:** 8612889002  
**Title:** Data Scientist/Senior Data Scientist  
**Company:** C3 AI  
**Location:** Redwood City, California, United States  
**Department:** Data Science  
**Office:** Redwood City  
**Job URL format:** C3 AI job-description page containing Greenhouse parameter `gh_jid=8612889002`  
**Description available:** Yes  
**Role family:** Data Science  
**Likely specialisation:** Enterprise AI / Applied Data Science  
**Likely experience range:** Unclear from the title alone; the combined Data Scientist/Senior Data Scientist title may cover multiple seniority levels  
**Relevant skills noticed:** Must be extracted from the full `content` field rather than inferred from the title  
**Potential fresher suitability:** Borderline or insufficient information until the qualification section is analysed  
**Computer Vision relevance:** Not established from the title  
**GenAI relevance:** Not established from the title  
**Manual-review decision:** Retain in the raw dataset, then classify after description parsing

---

## Example Normalisation Plan

| Original value | Normalised field | Proposed value |
|---|---|---|
| Data Scientist/Senior Data Scientist | role_family | Data Science |
| Data Scientist/Senior Data Scientist | seniority_raw | Mixed seniority |
| Redwood City, California, United States | country | United States |
| Redwood City, California, United States | region | California |
| Redwood City, California, United States | city | Redwood City |
| Data Science | department_normalized | Data Science |
| Unknown until description inspection | fresher_suitability | Insufficient information |
| Unknown until description inspection | experience_min_years | Null |
| Unknown until description inspection | experience_max_years | Null |
| No remote evidence in location | remote_type | Onsite or unclear |
| No India eligibility evidence | india_eligible | Unclear |

---

## Parsing Decisions

1. Preserve the complete Greenhouse response as raw JSON.
2. Preserve `content` as unmodified HTML in the parsed layer.
3. Create a separate plain-text description during processing.
4. Never overwrite the raw HTML description.
5. Preserve title and location exactly as supplied.
6. Store departments and offices as arrays because a job may have multiple values.
7. Treat `id` as the public source job-post ID.
8. Do not use the job title alone to assign an experience range.
9. Do not classify a remote role as globally accessible without supporting evidence.
10. Do not infer salary when no salary is published.
11. Keep the source timestamps separately from the RoleRadar collection timestamp.
12. Store the Greenhouse board token `c3iot` with every collected record.
13. Track the source collector version used to retrieve the response.
14. Reprocess saved raw responses whenever parsing logic improves.

---

## Final Conclusion

The C3 AI Greenhouse source provides enough information for the RoleRadar AI MVP.

It supplies stable job identifiers, original titles, locations, public URLs, timestamps, job descriptions, and organisational metadata. These fields are sufficient for raw collection, parsing, deduplication, role classification, location analysis, and initial job-market analysis.

However, important RoleRadar fields—including experience range, fresher suitability, education, technical skills, remote eligibility, India eligibility, and role specialisation—are not consistently available as structured API fields. They must be extracted later from the job description using deterministic text-processing rules, followed by machine-learning or controlled LLM-assisted extraction where necessary.

**Source decision:** Approved  
**Source tier:** A  
**Recommended collection frequency:** Once daily  
**Recommended first use:** Greenhouse collector MVP and raw-storage validation