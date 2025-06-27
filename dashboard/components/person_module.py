import streamlit as st

def draw_person_info(st, person_modules):
    st.subheader("👷 Detected Persons Summary")

    for person_id, item, status, timestamp in person_modules:
        color = "red" if status == "VIOLATION" else "green"
        st.markdown(f"""
            <div style="border:1px solid #ccc; border-radius:10px; padding:10px; margin-bottom:10px;">
                <strong style="color:{color};">{person_id}</strong><br>
                <b>PPE Item:</b> {item}<br>
                <b>Status:</b> <span style="color:{color};">{status}</span><br>
                <b>Scanned At:</b> {timestamp}
            </div>
        """, unsafe_allow_html=True)
