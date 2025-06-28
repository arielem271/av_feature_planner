import streamlit as st
from db import SessionLocal, Feature

def show_feature_edit():
    st.title("✏️ Edit Features")
    db = SessionLocal()
    features = db.query(Feature).all()

    if not features:
        st.info("No features to edit.")
        return

    names = [f.name for f in features]
    selected = st.selectbox("Select feature to edit", names)
    feature = db.query(Feature).filter(Feature.name == selected).first()

    if feature:
        feature.status = st.selectbox("Status", ["Planning", "Development", "Completed"], index=["Planning", "Development", "Completed"].index(feature.status) if feature.status else 0)
        feature.quality = st.text_area("Quality", feature.quality or "")
        feature.timeline_required = st.text_input("Timeline Required", feature.timeline_required or "")
        feature.timeline_planned = st.text_input("Timeline Planned", feature.timeline_planned or "")
        feature.timeline_committed = st.text_input("Timeline Committed", feature.timeline_committed or "")

        if st.button("💾 Save Updates"):
            db.commit()
            st.success("✅ Feature updated!")