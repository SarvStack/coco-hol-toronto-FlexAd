import streamlit as st

st.title("Workshop agenda")

st.markdown("##### Morning — Introduction & Guided Lab")

MORNING = [
    ("9:00 AM – 10:00 AM", "Introduction to Cortex Code", None, None),
    ("10:00 AM – 10:25 AM", "Session 1: Data Prep", "25 min", "1"),
    ("10:25 AM – 11:00 AM", "Session 2: Cortex Analyst & Semantic Views", "35 min", "2"),
    ("11:00 AM – 11:30 AM", "Session 3: Cortex Search", "30 min", "3"),
    ("11:30 AM – 12:00 PM", "Session 4: Cortex Agents", "30 min", "4"),
    ("12:00 PM – 12:15 PM", "Session 5: CoWork", "15 min", "5"),
    ("12:15 PM – 12:30 PM", "Session 6: Streamlit :gray-badge[Optional]", "15 min", "6"),
]

for time, title, duration, session_num in MORNING:
    col1, col2 = st.columns([1, 4])
    if session_num:
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    else:
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/school: **{title}**")

st.space("small")
st.markdown("##### Lunch")

col1, col2 = st.columns([1, 4])
col1.markdown("**12:30 PM – 1:30 PM**")
col2.markdown(":orange-badge[LUNCH]")

st.space("small")
st.markdown("##### Afternoon — Hands-on Practice on Snowflake Instance")

with st.container(border=True):
    st.markdown("""
**1:30 PM – 4:30 PM** — Apply what you learned in the morning lab to your **Snowflake instance**.

Work at your own pace with Cortex Code on real data and use cases. The Snowflake team is available for guidance and questions throughout the afternoon.
""")

st.space("medium")

st.markdown("##### What you'll build in the morning lab")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | 9 | Campaign performance, bid activity, audience segments, optimization reports |
| **Cortex Search Services** | 1 | ADTECH_SEARCH |
| **Semantic Views** | 1 | ADTECH_OPERATIONS_VIEW with relationships, metrics, and AI instructions |
| **Cortex Agents** | 1 | ADTECH_AGENT with Analyst + Search + custom tools |
| **Streamlit Apps** | 1 | Operations dashboard with AI chat |
""")

st.space("small")

st.markdown("##### Location")
with st.container(border=True):
    st.markdown("""
:material/location_on: **Snowflake Office (16 York Street, Suites 3100–3200), Toronto, ON**

October 21, 2026 — 9:00 AM to 4:30 PM
""")
