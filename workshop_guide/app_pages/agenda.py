import streamlit as st

st.title("Workshop agenda")

AGENDA = [
    ("8:30 AM", "Arrival & Coffee", None, None),
    ("9:00 AM", "Welcome & Workshop Overview", None, None),
    ("9:15 AM – 10:00 AM", "Session 1: Data Prep", "45 min", "1"),
    ("10:00 AM – 11:00 AM", "Session 2: Cortex Analyst & Semantic Views", "60 min", "2"),
    ("11:00 AM – 12:00 PM", "Session 3: Cortex Search", "60 min", "3"),
    ("12:00 PM – 1:00 PM", ":orange-badge[BREAK]", None, None),
    ("1:00 PM – 2:15 PM", "Session 4: Cortex Agents", "75 min", "4"),
    ("2:15 PM – 3:15 PM", "Session 5: CoWork", "60 min", "5"),
    ("3:15 PM – 4:30 PM", "Session 6: Streamlit", "75 min", "6"),
]

for time, title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f"{title}")
    else:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":gray[{title}]")

st.space("medium")

st.markdown("##### What you'll build by end of session")
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
