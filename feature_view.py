import streamlit as st
from db import SessionLocal, Feature

def show_feature_view():
    st.title("📊 View Features")
    db = SessionLocal()
    features = db.query(Feature).all()

    if not features:
        st.info("No features found.")
        return

    for f in features:
        st.markdown(f"### {f.name}")
        st.markdown(f"**Goal:** {f.goal or ''}")
        st.markdown(f"**Customer/Internal:** {f.customer_internal or ''}")
        st.markdown(f"**Status:** {f.status or ''}")
        st.markdown(f"**Usefulness:** {f.usefulness or ''}")
        st.markdown(f"**Quality:** {f.quality or ''}")
        st.markdown(f"**Timelines:** Required: {f.timeline_required or ''}, Planned: {f.timeline_planned or ''}, Committed: {f.timeline_committed or ''}")
        st.divider()