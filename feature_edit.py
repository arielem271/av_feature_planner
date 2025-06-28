import streamlit as st
from db import SessionLocal, Feature
from datetime import datetime, date

def safe_date(value):
    """Convert DB string to date or return today if invalid."""
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
        feature.status = st.selectbox(
            "Status",
            ["Planning", "Development", "Completed"],
            index=["Planning", "Development", "Completed"].index(feature.status) if feature.status else 0
        )
        feature.quality = st.text_area("Quality", feature.quality or "")
        feature.usefulness = st.slider("Usefulness", 1, 100, feature.usefulness or 50)

        feature.timeline_required = st.date_input("Timeline Required", safe_date(feature.timeline_required)).isoformat()
        feature.timeline_planned = st.date_input("Timeline Planned", safe_date(feature.timeline_planned)).isoformat()
        feature.timeline_committed = st.date_input("Timeline Committed", safe_date(feature.timeline_committed)).isoformat()

        with st.expander("Requirements"):
            feature.sys1_status = st.selectbox(
                "Sys1 Status",
                ["Defined", "In Progress", "Done"],
                index=["Defined", "In Progress", "Done"].index(feature.sys1_status) if feature.sys1_status else 0
            )
            feature.sys2_status = st.selectbox(
                "Sys2 Status",
                ["Defined", "In Progress", "Done"],
                index=["Defined", "In Progress", "Done"].index(feature.sys2_status) if feature.sys2_status else 0
            )

        with st.expander("Alignment"):
            feature.trigger = st.text_input("Trigger", feature.trigger or "")
            feature.owned_by = st.text_input("Owned By", feature.owned_by or "")
            feature.alignment_notes = st.text_area("Alignment Notes", feature.alignment_notes or "")

        if st.form_submit_button("💾 Save Updates"):
            db.commit()
            st.success("✅ Feature updated!")
