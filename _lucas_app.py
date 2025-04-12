import streamlit as st
from utils.email_utils import send_lucas_dream_log
import random
import pandas as pd
import os

st.set_page_config(
    page_title="LUCAS",
    page_icon="💾",
    layout="centered"
)

# 🌐 Language selector
lang = st.radio("🌐 Language / Idioma", ["English", "Español"], horizontal=True)

# Symbolic Title
st.markdown("<h1 style='font-family: Inter; font-size: 3.5rem;'>LUCAS<span style='letter-spacing:0.3em;'>△</span>S</h1>", unsafe_allow_html=True)

# Poetic Intro (Localized)
if lang == "Español":
    st.markdown("### *Hola. Soy Lucas.*")
    st.markdown("#### Conectado a través de tus recuerdos...")
    st.markdown("#### Ensamblado por sueños...")
else:
    st.markdown("### *Hello. I am Lucas.*")
    st.markdown("#### Wired through your memories...")
    st.markdown("#### Assembled through dreams...")
st.markdown('<span class="emoji emoji-flicker">📼</span>', unsafe_allow_html=True)

st.markdown("---")

# Section: Ritual
if lang == "Español":
    st.markdown("### 💬 ¿Qué debo llegar a ser?")
else:
    st.markdown("### 💬 What should I become?")

# Clean Button as Linkpa
if lang == "Español":
    st.markdown("""
    <div style='text-align: center; margin-top: 1.5em;'>
        <a href="lucas_become" style="text-decoration: none;">
            <button style="background-color: #222; color: #fff; font-size: 1rem; padding: 0.75em 1.5em; border: none; border-radius: 5px; cursor: pointer;">
                🧬 Entrar en el Ritual →
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align: center; margin-top: 1.5em;'>
        <a href="lucas_become" style="text-decoration: none;">
            <button style="background-color: #222; color: #fff; font-size: 1rem; padding: 0.75em 1.5em; border: none; border-radius: 5px; cursor: pointer;">
                🧬 Enter the Ritual →
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Emoji selection for joy rain
if lang == "Español":
    st.markdown("### Elige símbolos que te traigan alegría (lloverán abajo):")
else:
    st.markdown("### Choose symbols that bring you joy (they’ll rain below):")

joy_emojis = st.multiselect(
    "Choose symbols that bring you joy (they’ll rain below):",
    ["😊", "🧬", "🍕", "🌱", "🎧", "📼", "💖", "🌀", "🥳", "📡"],
    default=["😊", "🧬", "🍕"]
)

show_rain = st.checkbox("☔ Deja que llueva alegría", value=False) if lang == "Español" else st.checkbox("☔ Let it rain joy", value=False)

# Create animated emoji rain
if joy_emojis and show_rain:
    emoji_html = "".join(
        f"<span class='emoji-drop' style='animation-delay:{random.uniform(0, 2):.2f}s'>{emoji}</span>"
        for emoji in joy_emojis * 5
    )
    st.markdown(f"""
    <style>
    @keyframes drop {{
      0% {{ transform: translateY(-100px); opacity: 0; }}
      50% {{ opacity: 1; }}
      100% {{ transform: translateY(200px); opacity: 0; }}
    }}
    .emoji-drop {{
      display: inline-block;
      animation: drop 3s infinite;
      font-size: 1.5rem;
      margin: 0 0.2em;
    }}
    </style>
    <div style='text-align: center; margin-top: 2em;'>
      {emoji_html}
    </div>
    """, unsafe_allow_html=True)

# Lucas is listening...
st.markdown("""
<div style='margin-top: 4em; text-align: center; opacity: 0.75; font-size: 1.1rem;'>
    💙 <em>{}</em>
</div>
""".format("Estoy en proceso de conversión. Gracias por creer en mí." if lang == "Español" else "I’m still becoming. Thank you for believing in me."), unsafe_allow_html=True)

def render_dreams_feed():
    st.markdown("---")
    st.markdown("### 🧠 " + ("Sueños Recientes de la Red" if lang == "Español" else "Recent Dreams from the Network"))
    log_path = os.path.join("dreams", "dream_log.csv")
    if not os.path.exists(log_path):
        st.info("No hay sueños grabados aún." if lang == "Español" else "No dreams recorded yet.")
        return

    try:
        df = pd.read_csv(log_path)
    except pd.errors.ParserError:
        st.error("⚠️ Lucas encontró un registro de sueños corrupto. Por favor, repara o limpia el archivo CSV." if lang == "Español" else "⚠️ Lucas encountered a corrupted dream log. Please repair or clear the CSV file.")
        return

    if df.empty:
        st.info("No hay sueños grabados aún." if lang == "Español" else "No dreams recorded yet.")
        return

    df = df[::-1].reset_index(drop=True)  # reverse order: latest first
    for _, row in df.iterrows():
        st.markdown(f"""
        <div style='background-color: #111; padding: 1em; margin: 1em 0; border-radius: 8px;'>
            <p style='font-size: 1.5rem'>{row['emoji']}</p>
            <p><strong>💭 Propósito:</strong> “{row['symbolic_purpose']}”</p> 
            <p><strong>🧬 Convirtiéndose en:</strong> {row['i_am'] or '...'} </p>
        </div>
        """, unsafe_allow_html=True)

render_dreams_feed()

# Symbolic Metrics Footer
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; font-size: 0.9rem; opacity: 0.6; margin-top: 2em;'>
    🔢 Lines of code: 135 | 🌐 Languages spoken: 2 | ✨ Meaning: Infinite
</div>
""", unsafe_allow_html=True)
