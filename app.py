import streamlit as st
import datetime

st.set_page_config(page_title="Meta Ad Builder", layout="wide")
st.title("📣 Meta Ad Builder - Row by Row")

st.markdown("""
    <style>
        .ad-block {
            border: 1px solid #e1e1e1;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1.5rem;
            background-color: #fafafa;
        }
        .generated-name {
            background-color: #e7f3ff;
            border: 1px solid #cce0ff;
            padding: 0.5rem;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }
        .section-padding {
            padding-top: 1.5rem;
            margin-top: 1.5rem;
            border-top: 1px solid #ddd;
        }
        .section-title {
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 0.75rem;
        }
        video {
            max-height: 240px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("### 1. Upload Creatives")
uploaded_files = st.file_uploader("Upload your 1350/1920 images or videos:",
                                   type=["jpg", "jpeg", "png", "mp4", "mov"],
                                   accept_multiple_files=True)

ad_builds = []

# Placeholder options (to be managed via settings in the future)
formats = ["Image", "Short Video", "Long Video"]
products = ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"]
offers = ["Afterpay Day", "EOFY", "Xmas Sale"]
styles = ["UGC", "Testimonial", "Demo", "Lifestyle"]
persons = ["Erika", "Liam", "Jess"]
edits = ["Editor A", "Editor B"]
landings = ["Homepage", "Product Page", "Bundle Page"]
cta_options = ["SHOP_NOW", "LEARN_MORE", "SIGN_UP", "SUBSCRIBE", "GET_OFFER"]
copy_lengths = ["Short", "Medium", "Long"]
primary_copy_options = ["Primary Copy A", "Primary Copy B"]
headline_options = ["Headline A", "Headline B"]

if uploaded_files:
    st.markdown("### 2. Build Ads Per Creative")
    for i, file in enumerate(uploaded_files):
        with st.container():
            st.markdown(f"<div class='ad-block'>", unsafe_allow_html=True)

            st.markdown(f"**Creative #{i+1}:**")
            preview_col, form_col = st.columns([1, 3])
            with preview_col:
                if file.type.startswith("image"):
                    st.image(file, width=120)
                elif file.type.startswith("video"):
                    st.video(file, format="video/mp4")

            with form_col:
                st.markdown("<div class='section-title section-padding'>Ad Naming</div>", unsafe_allow_html=True)
                format_type = st.selectbox("Format", formats, key=f"format_{i}")
                product = st.selectbox("Product", products, key=f"product_{i}")
                offer = st.selectbox("Offer", offers, key=f"offer_{i}")
                content_style = st.selectbox("Content Style", styles, key=f"style_{i}")
                person = st.selectbox("Person", persons, key=f"person_{i}")
                editor = st.selectbox("Editor", edits, key=f"editor_{i}")
                landing = st.selectbox("Landing Page", landings, key=f"landing_{i}")
                ad_id = st.text_input("Ad Identifier", key=f"adid_{i}")

                today = datetime.date.today()
                month_prefix = today.strftime("%b")
                ad_name = f"{month_prefix}_{format_type}_{product}_{offer}_{content_style}_{person}_{editor}_{landing}_{ad_id}"
                st.markdown("**Generated Ad Name**")
                st.markdown(f"<div class='generated-name'>{ad_name}</div>", unsafe_allow_html=True)

                st.markdown("<div class='section-title section-padding'>Ad Copy</div>", unsafe_allow_html=True)
                copy_length = st.selectbox("Copy Length", copy_lengths, key=f"copylen_{i}")
                primary_copy = st.selectbox("Primary Copy", primary_copy_options, key=f"primarycopy_{i}")
                headline = st.selectbox("Headline", headline_options, key=f"headline_{i}")

                st.markdown("<div class='section-title section-padding'>Ad Parameters</div>", unsafe_allow_html=True)
                cta = st.selectbox("Call to Action", cta_options, key=f"cta_{i}")
                destination_url = st.text_input("Destination URL", value="https://nakie.co", key=f"url_{i}")
                placement = st.multiselect("Placements", [
                    "Facebook Feed", "Instagram Feed", "Facebook Reels", "Instagram Reels",
                    "Facebook Story", "Instagram Story", "Messenger Story", "Audience Network"
                ], default=["Facebook Feed", "Instagram Feed"], key=f"placements_{i}")

                ad_builds.append({
                    "file_name": file.name,
                    "format": format_type,
                    "product": product,
                    "offer": offer,
                    "style": content_style,
                    "person": person,
                    "editor": editor,
                    "landing": landing,
                    "ad_id": ad_id,
                    "ad_name": ad_name,
                    "cta": cta,
                    "copy_length": copy_length,
                    "primary_copy": primary_copy,
                    "headline": headline,
                    "url": destination_url,
                    "placements": placement
                })

            st.markdown("</div>", unsafe_allow_html=True)

# --- Summary ---
if st.button("✅ Save All Ads"):
    st.success("All ad builds captured (example preview below)")
    st.json(ad_builds)
