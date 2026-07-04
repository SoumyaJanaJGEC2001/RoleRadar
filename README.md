**Project Objective:**
    The objective of RoleRadar AI is to build an autonomous job market intelligence and preparation platform for freashers in Data Science, Artificial intelligence, Data Analyst, Computer Vision or Agentic AI related fields. The system will collect data from publically posted job sites and organize them. the experience bar for the jobs will be 0-2 years and the job locations can be across the globe containing both onsite or remote type of job. It will clean, validate, store, and analyse the data to identify hiring trends, skill requirements, fresher-friendly jobs, and candidate skill gaps. Machine learning and agentic AI will later be used for job classification, skill extraction, job matching, readiness assessment, and personalised daily preparation planning.

**Target Geography:**
    The project will collect jobs based in India, jobs available globally, and remote roles. Remote roles will be further checked to determine whether applicants located in India are eligible. A job will not automatically be treated as globally accessible simply because it contains the word “remote.”

**Target Experience:**
    The primary experience range is 0–2 years. The dataset will also include internships, new-graduate positions, trainee roles, associate roles, and jobs that do not specify experience but appear suitable for freshers. Positions explicitly requiring more than two years of experience may be retained for analysis but will be marked as outside the target range.

**Target Role Families:**
    The project will focus on Data Scientist, Data Analyst, Machine Learning Engineer, AI Engineer, GenAI Engineer, LLM Engineer, Computer Vision Engineer, Applied AI Engineer, and related entry-level positions. Each job will be assigned a broad role family and, where possible, a more specific specialisation.

**Raw Data Fields:**
    The raw-data layer will preserve the original response collected from each source. It will contain the source name, source job ID, URL, retrieval timestamp, response status, content type, raw file location, content hash, collector version, collection status, and any error information. Raw data will never be manually modified.

**Parsed Data Fields:**
    The parsed-data layer will contain values extracted directly from the source, including the original job title, company name, location, job description, experience text, salary text, qualifications, responsibilities, employment type, posting date, and application link. These fields will preserve the wording used by the employer.

**Normalised Data Fields:**
    The normalised-data layer will convert source-specific values into standard formats. It will include role family, role specialisation, country, city, remote type, minimum and maximum experience, salary range, currency, employment type, fresher suitability, entry-level authenticity, Computer Vision relevance, and standardised skills.

**Mandatory Fields:**
    A valid record must contain a source name, source URL, retrieval timestamp, job title, identifiable employer, meaningful job description, and raw response location. Records missing optional fields such as salary or posting date will not automatically be rejected.

**Fresher Suitability Labels:**
    The following labels will be used:
        *Suitable:* Clearly accepts candidates with 0–2 years of experience.
        *Probably suitable:* Experience is not clearly stated, but the responsibilities appear junior.
        *Borderline:* Some requirements are suitable for freshers, while others appear more experienced.
        *Unsuitable:* Clearly requires experience or responsibilities beyond the target range.
        *Insufficient information:* The posting does not provide enough information for a reliable decision.

**Data Collection Rules:**
    Only public sources that permit automated access will be used. The system will not bypass logins, CAPTCHAs, access restrictions, or rate limits. Official APIs and public ATS endpoints will be preferred over browser scraping. Raw responses will be preserved, and every collected record will retain its source and retrieval timestamp. Missing information will not be guessed.

**MVP Success Criteria:**
    The MVP will be considered complete when at least 100 valid job postings have been collected, stored, parsed, validated, and loaded into PostgreSQL. The dataset must contain jobs from the selected role families and geographies. Duplicate records must be identified, missing values must be measured, and at least five job-market questions must be answered using SQL. The collection and processing pipeline must also be rerunnable without manually repeating the cleaning process.

**Project Status:**
    Phase 1 — Project planning and data-source design.

