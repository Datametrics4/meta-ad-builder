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
        st.markdown(f"---\n**{file.name}**")
        if file.type.startswith("image"):
            st.image(file, width=300)
        elif file.type.startswith("video"):
            st.video(file)

# --- Ad Builder Form ---
st.header("2. Build Ad Metadata")
col1, col2 = st.columns(2)

with col1:
    product = st.selectbox("Product", ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"])
    format_type = st.selectbox("Format", ["Image", "Short Video", "Long Video"])
    offer = st.text_input("Offer Type (e.g. Afterpay Day)")
    cta = st.selectbox("Call to Action", ["SHOP_NOW", "LEARN_MORE", "SIGN_UP", "SUBSCRIBE", "GET_OFFER"])
    country = st.multiselect("Country Targeting", ["AU", "NZ", "US", "UK"], default=["AU"])
    language = st.selectbox("Language", ["English", "Spanish", "French"], index=0)

with col2:
    today = datetime.date.today()
    month_prefix = today.strftime("%b")
    ad_name = st.text_input("Ad Name", value=f"{month_prefix}_{product.replace(' ', '')}_{offer.replace(' ', '')}")
    destination_url = st.text_input("Destination URL", value="https://nakie.co")
    placement = st.multiselect("Placements", [
        "Facebook Feed", "Instagram Feed", "Facebook Reels", "Instagram Reels",
        "Facebook Story", "Instagram Story", "Messenger Story", "Audience Network"
    ], default=["Facebook Feed", "Instagram Feed"])
    notes = st.text_area("Internal Notes")

# --- Submit ---
if st.button("✅ Save Ad Build"):
    st.success("Ad metadata saved (this would log to Google Sheets in final version)")
    st.markdown("### 🧾 Ad Summary")
    st.markdown(f"**Ad Name:** {ad_name}")
    st.markdown(f"**Product:** {product}")
    st.markdown(f"**Format:** {format_type}")
    st.markdown(f"**Offer:** {offer}")
    st.markdown(f"**CTA:** {cta}")
    st.markdown(f"**Destination URL:** {destination_url}")
    st.markdown(f"**Countries:** {', '.join(country)}")
    st.markdown(f"**Language:** {language}")
    st.markdown(f"**Placements:** {', '.join(placement)}")
    st.markdown(f"**Notes:** {notes}")

    if uploaded_files:
        st.markdown("### 🎬 Creative Previews")
        for file in uploaded_files:
            st.markdown(f"---\n**{file.name}**")
            if file.type.startswith("image"):
                st.image(file, width=300)
            elif file.type.startswith("video"):
                st.video(file)

    st.markdown("---")
    st.json({
        "ad_name": ad_name,
        "product": product,
        "offer": offer,
        "headline": offer,
        "cta": cta,
        "url": destination_url,
        "country": country,
        "language": language,
        "placements": placement,
        "uploaded_files": [file.name for file in uploaded_files] if uploaded_files else [],
        "notes": notes
    })

