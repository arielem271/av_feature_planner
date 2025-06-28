import streamlit as st
from db import SessionLocal, Feature, init_db

def show_feature_edit():
    st.header("✏️ Feature Editor")
    init_db()
    db = SessionLocal()
    name = st.text_input("Feature Name")
    desc = st.text_area("Feature Description")
    status = st.selectbox("Status", ["Planning", "Development", "Completed"])
    if st.button("Add / Update Feature"):
        existing = db.query(Feature).filter(Feature.name == name).first()
        if existing:
            existing.description = desc
            existing.status = status
            st.success("Feature updated.")
        else:
            f = Feature(name=name, description=desc, status=status)
            db.add(f)
            st.success("Feature added.")
        db.commit()