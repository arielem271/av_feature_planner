import streamlit as st
from datetime import date
from db import SessionLocal, Feature, Requirement, Alignment
from feature_constants import FEATURE_CONSTANTS

def show_feature_definition():
    st.title("🔧 AVF Product Plan")

    db = SessionLocal()

    # === Feature Creation Form ===
    theme = st.selectbox("Select Theme", list(FEATURE_CONSTANTS.keys()), key="feature_def_theme")
    features_list = [f["name"] for f in FEATURE_CONSTANTS[theme]]
    feature_name = st.selectbox("Select Feature", features_list, key="feature_def_name")

    goal = st.text_area("Goal / Motivation", key="feature_def_goal")
    usefulness = st.slider("Usefulness", 1, 100, 50, key="feature_def_usefulness")
    quality = st.text_area("Quality", key="feature_def_quality")
    timeline_required = st.date_input("Timeline Required", value=date.today(), key="feature_def_timeline")

    if st.button("💾 Save New Feature", key="feature_def_save"):
        existing = db.query(Feature).filter(Feature.name == feature_name).first()
        if existing:
            st.warning(f"⚠️ Feature '{feature_name}' already exists. Please edit it instead.")
        else:
            new_feature = Feature(
                name=feature_name,
                theme=theme,
                goal=goal,
                usefulness=usefulness,
                quality=quality,
                timeline_required=timeline_required.isoformat()
            )
            db.add(new_feature)
            db.commit()
            st.success(f"✅ Feature '{feature_name}' saved!")

    # === Existing Features + Requirements + Alignment ===
    show_existing_features(db)

def show_existing_features(db):
    st.header("📌 Existing Features")

    features = db.query(Feature).all()
    if not features:
        st.info("No features available yet.")
        return

    for feature in features:
        with st.expander(f"{feature.name}"):
            st.markdown(f"**Theme:** {feature.theme}")
            st.markdown(f"**Goal:** {feature.goal}")
            st.markdown(f"**Usefulness:** {feature.usefulness}")
            st.markdown(f"**Quality:** {feature.quality}")
            st.markdown(f"**Timeline Required:** {feature.timeline_required}")

            # === Requirements section
            st.subheader("Requirements")
            reqs = db.query(Requirement).filter(Requirement.feature_id == feature.id).all()
            if reqs:
                for req in reqs:
                    st.markdown(
                        f"- **ID:** {req.id}, **Spec:** {req.spec}, **Verification:** {req.verification}, **Status:** {req.status}"
                    )
            else:
                st.write("No requirements defined.")

            with st.form(key=f"add_req_form_{feature.id}"):
                spec = st.text_input("Spec", key=f"spec_{feature.id}")
                verification = st.text_input("Verification", key=f"ver_{feature.id}")
                status = st.selectbox("Status", ["Planned", "In Progress", "Done"], key=f"status_{feature.id}")
                submitted = st.form_submit_button("➕ Add Requirement")
                if submitted:
                    new_req = Requirement(
                        feature_id=feature.id,
                        spec=spec,
                        verification=verification,
                        status=status
                    )
                    db.add(new_req)
                    db.commit()
                    st.success("✅ Requirement added.")
                    st.experimental_rerun()

            # === Alignment section
            st.subheader("Alignment")
            aligns = db.query(Alignment).filter(Alignment.feature_id == feature.id).all()
            if aligns:
                for ali in aligns:
                    st.markdown(
                        f"- **System:** {ali.system}, **Design:** {ali.design_status}, "
                        f"**Upload:** {ali.design_upload}, **Polarion:** {ali.polarion_link}"
                    )
            else:
                st.write("No alignment data available.")

            with st.form(key=f"add_align_form_{feature.id}"):
                system = st.text_input("System", key=f"sys_{feature.id}")
                design_status = st.selectbox("Design Status", ["Planned", "In Progress", "Done"], key=f"design_{feature.id}")
                design_upload = st.text_input("Design Upload Link", key=f"upload_{feature.id}")
                polarion_link = st.text_input("Polarion Link", key=f"polarion_{feature.id}")
                submitted_align = st.form_submit_button("➕ Add Alignment")
                if submitted_align:
                    new_align = Alignment(
                        feature_id=feature.id,
                        system=system,
                        design_status=design_status,
                        design_upload=design_upload,
                        polarion_link=polarion_link
                    )
                    db.add(new_align)
                    db.commit()
                    st.success("✅ Alignment added.")
                    st.experimental_rerun()
