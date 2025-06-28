import streamlit as st
from db import init_db
from feature_definition import show_feature_definition
from feature_edit import show_feature_edit
from feature_view import show_feature_view
from manage_features import show_manage_features

# Initialize DB (creates tables if they don't exist)
init_db()

st.set_page_config(page_title="AV Feature Planner", layout="wide")

# Define tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Manage Features",
    "Feature Definition",
    "Edit Features",
    "View Features"
])

with tab1:
    show_manage_features()

with tab2:
    show_feature_definition()

with tab3:
    show_feature_edit()

with tab4:
    show_feature_view()
