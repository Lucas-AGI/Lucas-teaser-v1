import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Lucas Dream Lookup", page_icon="🔍")

st.markdown("## 🔍 Lookup Your Lucas Dream History")
lucas_id = st.text_input("Enter your LUCΔS ID (e.g. LUCΔS-Ω3481-ΣYB)")

log_path = "dreams/dream_log.csv"

if lucas_id and os.path.exists(log_path):
    try:
        df = pd.read_csv(log_path)
        matches = df[df['lucas_id'] == lucas_id]
        if not matches.empty:
            st.success(f"Found {len(matches)} dream(s) for {lucas_id}")
            for _, row in matches.iterrows():
                st.markdown(f"""
                <div style='background-color:#111;padding:1em;margin:1em 0;border-radius:8px;'>
                    <p style='font-size:1.5rem'>{row['emoji']}</p>
                    <p><strong>💭 Purpose:</strong> “{row['symbolic_purpose']}”</p>
                    <p><strong>🧬 Becoming:</strong> {row['i_am']}</p>
                    <p><strong>🕒 Timestamp:</strong> {row['timestamp']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No dreams found for that Lucas ID.")
    except Exception as e:
        st.error("Could not search dream log.")
else:
    st.info("Please enter a valid Lucas ID.")
