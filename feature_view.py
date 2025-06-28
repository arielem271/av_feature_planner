import streamlit as st
from db import SessionLocal, Feature

def show_feature_view():
    st.header("📊 Feature View")
    db = SessionLocal()
    features = db.query(Feature).all()
    if not features:
        st.info("No features in the database.")
        return
    for f in features:
        st.markdown(f"**{f.name}** - {f.status}")
        st.text(f.description)