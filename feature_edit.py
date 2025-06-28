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
    selected = st.selectbox("Select feature", names)

    if not selected:
        st.info("Please select a feature to edit.")
        return

    feature = db.query(Feature).filter(Feature.name == selected).first()

    with st.form("edit_form"):
        feature.status = st.selectbox("Status", ["Planning", "Development", "Completed"],
                                      index=["Planning", "Development", "Completed"].index(feature.status) if feature.status else 0)
        feature.quality = st.text_area("Quality", feature.quality or "")
        feature.usefulness = st.slider("Usefulness", 1, 100, feature.usefulness or 50)
        feature.timeline_required = st.date_input("Timeline Required", safe_date(feature.timeline_required)).isoformat()
        feature.timeline_planned = st.date_input("Timeline Planned", safe_date(feature.timeline_planned)).isoformat()
        feature.timeline_committed = st.date_input("Timeline Committed", safe_date(feature.timeline_committed)).isoformat()

        with st.expander("Requirements"):
            feature.sys1_defined = st.checkbox("SYS1 Defined", feature.sys1_defined or False)
            feature.sys1_implemented = st.checkbox("SYS1 Implemented", feature.sys1_implemented or False)
            feature.sys1_verified = st.checkbox("SYS1 Verified", feature.sys1_verified or False)
            feature.sys2_defined = st.checkbox("SYS2 Defined", feature.sys2_defined or False)
            feature.sys2_implemented = st.checkbox("SYS2 Implemented", feature.sys2_implemented or False)
            feature.sys2_verified = st.checkbox("SYS2 Verified", feature.sys2_verified or False)

        with st.expander("Alignment"):
            feature.linked_components = st.text_input("Linked Components", feature.linked_components or "")
            feature.triggered_components = st.text_input("Triggered Components", feature.triggered_components or "")
            feature.trigger_event = st.text_input("Trigger Event", feature.trigger_event or "")
            feature.owned_by = st.text_input("Owned By", feature.owned_by or "")
            feature.alignment_notes = st.text_area("Alignment Notes", feature.alignment_notes or "")

        if st.form_submit_button("💾 Save Updates"):
            db.commit()
            st.success("✅ Feature updated!")
