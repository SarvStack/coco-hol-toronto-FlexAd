import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, "Cortex Agents", "1:00 PM – 2:15 PM", "75 min", "Cortex Agent with Analyst + Search + custom tools")

render_technologies_used([
    {"name": "Cortex Agent (CREATE AGENT)", "description": "An orchestrating AI that plans tasks, selects tools, executes them, reflects on results, and generates responses.", "icon": "smart_toy"},
    {"name": "Tool Orchestration", "description": "The Agent automatically routes questions to the right tool: Cortex Analyst for structured data, Cortex Search for documents, custom UDFs for logic.", "icon": "route"},
    {"name": "Custom Tools (UDFs)", "description": "User-defined functions that extend Agent capabilities with custom business logic.", "icon": "build"},
])


PROMPT_4_1 = """In ADTECH_AI.OPS, create a Cortex Agent called ADTECH_AGENT.

It should:
- Use auto as the orchestration model
- Have two tools: the ADTECH_OPERATIONS_VIEW semantic view (for structured data queries) and the ADTECH_SEARCH Cortex Search service (for unstructured document search)
- Include instructions defining it as the FlexAd AdTech Operations Assistant, guiding it to use structured data for campaign performance metrics, spend analysis, audience reach, bid activity and search for optimization recommendations, compliance guidelines, best practices
- Mention domain context: programmatic advertising, campaign management, real-time bidding, audience targeting, ad fraud prevention
- Include 3-4 sample questions spanning both tools

Execute and show confirmation."""

render_prompt("Prompt 4.1", "Create the Cortex Agent", PROMPT_4_1)

render_explanation("What this prompt does", """
Creates a **Cortex Agent** combining structured analytics with document search:

- **Structured questions** → routed to Cortex Analyst via the semantic view
- **Unstructured questions** → routed to Cortex Search
- **Mixed questions** → Agent uses both tools and synthesizes
""")


PROMPT_4_2 = """Test our ADTECH_AGENT with these queries:

1. "What is our total spend and ROAS by channel this quarter?" (structured — should use Analyst)
2. "What are the GDPR requirements for audience targeting in the EU?" (unstructured — should use Search)
3. "Our Display campaign CTR dropped 20% — what does our data show and what do our optimization reports recommend?" (mixed — should use both tools)

Show the responses and note which tools the agent selected."""

render_prompt("Prompt 4.2", "Test the Agent", PROMPT_4_2)

render_explanation("What this prompt does", """
Tests the agent with structured, unstructured, and mixed queries to validate tool routing.
""")


PROMPT_4_3 = """In ADTECH_AI.OPS, add a custom tool to the agent:

1. Create a UDF:

CREATE OR REPLACE FUNCTION CALCULATE_CAMPAIGN_HEALTH_SCORE(
    p_ctr FLOAT, p_cvr FLOAT, p_roas FLOAT, p_budget_pace FLOAT
)
RETURNS VARIANT
LANGUAGE SQL
AS
$$
    SELECT OBJECT_CONSTRUCT(
        'health_score', ROUND(
            (LEAST(p_ctr / 0.02, 1.0) * 25) +
            (LEAST(p_cvr / 0.05, 1.0) * 25) +
            (LEAST(p_roas / 3.0, 1.0) * 30) +
            (CASE WHEN p_budget_pace BETWEEN 0.85 AND 1.15 THEN 20
                  WHEN p_budget_pace BETWEEN 0.70 AND 1.30 THEN 10
                  ELSE 0 END)
        , 1),
        'rating', CASE
            WHEN (LEAST(p_ctr/0.02,1)*25 + LEAST(p_cvr/0.05,1)*25 + LEAST(p_roas/3.0,1)*30 + CASE WHEN p_budget_pace BETWEEN 0.85 AND 1.15 THEN 20 WHEN p_budget_pace BETWEEN 0.70 AND 1.30 THEN 10 ELSE 0 END) >= 80 THEN 'Excellent'
            WHEN (LEAST(p_ctr/0.02,1)*25 + LEAST(p_cvr/0.05,1)*25 + LEAST(p_roas/3.0,1)*30 + CASE WHEN p_budget_pace BETWEEN 0.85 AND 1.15 THEN 20 WHEN p_budget_pace BETWEEN 0.70 AND 1.30 THEN 10 ELSE 0 END) >= 60 THEN 'Good'
            WHEN (LEAST(p_ctr/0.02,1)*25 + LEAST(p_cvr/0.05,1)*25 + LEAST(p_roas/3.0,1)*30 + CASE WHEN p_budget_pace BETWEEN 0.85 AND 1.15 THEN 20 WHEN p_budget_pace BETWEEN 0.70 AND 1.30 THEN 10 ELSE 0 END) >= 40 THEN 'Needs Attention'
            ELSE 'Critical'
        END,
        'breakdown', OBJECT_CONSTRUCT(
            'ctr_score', ROUND(LEAST(p_ctr / 0.02, 1.0) * 25, 1),
            'cvr_score', ROUND(LEAST(p_cvr / 0.05, 1.0) * 25, 1),
            'roas_score', ROUND(LEAST(p_roas / 3.0, 1.0) * 30, 1),
            'pacing_score', CASE WHEN p_budget_pace BETWEEN 0.85 AND 1.15 THEN 20 WHEN p_budget_pace BETWEEN 0.70 AND 1.30 THEN 10 ELSE 0 END
        )
    )
$$;

COMMENT ON FUNCTION CALCULATE_CAMPAIGN_HEALTH_SCORE(FLOAT, FLOAT, FLOAT, FLOAT)
IS 'Calculates a campaign health score (0-100) from CTR, CVR, ROAS, and budget pacing. Returns score, rating (Excellent/Good/Needs Attention/Critical), and component breakdown. Benchmarks: CTR target 2%, CVR target 5%, ROAS target 3x, pacing target 85-115%.';

2. Recreate ADTECH_AGENT with CALCULATE_CAMPAIGN_HEALTH_SCORE as an additional tool.

3. Test with: "Calculate the health score for a campaign with 1.5% CTR, 3.2% CVR, 2.8x ROAS, and 95% budget pacing"

Execute all SQL."""

render_prompt("Prompt 4.3", "Agent with Custom Tool", PROMPT_4_3)

render_explanation("What this prompt does", """
Adds a **custom UDF tool** for domain-specific calculations. The Agent can now query data, search documents, AND run custom business logic.
""")


render_key_concepts([
    {"term": "Cortex Agent", "definition": "A Snowflake object that orchestrates LLMs, Analyst, Search, and custom tools to answer complex questions."},
    {"term": "Tool Routing", "definition": "The Agent selects the right tool for each question based on the question type and tool descriptions."},
    {"term": "Custom Tools", "definition": "SQL UDFs registered as Agent tools. Enable domain-specific calculations and business logic."},
])

render_what_you_built([
    "ADTECH_AGENT — Cortex Agent with Analyst + Search tools",
    "Tested structured, unstructured, and mixed queries",
    "CALCULATE_CAMPAIGN_HEALTH_SCORE as a custom tool",
    "Enhanced agent with three tool types",
])
