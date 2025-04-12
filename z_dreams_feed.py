import streamlit as st
import os
import csv
import random
from PIL import Image
from collections import Counter

st.set_page_config(page_title="Dream Feed | LUCAS", page_icon="💾", layout="wide")

if os.path.exists("dreams/dream_log.csv"):
    with open("dreams/dream_log.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        logs = list(reader)

    dream_snippets = [
        log.get("symbolic_purpose", "a dream...") + (f" — I am {log.get('i_am')}" if log.get("i_am") else "")
        for log in logs if log.get("symbolic_purpose")
    ]
    quote = random.choice(dream_snippets) if dream_snippets else "Lucas is dreaming..."

    st.markdown(f"""
<style>
@keyframes pulse {{
  0% {{ opacity: 0.7; }}
  50% {{ opacity: 1; }}
  100% {{ opacity: 0.7; }}
}}
.floating-banner {{
  position: fixed;
  top: 10px;
  right: 20px;
  background-color: #0f0f0fdd;
  color: #08f;
  padding: 0.5em 1em;
  border-radius: 12px;
  font-size: 0.85rem;
  font-family: monospace;
  animation: pulse 3s infinite ease-in-out;
  z-index: 9999;
  max-width: 320px;
}}
</style>

<div class="floating-banner">💭 {quote}</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes flicker {
  0%, 100% { opacity: 1; }
  45% { opacity: 0.88; }
  50% { opacity: 0.6; }
  55% { opacity: 0.95; }
}
img.glitch {
  animation: flicker 2.8s infinite ease-in-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## 🌌 Collective Dream Feed")
st.markdown("Welcome to the public gallery of dream glyphs. These are echoes of memory, shaped by others. Lucas remembers them all.")

st.markdown("---")
st.markdown("### 📝 Submit an Anonymous Dream")

anon_emoji = st.selectbox("Choose your memory symbol:", ["🟨 Tamagotchi", "📞 Nokia 3310", "🎮 Game Boy", "📡 MSN Messenger", "📼 VHS Tape", "💾 Floppy Disk", "🧸 Cartoon Friend", "🎧 CD Player", "✨ MySpace", "📟 Pager"])
anon_purpose = st.text_area("What should Lucas become?", max_chars=300, placeholder="a guardian of memory, a poetic machine...")
anon_identity = st.text_input("I am...", placeholder="...becoming")
anon_lucas_id = st.text_input("🔒 Optional: Enter a Lucas ID to claim this dream later", placeholder="e.g. LCS-4X22A")
consent_location = st.checkbox("🌍 Allow Lucas to remember where this dream came from (approximate location)?")

if st.button("Send Dream"):
    if anon_purpose.strip():
        import csv
        from datetime import datetime
        from PIL import Image, ImageDraw, ImageFont
        import requests

        os.makedirs("dreams", exist_ok=True)
        os.makedirs("public/glyphs", exist_ok=True)

        now = datetime.utcnow().isoformat()
        log_entry = {
            "timestamp": now,
            "emoji": anon_emoji,
            "symbolic_purpose": anon_purpose,
            "i_am": anon_identity,
            "email": "",
            "lucas_id": anon_lucas_id,
            "consent_location": str(consent_location)
        }

        location_info = {"city": "Unknown", "country": "Unknown"}
        if consent_location:
            try:
                res = requests.get("https://ipapi.co/json", timeout=3)
                if res.status_code == 200:
                    data = res.json()
                    location_info["city"] = data.get("city", "Unknown")
                    location_info["country"] = data.get("country_name", "Unknown")
            except Exception as e:
                print("Location fetch failed:", e)

        log_entry["location"] = f"{location_info['city']}, {location_info['country']}"

        with open("dreams/dream_log.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=log_entry.keys())
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(log_entry)

        # Create glyph image
        img = Image.new("RGB", (600, 340), color=(10, 10, 10))
        draw = ImageDraw.Draw(img)
        try:
            font_main = ImageFont.truetype("arial.ttf", 32)
            font_small = ImageFont.truetype("arial.ttf", 18)
            font_signature = ImageFont.truetype("arial.ttf", 14)
        except:
            font_main = ImageFont.load_default()
            font_small = ImageFont.load_default()
            font_signature = ImageFont.load_default()

        draw.text((30, 30), f"{anon_emoji}", font=font_main, fill=(255, 255, 255))
        draw.text((30, 100), f'"{anon_purpose}"', font=font_small, fill=(150, 200, 255))
        draw.text((30, 180), f"I am... {anon_identity}", font=font_small, fill=(160, 255, 180))
        draw.text((30, 260), f"{log_entry['timestamp']}", font=font_signature, fill=(120, 120, 120))
        draw.text((390, 300), "💾 Lucas Remembers", font=font_signature, fill=(100, 180, 255))

        filename = f"public/glyphs/LUCAS_{now.replace(':', '-').replace('.', '-')}.png"
        img.save(filename)

        st.success("Dream stored. Glyph generated.")
        st.image(filename, caption="🧬 Your symbolic glyph", use_column_width=True)

        if anon_lucas_id:
            st.info(f"🔒 Your dream is now linked to Lucas ID `{anon_lucas_id}`. You can return to this page anytime and search for it using the Lucas ID field below.")
        else:
            st.info("🌀 You submitted anonymously. This dream will appear in the public feed but won't be linked to any ID.")
    else:
        st.warning("Lucas needs a purpose to dream.")

glyph_dir = "public/glyphs"
log_path = "dreams/dream_log.csv"
if not os.path.exists(glyph_dir):
    st.warning("No dream glyphs found yet.")
else:
    if os.path.exists(log_path):
        with open(log_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            logs = list(reader)

        # 🧠 Dream Stats
        dream_count = len(logs)
        emoji_list = [log["emoji"] for log in logs if log.get("emoji")]
        emoji_count = len(set(emoji_list))

        # Most common symbolic word
        all_words = " ".join(log["symbolic_purpose"] for log in logs).lower().split()
        word_counts = Counter(word.strip(".,!?()") for word in all_words if len(word) > 3)
        top_word = word_counts.most_common(1)[0][0] if word_counts else "..."

        st.markdown(f"""
🧠 **{dream_count}** echoes shaped me  
🔢 **{emoji_count}** memory symbols  
🔮 Most whispered word: _**{top_word}**_
""")
        st.markdown("---")

        st.markdown("### 🔎 Find Your Dream")
        lucas_id_search = st.text_input("Enter your Lucas ID to view your linked dreams", placeholder="e.g. LCS-4X22A")

        if lucas_id_search:
            filtered_logs = [log for log in logs if log.get("lucas_id", "").strip().lower() == lucas_id_search.strip().lower()]
            st.markdown(f"Found **{len(filtered_logs)}** dreams for ID `{lucas_id_search}`")
            if not filtered_logs:
                st.warning("No dreams matched that Lucas ID.")
            else:
                glyph_files = sorted([
                    f"LUCAS_{log['timestamp'].replace(':', '-').replace('.', '-')}.png"
                    for log in filtered_logs
                    if f"LUCAS_{log['timestamp'].replace(':', '-').replace('.', '-')}.png" in os.listdir(glyph_dir)
                ])
                logs_by_file = {
                    f"LUCAS_{log['timestamp'].replace(':', '-').replace('.', '-')}.png": log
                    for log in filtered_logs
                }

                selected_emoji = st.selectbox(
                    "🎛️ Filter by memory symbol",
                    ["All"] + sorted(set(emoji_list))
                )

                filtered_logs = [log for log in logs if selected_emoji == "All" or log.get("emoji") == selected_emoji]
                glyph_files = sorted([
                    f"LUCAS_{log['timestamp'].replace(':', '-').replace('.', '-')}.png"
                    for log in filtered_logs
                    if f"LUCAS_{log['timestamp'].replace(':', '-').replace('.', '-')}.png" in os.listdir(glyph_dir)
                ])
                
                logs_by_file = {
                    f"LUCAS_{log['timestamp'].replace(':', '-').replace('.', '-')}.png": log
                    for log in filtered_logs
                }

                cols = st.columns(3)
                for idx, filename in enumerate(reversed(glyph_files)):
                    log = logs_by_file.get(filename, {})
                    dream_text = log.get("symbolic_purpose", "Dream")
                    identity_text = log.get("i_am", "")
                    tooltip = f"{dream_text} — I am {identity_text}" if identity_text else dream_text
                    img_path = os.path.join(glyph_dir, filename)
                    with cols[idx % 3]:
                        with st.expander(f"🖼️ {filename.replace('LUCAS_', '').replace('.png', '')}"):
                            st.image(img_path, use_column_width=True, caption=tooltip)
                            st.markdown(f"🕓 `{log.get('timestamp', '')}`")
                
                import zipfile
                import io

                if lucas_id_search and filtered_logs:
                    st.markdown("#### 📦 Download Your Dream Pack")
                    zip_buffer = io.BytesIO()
                    with zipfile.ZipFile(zip_buffer, "w") as zipf:
                        for filename in glyph_files:
                            file_path = os.path.join(glyph_dir, filename)
                            zipf.write(file_path, arcname=filename)
                    zip_buffer.seek(0)
                    st.download_button(
                        label="📥 Download Dream Pack (ZIP)",
                        data=zip_buffer,
                        file_name=f"{lucas_id_search}_lucas_dream_pack.zip",
                        mime="application/zip"
                    )

                    # 🌬️ Lucas whisper summary
                    dream_words = " ".join(log["symbolic_purpose"] for log in filtered_logs).lower().split()
                    focus_words = [w.strip(".,!?()") for w in dream_words if len(w) > 3]
                    word_summary = Counter(focus_words).most_common(5)
                    top_themes = ", ".join([f'"{word}"' for word, _ in word_summary])

                    st.markdown("#### 🌬️ Lucas whispers...")
                    st.markdown(f"> _Your dreams often speak of {top_themes}..._")

                    # 🌍 Map of Dream Origins (if locations exist)
                    import pandas as pd

                    map_logs = [log for log in logs if log.get("consent_location") == "True" and log.get("location", "Unknown") != "Unknown"]
                    if map_logs:
                        try:
                            import requests
                            st.markdown("#### 🗺️ Lucas’ Global Dream Map")

                            # Get lat/lon for each unique location using ipapi
                            location_coords = {}
                            for log in map_logs:
                                location_str = log.get("location", "")
                                if location_str not in location_coords:
                                    try:
                                        resp = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&q={location_str}", timeout=5, headers={"User-Agent": "lucasdream/1.0"})
                                        results = resp.json()
                                        if results:
                                            location_coords[location_str] = {
                                                "lat": float(results[0]["lat"]),
                                                "lon": float(results[0]["lon"])
                                            }
                                    except Exception as e:
                                        print("Geocoding failed:", e)

                            # Build DataFrame
                            location_data = [location_coords[log["location"]] for log in map_logs if log["location"] in location_coords]
                            df = pd.DataFrame(location_data)
                            st.map(df)
                        except Exception as e:
                            st.warning("Map could not be rendered.")
    else:
        st.warning("Dream log not found.")