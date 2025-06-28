import streamlit as st
from db import SessionLocal, Feature
import pandas as pd

def show_feature_view():
    st.title("📊 View Features")
    db = SessionLocal()

    features = db.query(Feature).all()

    data = [{
        "Name": f.name,
        "Updated At": f.updated_at,
        "Status": f.status,
        "Usefulness": f.usefulness,
        "Quality": f.quality
    } for f in features]

    df = pd.DataFrame(data)
    st.dataframe(df)

    for f in features:
        if st.button(f"🗑 Remove '{f.name}'"):
            db.delete(f)
            db.commit()
            st.success(f"Removed feature {f.name}")
            st.experimental_rerun()
