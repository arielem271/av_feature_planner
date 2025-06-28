import streamlit as st
from db import SessionLocal, Feature
import pandas as pd

def show_feature_view():
    st.title("📊 View Features")
    db = SessionLocal()
    features = db.query(Feature).all()

    if not features:
        st.info("No features found.")
        return

    data = [{
        "Name": f.name,
        "Updated At": f.updated_at,
        "Status": f.status,
        "Usefulness": f.usefulness,
        "Quality": f.quality
    } for f in features]

    df = pd.DataFrame(data).sort_values("Updated At", ascending=False)
    st.dataframe(df)
