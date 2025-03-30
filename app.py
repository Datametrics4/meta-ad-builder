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

# Placeholder options (to be managed via settings in the future)
formats = ["Image", "Short Video", "Long Video"]
products = ["SnapMount 3", "PowerPack Mini", "TRVLR Tag", "Other"]
offers = ["Afterpay Day", "EOFY", "Xmas Sale"]
styles = ["UGC", "Testimonial", "Demo", "Lifestyle"]
persons = ["Erika", "Liam", "Jess"]
edits = ["Editor A", "Editor B"]
landings = ["Homepage", "Product Page", "Bundle Page"]
ad_ids = ["v1", "v2", "Test"]

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
                st.markdown("**📝 Ad Naming Configuration**")
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    format_type = st.selectbox("Format", formats, key=f"format_{i}")
                    product = st.selectbox("Product", products, key=f"product_{i}")
                with c2:
                    offer = st.selectbox("Offer", offers, key=f"offer_{i}")
                    content_style = st.selectbox("Content Style", styles, key=f"style_{i}")
                with c3:
                    person = st.selectbox("Person", persons, key=f"person_{i}")
                    editor = st.selectbox("Editor", edits, key=f"editor_{i}")
                with c4:
                    landing = st.selectbox("Landing Page", landings, key=f"landing_{i}")
                    ad_id = st.selectbox("Ad Identifier", ad_ids, key=f"adid_{i}")

                today = datetime.date.today()
                month_prefix = today.strftime("%b")
                ad_name = f"{month_prefix}_{format_type}_{product}_{offer}_{content_style}_{person}_{editor}_{landing}_{ad_id}"
                st.text_input("Generated Ad Name", value=ad_name, key=f"adname_{i}")

                destination_url = st.text_input("Destination URL", value="https://nakie.co", key=f"url_{i}")
                placement = st.multiselect("Placements", [
                    "Facebook Feed", "Instagram Feed", "Facebook Reels", "Instagram Reels",
                    "Facebook Story", "Instagram Story", "Messenger Story", "Audience Network"
                ], default=["Facebook Feed", "Instagram Feed"], key=f"placements_{i}")

                notes = st.text_area("Notes", key=f"notes_{i}")

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
                    "url": destination_url,
                    "placements": placement,
                    "notes": notes
                })

            st.markdown("</div>", unsafe_allow_html=True)

# --- Summary ---
if st.button("✅ Save All Ads"):
    st.success("All ad builds captured (example preview below)")
    st.json(ad_builds)
