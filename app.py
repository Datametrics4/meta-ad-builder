import streamlit as st
import datetime

st.set_page_config(page_title="Meta Ad Builder", layout="wide")
st.title("Meta Ad Builder")

st.markdown("""
    <style>
        .generated-name {
            background-color: #e7f3ff;
            border: 1px solid #cce0ff;
            padding: 0.5rem;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
        }
        .section-padding {
            padding-top: 2rem;
            margin-top: 2rem;
            border-top: 1px solid #ddd;
        }
        .section-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .ad-header {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .error-text {
            color: red;
            font-size: 0.85rem;
            padding-top: 0.3rem;
        }
        .success-text {
            color: green;
            font-size: 0.9rem;
            padding-top: 0.3rem;
        }
        video, img {
            width: 100%;
            height: auto;
        }
        header .st-emotion-cache-18ni7ap.ezrtsby0 { display: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown("### 1. Upload Creatives")
uploaded_files = st.file_uploader("Upload your 1350/1920 images or videos:",
                                   type=["jpg", "jpeg", "png", "mp4", "mov"],
                                   accept_multiple_files=True)

# Placeholder options
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
    st.markdown("### 2. Ad Building")

    for i, file in enumerate(uploaded_files):
        saved_key = f"saved_{i}"
        error_key = f"error_{i}"
        ad_name_key = f"ad_name_{i}"
        visible_key = f"show_expander_{i}"

        if saved_key not in st.session_state:
            st.session_state[saved_key] = False
        if error_key not in st.session_state:
            st.session_state[error_key] = ""
        if ad_name_key not in st.session_state:
            st.session_state[ad_name_key] = ""
        if visible_key not in st.session_state:
            st.session_state[visible_key] = True

        today = datetime.date.today()
        month_prefix = today.strftime("%b")

        if st.session_state[saved_key] and st.session_state[ad_name_key]:
            creative_title = f"Creative #{i+1}: {st.session_state[ad_name_key]}"
        else:
            creative_title = f"Creative #{i+1}: [Not Saved]"

        st.markdown(f"<div class='ad-header'>{creative_title}</div>", unsafe_allow_html=True)

        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            if st.button(f"✅ Save Ad", key=f"save_{i}"):
                ad_id = st.session_state.get(f"adid_{i}", "").strip()
                if not ad_id:
                    st.session_state[error_key] = "Ad Identifier is required."
                else:
                    format_type = st.session_state.get(f"format_{i}", "")
                    product = st.session_state.get(f"product_{i}", "")
                    offer = st.session_state.get(f"offer_{i}", "")
                    content_style = st.session_state.get(f"style_{i}", "")
                    person = st.session_state.get(f"person_{i}", "")
                    editor = st.session_state.get(f"editor_{i}", "")
                    landing = st.session_state.get(f"landing_{i}", "")

                    ad_name = f"{month_prefix}_{format_type}_{product}_{offer}_{content_style}_{person}_{editor}_{landing}_{ad_id}"
                    st.session_state[ad_name_key] = ad_name
                    st.session_state[saved_key] = True
                    st.session_state[error_key] = ""

        with col_btn2:
            if st.button(f"🔽 Close Ad", key=f"close_{i}"):
                st.session_state[visible_key] = False

        if st.session_state[error_key]:
            st.markdown(f"<div class='error-text'>{st.session_state[error_key]}</div>", unsafe_allow_html=True)

        if st.session_state[saved_key] and not st.session_state[error_key]:
            st.markdown("<div class='success-text'>Ad saved successfully!</div>", unsafe_allow_html=True)

        if st.session_state[visible_key]:
            preview_col, form_col = st.columns([1.2, 2.8])
            with preview_col:
                if file.type.startswith("image"):
                    st.image(file, use_column_width=True)
                    st.markdown("**Image Hash:**")
                elif file.type.startswith("video"):
                    st.video(file, format="video/mp4")
                    st.markdown("**Meta Video ID:**")

            with form_col:
                st.markdown("<div class='section-title'>Ad Naming</div>", unsafe_allow_html=True)
                st.selectbox("Format", formats, key=f"format_{i}")
                st.selectbox("Product", products, key=f"product_{i}")
                st.selectbox("Offer", offers, key=f"offer_{i}")
                st.selectbox("Content Style", styles, key=f"style_{i}")
                st.selectbox("Person", persons, key=f"person_{i}")
                st.selectbox("Editor", edits, key=f"editor_{i}")
                st.selectbox("Landing Page", landings, key=f"landing_{i}")
                st.text_input("Ad Identifier", key=f"adid_{i}")

                ad_id_val = st.session_state.get(f"adid_{i}", "")
                ad_name_preview = f"{month_prefix}_{st.session_state.get(f'format_{i}', '')}_{st.session_state.get(f'product_{i}', '')}_{st.session_state.get(f'offer_{i}', '')}_{st.session_state.get(f'style_{i}', '')}_{st.session_state.get(f'person_{i}', '')}_{st.session_state.get(f'editor_{i}', '')}_{st.session_state.get(f'landing_{i}', '')}_{ad_id_val}"

                st.markdown("**Generated Ad Name**")
                st.markdown(f"<div class='generated-name'>{ad_name_preview}</div>", unsafe_allow_html=True)

                st.markdown("<div class='section-title section-padding'>Ad Copy</div>", unsafe_allow_html=True)
                st.selectbox("Copy Length", copy_lengths, key=f"copylen_{i}")
                st.selectbox("Primary Copy", primary_copy_options, key=f"primarycopy_{i}")
                st.selectbox("Headline", headline_options, key=f"headline_{i}")

                st.markdown("<div class='section-title section-padding'>Ad Parameters</div>", unsafe_allow_html=True)
                st.selectbox("Call to Action", cta_options, key=f"cta_{i}")
                st.text_input("Destination URL", value="https://nakie.co", key=f"url_{i}")
                st.multiselect("Placements", [
                    "Facebook Feed", "Instagram Feed", "Facebook Reels", "Instagram Reels",
                    "Facebook Story", "Instagram Story", "Messenger Story", "Audience Network"
                ], default=["Facebook Feed", "Instagram Feed"], key=f"placements_{i}")

        st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)
