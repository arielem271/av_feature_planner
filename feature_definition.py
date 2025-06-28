import streamlit as st
from datetime import date
from feature_constants import FEATURE_CONSTANTS

def show_feature_definition():
    st.title("🔧 Feature Definition")

    # Dynamic theme + feature selection from FEATURE_CONSTANTS
    theme = st.selectbox("Select Theme", list(FEATURE_CONSTANTS.keys()))
    features = [f["name"] for f in FEATURE_CONSTANTS[theme]]
    feature_name = st.selectbox("Select Feature", features)

    goal = st.text_area("Goal / Motivation")
    usefulness = st.slider("Usefulness", 1, 100, 50)
    quality = st.text_area("Quality")
    timeline_required = st.date_input("Timeline Required", value=date.today())

    # Requirements - SYS1
    with st.expander("Requirements - SYS1 Table"):
        for platform in [61, 62, 63, 64]:
            enabled = st.checkbox(f"Enable Platform {platform}", key=f"enable_sys1_{platform}")
            cols = st.columns(10)
            with cols[0]:
                st.markdown(f"**Platform {platform}**")
            with cols[1]:
                st.text_input("Link to Polarion", key=f"polarion_{platform}", disabled=not enabled)
            with cols[2]:
                st.number_input("Total", min_value=0, key=f"total_{platform}", disabled=not enabled)
            with cols[3]:
                st.number_input("In Review", min_value=0, key=f"in_review_{platform}", disabled=not enabled)
            with cols[4]:
                st.number_input("Approved", min_value=0, key=f"approved_{platform}", disabled=not enabled)
            with cols[5]:
                st.number_input("Rejected", min_value=0, key=f"rejected_{platform}", disabled=not enabled)
            with cols[6]:
                st.number_input("Covered by SYS2", min_value=0, key=f"covered_sys2_{platform}", disabled=not enabled)
            with cols[7]:
                st.number_input("Partly Agreed", min_value=0, key=f"partly_agreed_{platform}", disabled=not enabled)
            with cols[8]:
                st.number_input("To Be Clarified", min_value=0, key=f"to_be_clarified_{platform}", disabled=not enabled)
            with cols[9]:
                st.number_input("Implemented", min_value=0, key=f"implemented_{platform}", disabled=not enabled)

    # Requirements - SYS2
    with st.expander("Requirements - SYS2 Table"):
        cols = st.columns([2, 1, 1, 1])
        with cols[0]:
            st.text_input("Link to Polarion", key="sys2_polarion")
        with cols[1]:
            st.number_input("Defined", min_value=0, key="sys2_defined")
        with cols[2]:
            st.number_input("Implemented", min_value=0, key="sys2_implemented")
        with cols[3]:
            st.number_input("Verified", min_value=0, key="sys2_verified")

    # Alignment - Owner
    with st.expander("Alignment - Owner Components"):
        for comp in ["AVX", "Policy", "Perception"]:
            st.markdown(f"**{comp}**")
            cols = st.columns(3)
            with cols[0]:
                st.selectbox("Alignment Status",
                             ["Aligned (effort estimation required)", "Aligned (timeline committed)", "Partial", "Pending"],
                             key=f"{comp}_align")
            with cols[1]:
                st.selectbox("Quality",
                             ["none", "test strategy", "strategy + test plan", "strategy + test plan + report"],
                             key=f"{comp}_quality")
            with cols[2]:
                st.text_input("Velocity", key=f"{comp}_velocity")

    # Alignment - Triggered
    with st.expander("Alignment - Triggered Components"):
        for comp in ["AVV SWE5", "Architecture SYS3", "Safety SYS2 / SWE1"]:
            st.markdown(f"**{comp}**")
            cols = st.columns(3)
            with cols[0]:
                st.selectbox("Alignment Status",
                             ["Aligned (effort estimation required)", "Aligned (timeline committed)", "Partial", "Pending"],
                             key=f"{comp}_align")
            with cols[1]:
                st.selectbox("Quality",
                             ["none", "test strategy", "strategy + test plan", "strategy + test plan + report"],
                             key=f"{comp}_quality")
            with cols[2]:
                st.text_input("Velocity", key=f"{comp}_velocity")

    if st.button("💾 Save (UI Only)"):
        st.success("✅ Data captured (not saved to DB)")
