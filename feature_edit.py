import streamlit as st
from db import SessionLocal, Feature
from datetime import datetime, date

def safe_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return date.today()

def show_feature_edit():
    st.title("✏️ Edit Features")
    db = SessionLocal()
    features = db.query(Feature).all()

    if not features:
        st.info("No features to edit.")
        return

    names = [f.name for f in features]
    selected = st.selectbox("Select feature", names, key="feature_edit_select")

    if not selected:
        st.info("Please select a feature to edit.")
        return

    feature = db.query(Feature).filter(Feature.name == selected).first()

    with st.form("edit_form"):
        quality = st.text_area("Quality", feature.quality or "", key="feature_edit_quality")
        usefulness = st.slider("Usefulness", 1, 100, feature.usefulness or 50, key="feature_edit_usefulness")
        timeline_required = st.date_input("Timeline Required", safe_date(feature.timeline_required), key="feature_edit_timeline")

        if st.form_submit_button("💾 Save Updates"):
            feature.quality = quality
            feature.usefulness = usefulness
            feature.timeline_required = timeline_required.isoformat()

            db.commit()
            st.success("✅ Feature updated!")
