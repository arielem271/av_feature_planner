import streamlit as st
from db import SessionLocal, Feature, Requirement, Alignment

def show_feature_view():
    st.title("🔍 View Features")

    db = SessionLocal()
    features = db.query(Feature).all()

    if not features:
        st.info("No features found.")
        return

    for feature in features:
        with st.expander(f"{feature.name}"):
            st.markdown(f"**Theme:** {feature.theme}")
            st.markdown(f"**Goal:** {feature.goal}")
            st.markdown(f"**Usefulness:** {feature.usefulness}")
            st.markdown(f"**Quality:** {feature.quality}")
            st.markdown(f"**Timeline Required:** {feature.timeline_required}")

            # Requirements section
            st.subheader("Requirements")
            reqs = db.query(Requirement).filter(Requirement.feature_id == feature.id).all()
            if reqs:
                for req in reqs:
                    st.markdown(f"- **ID:** {req.id}, **Spec:** {req.spec}, **Verification:** {req.verification}, **Status:** {req.status}")
            else:
                st.write("No requirements defined.")

            # Alignment section
            st.subheader("Alignment")
            aligns = db.query(Alignment).filter(Alignment.feature_id == feature.id).all()
            if aligns:
                for ali in aligns:
                    st.markdown(f"- **System:** {ali.system}, **Design:** {ali.design_status}, **Upload:** {ali.design_upload}, **Polarion:** {ali.polarion_link}")
            else:
                st.write("No alignment data available.")
