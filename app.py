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

if uploaded_files:
    st.markdown("### 2. Build Ads Per Creative")
    for i, file in enumerate(uploaded_files):
        with st.container():
            st.markdown(f"<div class='ad-block'>", unsafe_allow_html=True)

            st.markdown(f"**Creative #{i+1}: {file.name}**")
            preview_col, form_col = st.columns([1, 3])
            with preview_col:
                if file.type.startswith("image"):
                    st.image(file, width=120)
                elif file.type.startswith("video"):
                    st.video(file, format="video/mp4")

            with form_col:
                col1, col2 = st.columns(2)
                with col1:
                    product = st.selectbox(f"Product ({file.name})", ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"], key=f"product_{i}")
                    format_type = st.selectbox(f"Format ({file.name})", ["Image", "Short Video", "Long Video"], key=f"format_{i}")
                    offer = st.text_input(f"Offer Type ({file.name})", key=f"offer_{i}")
                    cta = st.selectbox(f"Call to Action ({file.name})", ["SHOP_NOW", "LEARN_MORE", "SIGN_UP", "SUBSCRIBE", "GET_OFFER"], key=f"cta_{i}")
                with col2:
                    today = datetime.date.today()
                    month_prefix = today.strftime("%b")
                    ad_name = st.text_input(f"Ad Name ({file.name})", value=f"{month_prefix}_{product.replace(' ', '')}_{offer.replace(' ', '')}", key=f"adname_{i}")
                    destination_url = st.text_input(f"Destination URL ({file.name})", value="https://nakie.co", key=f"url_{i}")
                    placement = st.multiselect(f"Placements ({file.name})", [
                        "Facebook Feed", "Instagram Feed", "Facebook Reels", "Instagram Reels",
                        "Facebook Story", "Instagram Story", "Messenger Story", "Audience Network"
                    ], default=["Facebook Feed", "Instagram Feed"], key=f"placements_{i}")

                notes = st.text_area(f"Notes ({file.name})", key=f"notes_{i}")

                ad_builds.append({
                    "file_name": file.name,
                    "product": product,
                    "format": format_type,
                    "offer": offer,
                    "cta": cta,
                    "ad_name": ad_name,
                    "url": destination_url,
                    "placements": placement,
                    "notes": notes
                })

            st.markdown("</div>", unsafe_allow_html=True)

# --- Summary ---
if st.button("✅ Save All Ads"):
    st.success("All ad builds captured (example preview below)")
    st.json(ad_builds)
