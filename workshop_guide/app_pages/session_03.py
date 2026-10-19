import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Search", "11:00 AM – 12:00 PM", "60 min", "Knowledge base, Cortex Search service, and RAG query pattern")

render_technologies_used([
    {"name": "Cortex Search Service", "description": "A managed hybrid search engine combining vector (semantic) and keyword search with automatic reranking. Created with a single SQL statement.", "icon": "search"},
    {"name": "RAG (Retrieval Augmented Generation)", "description": "A pattern that retrieves relevant documents first, then passes them as context to an LLM for grounded answer generation.", "icon": "hub"},
    {"name": "SEARCH_PREVIEW", "description": "SQL function to query a Cortex Search Service. Supports text queries, column selection, filtering, and result limits.", "icon": "preview"},
])


PROMPT_3_1 = """In ADTECH_AI.OPS:

1. First, create a unified text table for search called ADTECH_KNOWLEDGE_BASE that combines:
   - OPTIMIZATION_REPORTS: use report_id as doc_id, 'optimization_report' as doc_type, content as content, report_type as metadata_category, priority as metadata_priority, report_date as doc_date
   - COMPLIANCE_DOCS: use doc_id as doc_id, 'compliance_doc' as doc_type, title || ': ' || content as content, category as metadata_category, 'High' as metadata_priority, effective_date as doc_date

2. Then create a Cortex Search Service:
   CREATE OR REPLACE CORTEX SEARCH SERVICE ADTECH_SEARCH
     ON content
     ATTRIBUTES metadata_category, metadata_priority, doc_type
     WAREHOUSE = ADTECH_WH
     TARGET_LAG = '1 hour'
     EMBEDDING_MODEL = 'snowflake-arctic-embed-l-v2.0'
     AS (
       SELECT doc_id, doc_type, content, metadata_category, metadata_priority, doc_date
       FROM ADTECH_KNOWLEDGE_BASE
     );

Execute all SQL. Then verify with SHOW CORTEX SEARCH SERVICES."""

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

2. Retrieve top 5 documents from ADTECH_SEARCH, then pass to SNOWFLAKE.CORTEX.COMPLETE() with instructions to answer ONLY from the provided documents, cite doc_ids, and structure the answer with: 1) Common performance issues, 2) Root causes, 3) Effective optimization strategies, 4) Recommendations.

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
