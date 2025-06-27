import streamlit as st
import pandas as pd

def show_violation_log():
    st.subheader("📋 Violation Log")
    try:
        df = pd.read_csv("violation_log.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Violation log not found.")