import streamlit as st
import datetime

st.set_page_config(page_title="Meta Ad Builder", layout="wide")
st.title("📣 Meta Ad Builder")

# --- File Upload Section ---
st.header("1. Upload Creatives")
uploaded_files = st.file_uploader("Drop your images/videos here (1350 & 1920)",
                                   type=["jpg", "jpeg", "png", "mp4", "mov"],
                                   accept_multiple_files=True)

if uploaded_files:
    st.subheader("Preview Uploads")
    for file in uploaded_files:
        st.markdown(f"**{file.name}**")
        if file.type.startswith("image"):
            st.image(file, width=300)
        elif file.type.startswith("video"):
            st.video(file)

# --- Ad Builder Form ---
st.header("2. Build Ad Metadata")
col1, col2 = st.columns(2)

with col1:
    product = st.selectbox("Product", ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"])
    offer = st.text_input("Offer Type (e.g. Afterpay Day)")
    headline = st.text_input("Headline Copy")
    cta = st.selectbox("Call to Action", ["SHOP_NOW", "LEARN_MORE", "SIGN_UP", "SUBSCRIBE", "GET_OFFER"])

with col2:
    today = datetime.date.today()
    month_prefix = today.strftime("%b")
    ad_name = st.text_input("Ad Name", value=f"{month_prefix}_{product.replace(' ', '')}_{offer.replace(' ', '')}")
    destination_url = st.text_input("Destination URL", value="https://nakie.co")
    notes = st.text_area("Internal Notes")

# --- Submit ---
if st.button("✅ Save Ad Build"):
    st.success("Ad metadata saved (this would log to Google Sheets in final version)")
    st.json({
        "ad_name": ad_name,
        "product": product,
        "offer": offer,
        "headline": headline,
        "cta": cta,
        "url": destination_url,
        "uploaded_files": [file.name for file in uploaded_files] if uploaded_files else [],
        "notes": notes
    })
