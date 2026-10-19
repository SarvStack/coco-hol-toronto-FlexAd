import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Search", "11:00 AM – 12:00 PM", "60 min", "Knowledge base, Cortex Search service, and RAG query pattern")

render_technologies_used([
    {"name": "Cortex Search Service", "description": "A managed hybrid search engine combining vector (semantic) and keyword search with automatic reranking. Created with a single SQL statement.", "icon": "search"},
    {"name": "RAG (Retrieval Augmented Generation)", "description": "A pattern that retrieves relevant documents first, then passes them as context to an LLM for grounded answer generation.", "icon": "hub"},
    {"name": "SEARCH_PREVIEW", "description": "SQL function to query a Cortex Search Service. Supports text queries, column selection, filtering, and result limits.", "icon": "preview"},
])


PROMPT_3_1 = """In ADTECH_AI.OPS, using warehouse ADTECH_WH, execute everything:

1. Create a table called ADTECH_KNOWLEDGE_BASE that combines the rows of two tables, with change tracking enabled so a search service can refresh from it.
   - From OPTIMIZATION_REPORTS: REPORT_ID becomes DOC_ID, DOC_TYPE is 'optimization_report', CONTENT stays CONTENT, REPORT_TYPE becomes METADATA_CATEGORY, PRIORITY becomes METADATA_PRIORITY, REPORT_DATE becomes DOC_DATE, and keep CAMPAIGN_ID.
   - From COMPLIANCE_DOCS: DOC_ID stays DOC_ID, DOC_TYPE is 'compliance_doc', CONTENT is the title and content joined as "title: content", CATEGORY becomes METADATA_CATEGORY, METADATA_PRIORITY is 'High', EFFECTIVE_DATE becomes DOC_DATE, and CAMPAIGN_ID is empty.
   Skip rows with no content. Show the row count by document type (expect 60 reports and 30 compliance docs).

2. Create a Cortex Search service called ADTECH_SEARCH on that table:
   - Search on the CONTENT column.
   - Allow filtering by DOC_TYPE, METADATA_CATEGORY, METADATA_PRIORITY, DOC_DATE and CAMPAIGN_ID.
   - Return DOC_ID with each result. Use DOC_ID as the primary key only if it is unique across both sources; otherwise leave the primary key out.
   - Use warehouse ADTECH_WH, refresh at least every hour, and use the snowflake-arctic-embed-l-v2.0 embedding model.

3. Verify:
   - Confirm the service exists and report its status.
   - Run one test search for "how to improve CTR on video campaigns", limited to optimization reports, returning the top 3 results with their doc ID, category and content."""

render_prompt("Prompt 3.1", "Create Cortex Search Service", PROMPT_3_1)

render_explanation("What this prompt does", """
Builds a unified knowledge base from unstructured text sources and creates a hybrid search service.

The search service automatically embeds, indexes, and serves results with auto-refresh when source data changes.
""")


PROMPT_3_2 = """In ADTECH_AI.OPS, query our ADTECH_SEARCH service using SEARCH_PREVIEW:

1. Search for "fraud detection invalid traffic" — should find IVT prevention docs and fraud alerts
2. Search for "GDPR consent programmatic" — should find privacy compliance documents
3. Search for "campaign underperformance CTR drop" — should find creative fatigue and optimization reports
4. Search for "CTV video completion rate" — should find CTV best practices and video optimization docs

Execute all searches and show results."""

render_prompt("Prompt 3.2", "Query the Search Service", PROMPT_3_2)

render_explanation("What this prompt does", """
Tests different search capabilities across the document corpus:

1. **Fraud/IVT** — Tests semantic understanding of ad fraud terminology
2. **Privacy/GDPR** — Tests retrieval of regulatory compliance content
3. **Performance alerts** — Tests matching optimization reports about campaign issues
4. **Channel-specific** — Tests finding CTV/video-specific best practices
""")


PROMPT_3_3 = """In ADTECH_AI.OPS, implement a RAG pattern:

1. Question: "What are the most common causes of campaign underperformance and what optimization strategies have been effective?"

2. Retrieve top 5 documents from ADTECH_SEARCH, then pass to SNOWFLAKE.CORTEX.AI_COMPLETE() with instructions to answer ONLY from the provided documents, cite doc_ids, and structure the answer with: 1) Common performance issues, 2) Root causes, 3) Effective optimization strategies, 4) Recommendations.

Use claude-sonnet-4-6 as the model. Execute and show the RAG response."""

render_prompt("Prompt 3.3", "RAG Pattern: Search + Generate", PROMPT_3_3)

render_explanation("What this prompt does", """
Implements the full **RAG** pattern: retrieve relevant documents, then generate a grounded answer with citations.
""")


render_key_concepts([
    {"term": "Cortex Search Service", "definition": "A managed hybrid search engine created with SQL. Handles embedding, indexing, reranking, and auto-refresh automatically."},
    {"term": "RAG", "definition": "Retrieval Augmented Generation: retrieve documents, include as context in LLM prompt, generate grounded answer."},
    {"term": "Hybrid Search", "definition": "Combining vector search (semantic similarity) with keyword search (exact matching). Better than either alone."},
])

render_what_you_built([
    "ADTECH_KNOWLEDGE_BASE — unified document table (90 documents)",
    "ADTECH_SEARCH — Cortex Search service with hybrid search",
    "Search queries across optimization reports and compliance docs",
    "Full RAG pipeline for grounded Q&A",
])
