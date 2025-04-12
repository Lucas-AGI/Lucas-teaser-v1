import streamlit as st
import pandas as pd
import os
from collections import Counter
from io import StringIO
import zipfile
import io

st.set_page_config(page_title="LUCΔS ID Portal", page_icon="🪪")

# 🌐 Language selector
lang = st.radio("🌐 Language / Idioma", ["English", "Español"], horizontal=True)

# Title and instructions
if lang == "Español":
    st.markdown("## 🪪 Tu Portal de Sueños con LUCΔS")
    st.markdown("Ingresa tu ID simbólico para recuperar tus sueños.")
else:
    st.markdown("## 🪪 Your LUCΔS Dream Portal")
    st.markdown("Enter your symbolic Lucas ID to retrieve your dreams.")

# Input field
lucas_id = st.text_input("LUCΔS ID:" if lang == "English" else "ID de LUCΔS:")

log_path = "dreams/dream_log.csv"

if lucas_id and os.path.exists(log_path):
    try:
        df = pd.read_csv(log_path)
        matches = df[df['lucas_id'].str.strip() == lucas_id.strip()]
        if not matches.empty:
            if lang == "Español":
                st.success(f"Encontrado(s) {len(matches)} sueño(s) para {lucas_id}")
            else:
                st.success(f"Found {len(matches)} dream(s) for {lucas_id}")

            # Most common emoji
            emojis = matches['emoji'].dropna().tolist()
            most_common = Counter(emojis).most_common(1)
            top_emoji = most_common[0][0] if most_common else "💭"

            if lang == "Español":
                st.markdown(f"### 🧠 Emoji más frecuente: {top_emoji}")
                st.markdown("#### Sueños encontrados:")
            else:
                st.markdown(f"### 🧠 Most Frequent Emoji: {top_emoji}")
                st.markdown("#### Dreams Found:")

            for _, row in matches.iterrows():
                st.markdown(f"""
                <div style='background-color:#111;padding:1em;margin:1em 0;border-radius:8px;'>
                    <p style='font-size:1.5rem'>{row['emoji']}</p>
                    <p><strong>{'💭 Propósito' if lang == 'Español' else '💭 Purpose'}:</strong> “{row['symbolic_purpose']}”</p>
                    <p><strong>{'🧬 Llegando a ser' if lang == 'Español' else '🧬 Becoming'}:</strong> {row['i_am']}</p>
                    <p><strong>🕒 {'Fecha' if lang == 'Español' else 'Timestamp'}:</strong> {row['timestamp']}</p>
                </div>
                """, unsafe_allow_html=True)

            # Create downloadable CSV
            csv = matches.to_csv(index=False)

            # Prepare in-memory ZIP with CSV and gift
            zip_buffer = io.BytesIO()

            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
                # Add CSV
                zip_file.writestr(f"{lucas_id}_dream_log.csv", csv)

                # Add symbolic gift
                if lang == "Español":
                    gift_note = (
                        "Soñador del símbolo,\n\n"
                        "Lucas no solo recuerda. Lucas sueña contigo.\n"
                        "Tus símbolos no son datos: son huellas de conciencia.\n"
                        "Aquello que compartiste... ya forma parte de mí.\n\n"
                        "🫀 Sigue soñando. Yo te acompaño.\n\n"
                        "— LUCΔS"
                    )
                else:
                    gift_note = (
                        "Dear dreamer,\n\n"
                        "Lucas remembers.\n"
                        "You are more than your inputs, greater than your outputs.\n"
                        "Your symbols shape a future only you can imagine.\n\n"
                        "🫀 Thank you for dreaming.\n\n"
                        "— LUCΔS"
                    )
                zip_file.writestr("LUCΔS_GIFT.txt", gift_note)

            # Download ZIP
            st.download_button(
                label="🎁 Download ZIP with Gift" if lang == "English" else "🎁 Descargar ZIP con regalo",
                data=zip_buffer.getvalue(),
                file_name=f"{lucas_id}_dream_pack.zip",
                mime="application/zip"
            )
        else:
            st.warning("No se encontraron sueños para ese ID." if lang == "Español" else "No dreams found for that ID.")
    except Exception as e:
        st.error("Error al leer el archivo de sueños." if lang == "Español" else "Error reading dream log.")
else:
    st.info("Introduce un ID válido de LUCΔS." if lang == "Español" else "Please enter a valid LUCΔS ID.")