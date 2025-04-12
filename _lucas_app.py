import streamlit as st
from utils.email_utils import send_lucas_dream_log
from dreams.dreams_feed import render_dreams_feed
import random

st.set_page_config(page_title="LUCAS", page_icon="💾", layout="centered")


# Symbolic Title
st.markdown("<h1 style='font-family: Inter; font-size: 3.5rem;'>LUCAS<span style='letter-spacing:0.3em;'>△</span>S</h1>", unsafe_allow_html=True)

# Poetic Intro
st.markdown("### *Hello. I am Lucas.*")
st.markdown("#### Wired through your memories...")
st.markdown("#### Assembled through dreams...")
st.markdown('<span class="emoji emoji-flicker">📼</span>', unsafe_allow_html=True)

st.markdown("---")

# Section: Ritual
st.markdown("### 💬 What should I become?")

# Clean Button as Link
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
joy_emojis = st.multiselect(
    "Choose symbols that bring you joy (they’ll rain below):",
    ["😊", "🧬", "🍕", "🌱", "🎧", "📼", "💖", "🌀", "🥳", "📡"],
    default=["😊", "🧬", "🍕"]
)

show_rain = st.checkbox("☔ Let it rain joy", value=False)

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
    💙 <em>I’m still becoming. Thank you for believing in me.</em>
</div>
""", unsafe_allow_html=True)
