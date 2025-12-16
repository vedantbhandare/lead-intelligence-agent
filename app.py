import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Intelligence Dashboard", layout="wide")

st.title("🔬 Lead Intelligence Dashboard")
st.subheader("3D In-Vitro Models – High-Probability Leads")

# Load scored data
df = pd.read_csv("data/leads_scored.csv")

# Sidebar filters
st.sidebar.header("Filters")

min_score = st.sidebar.slider(
    "Minimum Probability Score",
    min_value=0,
    max_value=100,
    value=50
)

location_filter = st.sidebar.text_input("Filter by Company HQ (e.g. Boston, Basel)")

# Apply filters
filtered_df = df[df["probability_score"] >= min_score]

if location_filter:
    filtered_df = filtered_df[
        filtered_df["company_hq"].str.contains(location_filter, case=False, na=False)
    ]

# Display metrics
st.metric("Total Leads", len(filtered_df))
st.metric("Top Score", filtered_df["probability_score"].max())

# Display table
st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download option
st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_leads.csv",
    mime="text/csv"
)
