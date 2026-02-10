# import streamlit as st
# from agent import handle_query
# from data_loader import load_pilots, load_drones, load_missions

# st.set_page_config(
#     page_title="Drone Operations Coordinator AI",
#     page_icon="🚁",
#     layout="wide"
# )

# # -----------------------------
# # HEADER
# # -----------------------------
# st.markdown("""
#     <h1 style='text-align: center;'>
#     🚁 Drone Operations Coordinator AI
#     </h1>
# """, unsafe_allow_html=True)

# st.markdown(
#     "<p style='text-align:center;'>AI-powered pilot & drone assignment system</p>",
#     unsafe_allow_html=True
# )

# st.divider()

# # -----------------------------
# # LOAD DATA FOR DASHBOARD
# # -----------------------------
# pilots = load_pilots()
# drones = load_drones()
# missions = load_missions()

# available_pilots = sum(p["status"] == "Available" for p in pilots)
# available_drones = sum(d["status"] == "Available" for d in drones)
# urgent_missions = sum(m["priority"] == "Urgent" for m in missions)

# # -----------------------------
# # STATUS CARDS
# # -----------------------------
# col1, col2, col3 = st.columns(3)

# col1.metric("✅ Available Pilots", available_pilots)
# col2.metric("🚁 Available Drones", available_drones)
# col3.metric("⚡ Urgent Missions", urgent_missions)

# st.divider()

# # -----------------------------
# # CHAT + SIDEBAR LAYOUT
# # -----------------------------
# left, right = st.columns([2, 1])

# # -----------------------------
# # CHAT SECTION
# # -----------------------------
# with left:
#     st.subheader("💬 Operations Chat")

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     user_input = st.chat_input("Ask the coordinator...")

#     if user_input:
#         st.session_state.messages.append(
#             {"role": "user", "content": user_input}
#         )

#         response = handle_query(user_input)

#         st.session_state.messages.append(
#             {"role": "assistant", "content": response}
#         )

#         st.rerun()

# # -----------------------------
# # QUICK ACTION PANEL
# # -----------------------------
# with right:
#     st.subheader("⚡ Quick Actions")

#     if st.button("Assign PRJ001"):
#         response = handle_query("Assign PRJ001")
#         st.session_state.messages.append(
#             {"role": "assistant", "content": response}
#         )
#         st.rerun()

#     if st.button("Assign PRJ002"):
#         response = handle_query("Assign PRJ002")
#         st.session_state.messages.append(
#             {"role": "assistant", "content": response}
#         )
#         st.rerun()

#     if st.button("Urgent Reassignment"):
#         response = handle_query("urgent reassignment")
#         st.session_state.messages.append(
#             {"role": "assistant", "content": response}
#         )
#         st.rerun()

#     st.divider()

#     st.subheader("📋 Missions")
#     for m in missions:
#         st.write(f"**{m['project_id']}** — {m['priority']}")



import streamlit as st
from agent import handle_query
from data_loader import load_pilots, load_drones, load_missions

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Drone Operations Coordinator AI",
    page_icon="🚁",
    layout="centered"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🚁 Drone Operations Coordinator AI")
st.caption("AI assistant for pilot assignment, fleet coordination, and conflict detection")

st.divider()

# -----------------------------
# LOAD DATA
# -----------------------------
pilots = load_pilots()
drones = load_drones()
missions = load_missions()

available_pilots = sum(p["status"] == "Available" for p in pilots)
available_drones = sum(d["status"] == "Available" for d in drones)
urgent_missions = sum(m["priority"] == "Urgent" for m in missions)

# -----------------------------
# SYSTEM STATUS
# -----------------------------
c1, c2, c3 = st.columns(3)

c1.metric("Available Pilots", available_pilots)
c2.metric("Available Drones", available_drones)
c3.metric("Urgent Missions", urgent_missions)

st.divider()

# -----------------------------
# CHAT
# -----------------------------
st.subheader("Operations Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something like: Assign PRJ001")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = handle_query(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

st.divider()

# -----------------------------
# QUICK ACTIONS
# -----------------------------
st.subheader("Quick Actions")

qa1, qa2, qa3 = st.columns(3)

if qa1.button("Assign PRJ001"):
    response = handle_query("Assign PRJ001")
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    st.rerun()

if qa2.button("Assign PRJ002"):
    response = handle_query("Assign PRJ002")
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    st.rerun()

if qa3.button("Urgent Reassignment"):
    response = handle_query("urgent reassignment")
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    st.rerun()

st.divider()

# -----------------------------
# MISSIONS LIST
# -----------------------------
st.subheader("Missions")

for m in missions:
    st.write(
        f"**{m['project_id']}** — {m['client']} | "
        f"{m['location']} | Priority: {m['priority']}"
    )
