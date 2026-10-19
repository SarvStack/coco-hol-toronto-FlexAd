import streamlit as st
from components import render_session_header, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(5, "CoWork", "2:15 PM – 3:15 PM", "60 min", "Collaborative AI analysis with CoWork")

render_technologies_used([
    {"name": "Snowflake CoWork", "description": "An AI-powered collaborative workspace inside Snowsight where you can analyze data, generate insights, and share findings.", "icon": "group"},
    {"name": "Data Analysis", "description": "CoWork can query your Snowflake data, generate visualizations, and provide insights without writing SQL.", "icon": "analytics"},
    {"name": "Sharing & Collaboration", "description": "CoWork sessions can be shared with team members for collaborative data exploration.", "icon": "share"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open CoWork")
with st.container(border=True):
    st.markdown("""
In Snowsight, click **CoWork** in the left navigation panel. Start a new conversation.

CoWork discovers your tables in `ADTECH_AI.OPS` automatically. Paste each question below one at a time.
""")

st.space("small")

st.markdown("#### :material/chat: Questions to ask CoWork")
st.caption("Copy and paste each question into CoWork individually.")

questions = [
    ("Campaign Performance Overview", "Give me an overview of campaign performance across all channels. Which channels deliver the best ROAS and which have the lowest CPC? Show me a breakdown with key metrics."),
    ("Advertiser Tier Analysis", "Compare the performance of Enterprise vs Mid-Market vs Growth tier advertisers. Which tier delivers the best return on ad spend and why might that be?"),
    ("Bid Strategy Deep Dive", "Analyze our bid activity — what's our average win rate across campaigns? Which campaigns have the best bid efficiency (lowest ratio of win price to bid price)? Are we overbidding anywhere?"),
    ("Channel Mix Optimization", "If we had to reallocate 20% of our Display budget to other channels, which channels should receive it based on their ROAS and conversion rates? Show the data supporting your recommendation."),
    ("Creative Performance Analysis", "Which ad creative formats have the highest approval rate? Cross-reference with campaign performance — do approved creatives in certain formats correlate with better CTR or conversion rates?"),
]

for title, question in questions:
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.code(question, language="text", wrap_lines=True)

st.space("small")

render_explanation("How CoWork works", """
**CoWork** is Snowflake's collaborative AI workspace — different from Cortex Code:

| Tool | Best for |
|------|----------|
| Cortex Code | Building infrastructure, creating objects, writing SQL |
| CoWork | Exploring data, generating insights, team collaboration |
| Cortex Agent | End-user Q&A interface (deployed as a product) |
""")

render_key_concepts([
    {"term": "CoWork", "definition": "Snowflake's collaborative AI workspace. Conversational interface that queries data, creates visualizations, and generates insights."},
    {"term": "Context Maintenance", "definition": "CoWork maintains conversation history so follow-up questions build on previous analysis."},
])

render_what_you_built([
    "Explored AdTech operations data through conversational AI",
    "Generated visualizations and cross-table analysis",
    "Demonstrated the CoWork collaborative analysis pattern",
])
