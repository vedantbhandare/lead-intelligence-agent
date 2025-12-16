Got it 👍
Here’s a **clean, professional, submission-ready `README.md`** you can **copy-paste as is** into your repo.
It’s written exactly at the level reviewers expect (clear, business-aware, not overengineered).

---

```markdown
# Lead Intelligence Web Agent – 3D In-Vitro Models

This repository contains a prototype **lead-intelligence web agent** designed to help
business development teams identify, enrich, and prioritize high-probability prospects
interested in **3D in-vitro models for therapy development**.

The system mimics how a BD professional would combine **scientific intent**, **company
readiness**, and **role relevance** to decide who to contact first.

---

## Problem Statement

Teams working on advanced 3D in-vitro models face a large universe of potential contacts
across industry, academia, publications, and conferences.

The challenge is not finding leads, but **prioritizing who is most likely to want to work
with such technologies**.

This project demonstrates a structured approach to:
- Identifying relevant profiles
- Enriching them with scientific and business context
- Ranking them using a weighted “propensity-to-buy” model

---

## System Overview

### Pipeline

1. **Identification**
   - Profiles sourced from:
     - LinkedIn / professional networks
     - PubMed authors
     - Conference participants (e.g. toxicology, safety assessment)

2. **Enrichment**
   - Company funding stage (simulated business intelligence)
   - Scientific activity (recent liver/toxicology publications)
   - Technographic fit (in-vitro model relevance)
   - Geographic hubs (Boston, Bay Area, Basel, UK, etc.)

3. **Scoring**
   - Rule-based probability score (0–100)
   - Combines scientific intent and commercial readiness

4. **Output**
   - Ranked CSV of leads
   - Interactive Streamlit dashboard for filtering and export

---

## Scoring Logic (0–100)

| Signal | Weight |
|------|--------|
| Role fit (Toxicology / Safety / Preclinical) | +30 |
| Company funding (Series A / B) | +20 |
| Uses in-vitro models | +15 |
| Open to New Approach Methodologies (NAMs) | +10 |
| Location in innovation hub | +10 |
| Recent liver/toxicology publication | +40 |

Scores are capped at **100** and used to rank leads from highest to lowest priority.

---

## Repository Structure

```

lead-intelligence-agent/
│
├── data/
│   ├── leads_raw.csv        # Initial identified profiles
│   ├── leads_enriched.csv   # Enriched dataset
│   └── leads_scored.csv     # Ranked leads with scores
│
├── scoring.py               # Enrichment + scoring pipeline
├── app.py                   # Streamlit dashboard
├── README.md

````

---

## How to Run Locally

### 1. Install dependencies
```bash
pip install pandas streamlit
````

### 2. Run enrichment and scoring

```bash
python scoring.py
```

This generates:

* `data/leads_enriched.csv`
* `data/leads_scored.csv`

### 3. Launch the dashboard

```bash
streamlit run app.py
```

---

## Dashboard Features

* Ranked lead table
* Minimum score filtering
* Location-based filtering
* CSV export of filtered results

---

## Notes & Assumptions

* This is a **prototype/demo**, not a production scraper
* External data sources (funding, publications) are simulated to demonstrate logic
* No platform policies are violated (no live scraping)
* The system is designed to be easily extended with APIs (e.g. PubMed, Crunchbase, LinkedIn providers)

---

## Author
**Vedant Bhandare**

- Help you prepare **answers if Akash replies with questions**
```
