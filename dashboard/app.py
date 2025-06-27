import streamlit as st
from components.live_feed import run_live_feed
from components.violation_log_view import show_violation_log

st.set_page_config(page_title="PPE Detection Dashboard", layout="wide")

st.title("🦺 Real-Time PPE Detection Dashboard")

menu = st.sidebar.radio("Navigation", ["Live Detection", "Violation Logs"])

if menu == "Live Detection":
    run_live_feed()
elif menu == "Violation Logs":
    show_violation_log()