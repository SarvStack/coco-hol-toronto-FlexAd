import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(2, "Cortex Analyst & Semantic Views", "10:00 AM – 11:00 AM", "60 min", "Semantic view with relationships, metrics, and natural language queries")

render_technologies_used([
    {"name": "Cortex Analyst", "description": "Snowflake's text-to-SQL engine that converts natural language questions into SQL queries using a semantic view to understand your data's business meaning.", "icon": "chat"},
    {"name": "Semantic View", "description": "A first-class Snowflake object (CREATE SEMANTIC VIEW) that describes your data in business terms: tables, relationships, facts, dimensions, metrics, and synonyms.", "icon": "description"},
    {"name": "AI_SQL_GENERATION", "description": "Custom instructions embedded in the semantic view that guide how Cortex Analyst generates SQL — providing domain context and disambiguation hints.", "icon": "auto_fix_high"},
])


PROMPT_2_1 = """/semantic_studio In ADTECH_AI.OPS, create a semantic view called ADTECH_OPERATIONS_VIEW for use with Cortex Analyst. It should cover these tables: ADVERTISERS, CAMPAIGNS, AD_CREATIVES, CHANNELS, AUDIENCE_SEGMENTS, DAILY_PERFORMANCE, BID_ACTIVITY.

Include:
- Relationships between the tables following these rules:
  - Do NOT specify join_type — omit it entirely (the proto enum doesn't accept string values like many_to_one)
  - Convention: left_table = fact/many side, right_table = dimension/one side (put the table with many rows as left_table)
  - Define primary_key.columns on dimension tables (ADVERTISERS, CHANNELS, AUDIENCE_SEGMENTS) so the engine knows the "one" side
  - Use this template for each relationship:
    relationships:
      - name: <descriptive_name>
        left_table: <FACT_TABLE>
        right_table: <DIMENSION_TABLE>
        relationship_columns:
          - left_column: <FK_COLUMN>
            right_column: <PK_COLUMN>
  - Relationships needed: CAMPAIGNS → ADVERTISERS (advertiser_id), DAILY_PERFORMANCE → CAMPAIGNS (campaign_id), DAILY_PERFORMANCE → CHANNELS (channel_id), BID_ACTIVITY → CAMPAIGNS (campaign_id), AD_CREATIVES → CAMPAIGNS (campaign_id)
- Facts for key numeric columns: impressions, clicks, conversions, spend, revenue, bid_requests, bids_won, avg_bid_price, avg_win_price, daily_budget, estimated_reach
- Dimensions for categorical columns: advertiser name, industry, tier, country, campaign name, channel, objective, status, creative format, segment name, segment type
- Add useful SYNONYMS (e.g. spend → "ad spend", "cost", "budget used"; CTR → "click-through rate"; CVR → "conversion rate"; CPM → "cost per mille", "cost per thousand"; CPC → "cost per click"; ROAS → "return on ad spend")
- Metrics: CTR (clicks/impressions), CVR (conversions/clicks), CPM (spend/impressions*1000), CPC (spend/clicks), ROAS (revenue/spend), Win Rate (bids_won/bid_requests)
- An AI_SQL_GENERATION instruction with domain context: This is an AdTech/programmatic advertising platform. Key domain concepts: CTR = click-through rate (clicks/impressions), CVR = conversion rate (conversions/clicks), CPM = cost per mille (spend/impressions*1000), CPC = cost per click (spend/clicks), ROAS = return on ad spend (revenue/spend), Win Rate = bids won / bid requests. Campaign objectives include awareness, consideration, conversion, and retargeting. Channels include display, video, mobile, CTV, native, social, audio, and DOOH.

Execute the SQL and confirm with DESCRIBE SEMANTIC VIEW."""

render_prompt("Prompt 2.1", "Create the Semantic View", PROMPT_2_1)

render_explanation("What this prompt does", """
Creates a **semantic view** — a first-class Snowflake object that enables natural language to SQL.

The semantic view maps AdTech business terms to SQL:
- **Relationships** connect fact tables (DAILY_PERFORMANCE, BID_ACTIVITY) to dimension tables (ADVERTISERS, CHANNELS, CAMPAIGNS)
- **Facts** are numeric columns used in aggregations (impressions, spend, revenue)
- **Dimensions** are categorical columns used for grouping and filtering (channel, industry, objective)
- **Metrics** are pre-defined calculations (CTR, CPM, ROAS) so analysts can ask for them by name
- **AI instructions** teach the model domain-specific terminology and conventions
""")


PROMPT_2_2 = """Ask Cortex Analyst these questions using ADTECH_AI.OPS.ADTECH_OPERATIONS_VIEW:

1. What is the total ad spend and ROAS by channel?
2. Which advertisers have the highest click-through rate across all their campaigns?
3. Show me daily impressions and spend trends for the last 30 days
4. What are the top 5 campaigns by conversion rate, and what channels are they running on?

Show the generated SQL and results for each."""

render_prompt("Prompt 2.2", "Test with Natural Language Queries", PROMPT_2_2)

st.info("""
:material/lightbulb: **You can also test these in the Cortex Analyst UI!**

In Snowsight, navigate to **AI & ML → Cortex Analyst** in the left sidebar. Select your `ADTECH_OPERATIONS_VIEW` semantic view, and you'll see a playground where you can type natural language questions interactively.
""")

render_explanation("What this prompt does", """
Tests Cortex Analyst across different question types to validate the semantic view definitions.

1. **Aggregation with metric** — Tests ROAS metric definition and channel grouping
2. **Cross-table join** — Tests advertiser-campaign-performance relationship chain
3. **Time series** — Tests date filtering and trend analysis
4. **Ranking with join** — Tests conversion rate metric + multi-table context
""")


PROMPT_2_3 = """Now expand our ADTECH_OPERATIONS_VIEW in ADTECH_AI.OPS:

1. Add a new metric called eCPM (effective CPM) = (revenue / impressions) * 1000 — this measures how much revenue each 1000 impressions generates
2. Add a new metric called Bid Efficiency = (avg_win_price / avg_bid_price) — this measures how efficiently we're winning auctions (lower is better)
3. Add synonyms: eCPM → "effective CPM", "revenue per mille"; Bid Efficiency → "auction efficiency", "win efficiency"

Execute all SQL."""

render_prompt("Prompt 2.3", "Expand the Semantic View", PROMPT_2_3)

render_explanation("What this prompt does", """
Demonstrates iterative semantic view development — adding calculated metrics.

- **eCPM** is a key AdTech metric showing revenue earned per 1000 impressions — the flip side of CPM (cost per mille)
- **Bid Efficiency** measures how close our winning bids are to the auction clearing price — closer to 1.0 means less overpaying
""")


render_key_concepts([
    {"term": "Cortex Analyst", "definition": "Snowflake's text-to-SQL engine. Converts natural language to SQL using a semantic view for context."},
    {"term": "Semantic View", "definition": "A first-class Snowflake object mapping tables to business concepts. Contains relationships, facts, dimensions, metrics, synonyms, and AI instructions."},
    {"term": "AI_SQL_GENERATION", "definition": "Custom instructions guiding SQL generation. Essential for domain-specific terminology."},
])

render_what_you_built([
    "ADTECH_OPERATIONS_VIEW semantic view with domain-specific metrics",
    "Natural language queries validated against the view",
    "Expanded view with eCPM and Bid Efficiency metrics",
])
