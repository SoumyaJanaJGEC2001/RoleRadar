# RoleRadar AI Data Source Policy

This document defines the data sources from which RoleRadar AI may collect job-posting information. It is designed to ensure that collection is reproducible, responsible, limited to legitimate public information, and respectful of source access conditions. The project will prioritise official employer career pages and public applicant-tracking-system job-board endpoints.

## Purpose

RoleRadar AI exists to build an autonomous job-market intelligence and preparation platform for freshers in Data Science, Artificial Intelligence, Data Analysis, Computer Vision, and Agentic AI-related fields. The system will collect data from publicly posted job sites, organise it, clean and validate it, and analyse it to identify hiring trends, skill requirements, fresher-friendly opportunities, and candidate skill gaps. Machine learning and agentic AI will later be used for job classification, skill extraction, job matching, readiness assessment, and personalised daily preparation planning.

## Scope and Alignment with the README

This policy applies to all data collection, storage, parsing, validation, and analysis activities performed by the project. It is aligned with the project’s stated objectives, target geography, target experience, target role families, and MVP success criteria.

## Target Geography

The project will collect jobs based in India, jobs available globally, and remote roles. Remote roles will be further checked to determine whether applicants located in India are eligible. A job will not automatically be treated as globally accessible simply because it contains the word “remote”.

## Target Experience

The primary experience range is 0–2 years. The dataset will also include internships, new-graduate positions, trainee roles, associate roles, and jobs that do not specify experience but appear suitable for freshers. Positions explicitly requiring more than two years of experience may be retained for analysis but will be marked as outside the target range.

## Target Role Families

The project will focus on Data Scientist, Data Analyst, Machine Learning Engineer, AI Engineer, GenAI Engineer, LLM Engineer, Computer Vision Engineer, Applied AI Engineer, and related entry-level positions. Each job will be assigned a broad role family and, where possible, a more specific specialisation.

## Approved Source Types

Approved sources include:

- Official employer career pages
- Public applicant-tracking-system job-board endpoints
- Public APIs that provide job-posting data in a documented and non-restricted manner
- Publicly accessible company or recruitment pages that permit lawful automated retrieval

## Prohibited Source Types

The following sources are not permitted:

- Private, login-protected, or authenticated-only sources
- Sources that require bypassing CAPTCHAs, anti-bot protections, or access controls
- Sources that explicitly disallow automated collection or scraping
- Websites or APIs that require deceptive access methods or credential abuse
- Any source that would violate applicable terms of service, privacy rules, or platform restrictions

## Source Approval Checklist

A source may be approved only if all of the following are true:

- It is publicly accessible without bypassing access controls
- It is relevant to the project’s target geography, experience range, and role families
- It is consistent with the project’s collection principles and ethical standards
- It does not require personal data collection or intrusive access
- It can be accessed in a sustainable and reproducible way
- Its rate limits and access behaviour are understood and documented

## Data Collection Principles

The following principles apply to all approved collection activities:

- Only public sources that permit automated access will be used.
- The system will not bypass logins, CAPTCHAs, access restrictions, or rate limits.
- Official APIs and public ATS endpoints will be preferred over browser scraping.
- Raw responses will be preserved, and every collected record will retain its source and retrieval timestamp.
- Missing information will not be guessed.
- Data collection will remain limited, responsible, and proportionate to the project’s needs.

## Data Layer Policy

### Raw Data Fields

The raw-data layer will preserve the original response collected from each source. It will contain the source name, source job ID, URL, retrieval timestamp, response status, content type, raw file location, content hash, collector version, collection status, and any error information. Raw data will never be manually modified.

### Parsed Data Fields

The parsed-data layer will contain values extracted directly from the source, including the original job title, company name, location, job description, experience text, salary text, qualifications, responsibilities, employment type, posting date, and application link. These fields will preserve the wording used by the employer.

### Normalised Data Fields

The normalised-data layer will convert source-specific values into standard formats. It will include role family, role specialisation, country, city, remote type, minimum and maximum experience, salary range, currency, employment type, fresher suitability, entry-level authenticity, Computer Vision relevance, and standardised skills.

### Mandatory Fields

A valid record must contain a source name, source URL, retrieval timestamp, job title, identifiable employer, meaningful job description, and raw response location. Records missing optional fields such as salary or posting date will not automatically be rejected.

### Fresher Suitability Labels

The following labels will be used:

- Suitable: Clearly accepts candidates with 0–2 years of experience.
- Probably suitable: Experience is not clearly stated, but the responsibilities appear junior.
- Borderline: Some requirements are suitable for freshers, while others appear more experienced.
- Unsuitable: Clearly requires experience or responsibilities beyond the target range.
- Insufficient information: The posting does not provide enough information for a reliable decision.

## Rate and Frequency Policy

During local development, each approved company job board will be checked manually or at most once per day. The project will not use rapid parallel requests. Failed requests will not be retried continuously. Collection frequency will later be adjusted according to the source’s behaviour, documented limits, and the rate at which job postings normally change.

## Raw Data Retention

Raw responses will be retained in their original form so that collection activity is reproducible and auditable. Retention will be limited to what is necessary for validation, debugging, and analysis. Any retention practice must remain consistent with the project’s data governance and privacy expectations.

## Personal Data Exclusion

The collection process will exclude personal data where possible. The project will not intentionally collect names, email addresses, phone numbers, resumes, or other personal information unless it is strictly necessary and explicitly permitted by policy. Job-posting data will be prioritised over any personal or sensitive material.

## Source Review Process

Each approved data source will be reviewed periodically to confirm that it remains appropriate for use. The review will consider access conditions, legal or policy compliance, reliability, data quality, and changes in collection behaviour. Sources that no longer meet the criteria may be suspended or removed.

## Initial Approved Providers

The initial approved provider set will consist of sources that meet the policy criteria and support the project’s objectives for fresher-focused job-market intelligence. Additional providers may be approved over time following the source review process.

## MVP Success Criteria

The MVP will be considered complete when at least 100 valid job postings have been collected, stored, parsed, validated, and loaded into PostgreSQL. The dataset must contain jobs from the selected role families and geographies. Duplicate records must be identified, missing values must be measured, and at least five job-market questions must be answered using SQL. The collection and processing pipeline must also be rerunnable without manually repeating the cleaning process.

## Project Status

Phase 1 — Project planning and data-source design.