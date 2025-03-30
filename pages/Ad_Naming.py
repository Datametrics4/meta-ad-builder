import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")
st.title("⚙️ Settings")

# Default values
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
    "headline_options": ["Headline A", "Headline B"],
}

# Store options in session_state
for key, value in default_options.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.markdown("Use the fields below to manage dropdown options used in the Ad Builder.")

for key in default_options:
    new_values = st.text_area(
        label=key.replace("_", " ").title(),
        value=", ".join(st.session_state[key]),
        height=80
    )
    st.session_state[key] = [x.strip() for x in new_values.split(",") if x.strip()]
