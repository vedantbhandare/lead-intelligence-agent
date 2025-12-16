
# Lead Intelligence Agent (Demo)

A prototype **lead intelligence and scoring system** that identifies, enriches, and ranks high-probability business development leads for **3D in-vitro models in drug safety and toxicology**.

This project was built as a **working demo** to showcase how a web agent can combine professional profiles, scientific signals, and business context into a ranked lead list.

---

## What This Demo Does

1. **Ingests identified profiles** (simulated LinkedIn / PubMed / Conference data)
2. **Enriches leads** with company, location, and research intent signals
3. **Applies a probability score (0–100)** to rank leads by likelihood to engage
4. **Displays results** in an interactive Streamlit dashboard
5. **Exports ranked leads** to CSV for BD teams

---

## Scoring Logic (0–100)

| Signal                                       | Weight |
| -------------------------------------------- | ------ |
| Role fit (Toxicology / Safety / Preclinical) | +30    |
| Company funding (Series A / B)               | +20    |
| Uses in-vitro models                         | +15    |
| Open to New Approach Methodologies (NAMs)    | +10    |
| Location in innovation hub                   | +10    |
| Recent liver / toxicology publication        | +40    |

**Scores are capped at 100** and used to rank leads from highest to lowest priority.

---

## Example Outcome

* Junior scientist at a non-funded startup → **15 / 100**
* Director of Safety Assessment at a Series B biotech in Cambridge with recent liver toxicity research → **90+ / 100**

---

## Repository Structure

```
lead-intelligence-agent/
│
├── data/
│   ├── leads_raw.csv        # Initial identified profiles
│   ├── leads_enriched.csv   # Enriched dataset
│   └── leads_scored.csv     # Final ranked leads with scores
│
├── scoring.py               # Enrichment + scoring pipeline
├── app.py                   # Streamlit dashboard
├── README.md
```

---

## How to Run Locally

### 1. Install dependencies

```bash
pip install pandas streamlit
```

### 2️. Run the scoring pipeline

```bash
python scoring.py
```

This generates:

* `data/leads_enriched.csv`
* `data/leads_scored.csv`

### 3️. Launch the dashboard

```bash
streamlit run app.py
```

---

## Data Sources (Simulated for Demo)

This prototype simulates signals from:

* **LinkedIn / Sales Navigator** (roles, companies, locations)
* **PubMed / Google Scholar** (recent toxicology publications)
* **Conference attendee lists** (SOT, AACR, ISSX)
* **Funding intelligence** (Series A/B, public biotech indicators)

>  No scraping or private APIs are used in this demo.

---

## Future Extensions

* Live API integrations (Proxycurl, Semantic Scholar, Crunchbase)
* Automated PubMed keyword extraction
* Real-time lead refresh
* CRM integration
* Outreach personalization

---

## Submission Context

This repository was created as a **working demo** to illustrate how an intelligent web agent can identify and rank high-quality leads for **3D in-vitro models in therapeutic research**.

### Author
### Vedant Bhandare
