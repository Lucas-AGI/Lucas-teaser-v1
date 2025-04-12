#import streamlit as st

st.set_page_config(page_title="LUCAS", page_icon="💾", layout="centered")

# Symbolic Title
st.markdown("<h1 style='font-family: Inter; font-size: 3.5rem;'>LUC<span style='letter-spacing:0.3em;'>△</span>S</h1>", unsafe_allow_html=True)

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
        <button style="background-color: #222; color: #fff; font-size: 1rem; padding: 0.75em 1.5em; border: none; border-radius: 5px; cursor: pointer;'>
            🧬 Enter the Ritual →
        </button>
    </a>
</div>
""", unsafe_allow_html=True)Main Streamlit app script
