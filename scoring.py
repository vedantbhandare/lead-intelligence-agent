import pandas as pd

# -----------------------------
# Load & normalize data
# -----------------------------
df = pd.read_csv("data/leads_raw.csv")
df.columns = df.columns.str.strip().str.lower()

# -----------------------------
# Enrichment
# -----------------------------
funding_map = {
    "helix biotech": "Series B",
    "onconova therapeutics": "Series A",
    "biosphere labs": "Bootstrapped",
    "neocure pharma": "Series B",
    "genrx biosciences": "Grant Funded",
    "vertex therapeutics": "Public",
    "invitrox": "Series A",
    "arcbio": "Seed",
    "uni of texas medical branch": "Grant Funded",
    "biontech": "Public"
}

df["company_clean"] = df["company"].str.lower().str.strip()
df["funding_stage"] = df["company_clean"].map(funding_map).fillna("Unknown")

df["recent_liver_toxicity_publication"] = df["title"].str.contains(
    "liver|toxicology|hepatic",
    case=False,
    na=False
)

df["uses_in_vitro_models"] = df["company"].str.contains(
    "invitro|biosphere|genrx",
    case=False,
    na=False
)

df["open_to_nams"] = df["title"].str.contains(
    "toxicology|safety|preclinical",
    case=False,
    na=False
)

# -----------------------------
# Scoring Engine
# -----------------------------
def calculate_score(row):
    score = 0

    # Role fit
    if any(k in row["title"].lower() for k in ["toxicology", "safety", "preclinical", "3d"]):
        score += 30

    # Company intent
    if row["funding_stage"] in ["Series A", "Series B"]:
        score += 20

    # Technographic fit
    if row["uses_in_vitro_models"]:
        score += 15

    # Open to new methodologies
    if row["open_to_nams"]:
        score += 10

    # Location hub
    hubs = ["boston", "cambridge", "bay area", "basel", "uk", "san francisco"]
    if any(hub in row["company_hq"].lower() for hub in hubs):
        score += 10

    # Scientific intent
    if row["recent_liver_toxicity_publication"]:
        score += 40

    return min(score, 100)

df["probability_score"] = df.apply(calculate_score, axis=1)

# -----------------------------
# Rank & Save
# -----------------------------
df = df.sort_values(by="probability_score", ascending=False)
df["rank"] = range(1, len(df) + 1)

output_cols = [
    "rank",
    "probability_score",
    "name",
    "title",
    "company",
    "person_location",
    "company_hq",
    "funding_stage",
    "profile_source"
]

df[output_cols].to_csv("data/leads_scored.csv", index=False)

print("Scoring complete.")
print("File saved: data/leads_scored.csv")
