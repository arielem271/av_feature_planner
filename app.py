import streamlit as st
from feature_view import show_feature_view
from feature_edit import show_feature_edit

import streamlit as st
from db import init_db
from feature_view import show_feature_view
from feature_edit import show_feature_edit

# 🟢 Initialize DB once at app start
init_db()

# 🟢 Set up Streamlit page
st.set_page_config(page_title="AV Feature Planner", layout="wide")

# 🟢 Create tabs
tabs = st.tabs(["📊 View Features", "✏️ Edit Features"])

with tabs[0]:
    show_feature_view()

with tabs[1]:
    show_feature_edit()
