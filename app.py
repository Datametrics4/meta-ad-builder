import streamlit as st
import datetime

st.set_page_config(page_title="Meta Ad Builder", layout="wide")
st.markdown("""
    <style>
        .section-title {
            font-size: 1.5rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 600;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.5rem;
        }
        .ad-preview {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 1rem;
            background-color: #fafafa;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📣 Meta Ad Builder")

# --- Layout: Two columns ---
left_col, right_col = st.columns([1, 1.5])

# === LEFT: File Upload ===
with left_col:
    st.markdown("<div class='section-title'>1. Upload Creatives</div>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Upload images/videos (1350 & 1920)",
                                       type=["jpg", "jpeg", "png", "mp4", "mov"],
                                       accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            st.markdown(f"---\n**{file.name}**")
            if file.type.startswith("image"):
                st.image(file, use_column_width=True)
            elif file.type.startswith("video"):
                st.video(file)

# === RIGHT: Ad Builder Form ===
with right_col:
    st.markdown("<div class='section-title'>2. Ad Details</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        product = st.selectbox("Product", ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"])
        format_type = st.selectbox("Format", ["Image", "Short Video", "Long Video"])
        offer = st.text_input("Offer Type")
        cta = st.selectbox("Call to Action", ["SHOP_NOW", "LEARN_MORE", "SIGN_UP", "SUBSCRIBE", "GET_OFFER"])

    with col2:
        today = datetime.date.today()
        month_prefix = today.strftime("%b")
        ad_name = st.text_input("Ad Name", value=f"{month_prefix}_{product.replace(' ', '')}_{offer.replace(' ', '')}")
        destination_url = st.text_input("Destination URL", value="https://nakie.co")
        placement = st.multiselect("Placements", [
            "Facebook Feed", "Instagram Feed", "Facebook Reels", "Instagram Reels",
            "Facebook Story", "Instagram Story", "Messenger Story", "Audience Network"
        ], default=["Facebook Feed", "Instagram Feed"])
        country = st.multiselect("Country", ["AU", "NZ", "US", "UK"], default=["AU"])

    notes = st.text_area("Internal Notes")

# --- Save & Preview ---
st.markdown("<div class='section-title'>3. Preview & Save</div>", unsafe_allow_html=True)

if st.button("✅ Save Ad Build"):
    st.success("Ad metadata saved (placeholder)")

    st.markdown("<div class='ad-preview'>", unsafe_allow_html=True)
    st.markdown(f"**📝 Ad Name:** {ad_name}")
    st.markdown(f"**📦 Product:** {product}")
    st.markdown(f"**🎬 Format:** {format_type}")
    st.markdown(f"**🏷️ Offer:** {offer}")
    st.markdown(f"**🔗 URL:** {destination_url}")
    st.markdown(f"**📍 Placements:** {', '.join(placement)}")
    st.markdown(f"**🌐 Country:** {', '.join(country)}")
    st.markdown(f"**📣 CTA:** {cta}")
    st.markdown(f"**🗒️ Notes:** {notes}")
    st.markdown("</div>", unsafe_allow_html=True)

    if uploaded_files:
        st.markdown("<div class='section-title'>🎬 Creative Preview</div>", unsafe_allow_html=True)
        for file in uploaded_files:
            st.markdown(f"---\n**{file.name}**")
            if file.type.startswith("image"):
                st.image(file, use_column_width=True)
            elif file.type.startswith("video"):
                st.video(file)


