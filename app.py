import streamlit as st
from db import init_db
from feature_definition import show_feature_definition
from feature_edit import show_feature_edit
from feature_view import show_feature_view

st.set_page_config(page_title="AV Feature Planner", layout="wide")

# Linear-inspired background + spacing
st.markdown(
    '''
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Init DB
init_db()

tabs = st.tabs(["🔧 Feature Definition", "✏️ Edit Features", "📊 View Features"])

with tabs[0]:
    show_feature_definition()

with tabs[1]:
    show_feature_edit()

with tabs[2]:
    show_feature_view()