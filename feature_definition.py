import streamlit as st
from PIL import Image, UnidentifiedImageError
from db import SessionLocal, Feature, init_db
from feature_constants import FEATURE_CONSTANTS, get_next_feature_id

def show_feature_definition():
    st.title("🔧 Feature Definition")
    init_db()
    db = SessionLocal()
    feature_data = {}

    section1, section2, section3 = st.tabs(["1️⃣ Definition", "2️⃣ Requirements", "3️⃣ Alignment"])

    with section1:
        with st.form("def_form"):
            theme = st.selectbox("Select Theme", list(FEATURE_CONSTANTS.keys()))

            if "last_theme" not in st.session_state:
                st.session_state.last_theme = theme
                st.session_state.selected_feature = None

            if theme != st.session_state.last_theme:
                st.session_state.selected_feature = None
                st.session_state.last_theme = theme

            feature_names = [f["name"] for f in FEATURE_CONSTANTS[theme]]

            if st.session_state.selected_feature is None:
                st.session_state.selected_feature = st.selectbox(
                    "Select Feature",
                    feature_names
                )
            else:
                st.write(f"✅ Selected feature: **{st.session_state.selected_feature}**")
                if st.button("🔄 Change Feature Selection"):
                    st.session_state.selected_feature = None

            if st.checkbox("Add custom feature"):
                custom_name = st.text_input("Custom Feature Name")
                if custom_name:
                    new_id = get_next_feature_id(theme)
                    feature_data["feature_id"] = new_id
                    feature_data["name"] = custom_name
                    st.info(f"Assigned ID {new_id} to new feature '{custom_name}'")
            else:
                selected = next((f for f in FEATURE_CONSTANTS[theme] if f["name"] == st.session_state.selected_feature), None)
                feature_data["feature_id"] = selected["id"] if selected else None
                feature_data["name"] = st.session_state.selected_feature

            feature_data["goal"] = st.text_area("Goal / Motivation")
            feature_data["customer_internal"] = st.text_area("Customer(s) / Internal")
            feature_data["feature_spec_link"] = st.text_input("Feature Spec Link")
            feature_data["activity_type"] = st.selectbox("Activity Type", ["Initiation", "Ongoing", "Change Request"])
            feature_data["stage"] = st.selectbox("Stage", ["Planning", "Development", "Both"])
            feature_data["usefulness"] = st.slider("🎯 Usefulness (Product Value)", 1, 100, 50)
            feature_data["quality"] = st.text_area("📈 Quality (System OKRs or notes)")
            feature_data["timeline_required"] = st.text_input("📅 Timeline - Required")
            feature_data["timeline_planned"] = st.text_input("📅 Timeline - Planned")
            feature_data["timeline_committed"] = st.text_input("📅 Timeline - Committed")

            submitted = st.form_submit_button("💾 Save")
            if submitted:
                existing = db.query(Feature).filter(Feature.feature_id == feature_data["feature_id"]).first()
                if existing:
                    for k, v in feature_data.items():
                        setattr(existing, k, v)
                    st.success("✅ Feature updated!")
                else:
                    f = Feature(**feature_data)
                    db.add(f)
                    st.success("✅ Feature added!")
                db.commit()

    with section2:
        st.header("🔷 Requirements (Edit Mode)")
        st.markdown("_Requirements section placeholder_")

    with section3:
        st.header("🔷 Alignment (Edit Mode)")
        design_file = st.file_uploader("Upload PNG diagram", type=["png"])
        if design_file:
            try:
                img = Image.open(design_file)
                st.image(img, caption="Alignment Diagram", use_container_width=True)
            except UnidentifiedImageError:
                st.warning("⚠️ Unable to preview this file format.")
        else:
            st.markdown("_No diagram uploaded._")