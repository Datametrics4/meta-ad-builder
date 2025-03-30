import streamlit as st
import json
import os

st.set_page_config(page_title="Ad Naming", layout="wide")
st.title("📄 Ad Naming")

CONFIG_FILE = "naming_config.json"

# Default values if no config exists yet
default_options = {
    "formats": ["Image", "Short Video", "Long Video"],
    "products": ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"],
    "offers": ["Afterpay Day", "EOFY", "Xmas Sale"],
    "styles": ["UGC", "Testimonial", "Demo", "Lifestyle"],
    "persons": ["Erika", "Liam", "Jess"],
    "editors": ["Editor A", "Editor B"],
    "landings": ["Homepage", "Product Page", "Bundle Page"],
    "cta_options": ["SHOP_NOW", "LEARN_MORE", "SIGN_UP", "SUBSCRIBE", "GET_OFFER"],
    "copy_lengths": ["Short", "Medium", "Long"],
    "primary_copy_options": ["Primary Copy A", "Primary Copy B"],
    "headline_options": ["Headline A", "Headline B"]
}

# Load config from file or fallback to default
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        options = json.load(f)
else:
    options = default_options.copy()

# Streamlit UI
st.markdown("Use the fields below to manage dropdown options used in the Ad Builder.")

updated = False

for key, value in options.items():
    new_input = st.text_area(
        label=key.replace("_", " ").title(),
        value=", ".join(value),
        height=80
    )
    new_values = [v.strip() for v in new_input.split(",") if v.strip()]
    if new_values != options[key]:
        options[key] = new_values
        updated = True

# Save changes back to file
if updated:
    with open(CONFIG_FILE, "w") as f:
        json.dump(options, f, indent=2)
    st.success("✅ Changes saved!")

# Also push values to session_state
for key, value in options.items():
    st.session_state[key] = value
