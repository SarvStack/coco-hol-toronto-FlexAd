import streamlit as st

st.title("FlexAd AdTech AI Workshop")
st.markdown("Building Intelligence for Programmatic Advertising with Snowflake Cortex")

st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Prompts", "16", help="Total prompts across all tools")
col3.metric("Duration", "2h30", help="Total hands-on lab time")

st.space("medium")

st.markdown("#### How this workshop works")

st.markdown("""
Each section has **numbered prompts** that you copy and paste into the appropriate tool:

- **Cortex Code** — for building infrastructure, creating objects, and writing SQL/Python
- **Cortex Analyst** — for testing natural language queries against your semantic view
- **Snowflake CoWork** — for collaborative data exploration and analysis

All prompts build on each other sequentially — run them in order throughout the day.
""")

st.space("small")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
FlexAd Corp. is a leading programmatic advertising platform managing thousands of ad campaigns across display, video, mobile, and CTV channels. With millions of daily bid requests and complex audience targeting, FlexAd needs to optimize campaign performance, detect ad fraud, allocate budgets efficiently, and ensure compliance with advertising standards. We'll build an AI-powered analytics platform that combines structured campaign data with unstructured optimization reports and compliance documents.

We'll build a complete AI platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | Campaign metrics, bid activity, audience segments, advertiser profiles |
| **Unstructured** | Optimization reports, compliance documentation, campaign playbooks |
| **Time series** | Daily impressions, clicks, spend, bid volumes |
""")

st.space("small")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In 2h30, we build a complete AI-powered operations platform:

**1. Data Foundation** — Load structured and unstructured operations data into Snowflake from pre-generated CSV files.

**2. Natural Language Analytics** — Create a Semantic View over operational tables and query them with plain English via Cortex Analyst.

**3. Intelligent Search** — Build a Cortex Search service over optimization reports and compliance documents for hybrid semantic + keyword search.

**4. AI Agents** — Create a Cortex Agent that orchestrates structured data queries AND document search through a single conversational interface.

**5. Collaborative AI** — Use CoWork to collaboratively analyze data with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and an AI chat interface.
""")

st.space("small")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.space("medium")
st.caption("Built for the October 21, 2026 workshop  :material/location_on:  Snowflake Office, Toronto, ON")
