import streamlit as st
from datetime import date
from db import SessionLocal, Feature
from feature_constants import FEATURE_CONSTANTS

def show_manage_features():
    st.title("🛠️ Manage Features")

    db = SessionLocal()

    action = st.radio("Select Action", ["Add Feature", "Delete Feature"], key="manage_action")

    if action == "Add Feature":
        theme = st.selectbox("Select Theme", list(FEATURE_CONSTANTS.keys()), key="manage_theme")
        feature_name = st.text_input("Enter New Feature Name", key="manage_new_name")

        goal = st.text_area("Goal / Motivation", key="manage_goal")
        usefulness = st.slider("Usefulness", 1, 100, 50, key="manage_usefulness")
        quality = st.text_area("Quality", key="manage_quality")
        timeline_required = st.date_input("Timeline Required", value=date.today(), key="manage_timeline")

        if st.button("💾 Save New Feature", key="manage_save"):
            if not feature_name.strip():
                st.warning("⚠️ Please enter a feature name.")
            else:
                existing = db.query(Feature).filter(Feature.name == feature_name).first()
                if existing:
                    st.warning(f"⚠️ A feature named '{feature_name}' already exists.")
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
                    st.success(f"✅ Feature '{feature_name}' saved (ID: {new_feature.id})!")

    elif action == "Delete Feature":
        features_in_db = db.query(Feature).all()
        if not features_in_db:
            st.info("No features available to delete.")
            return

        feature_names = [f.name for f in features_in_db]
        selected_name = st.selectbox("Select Feature to Delete", feature_names, key="manage_delete_select")

        if st.button("🗑️ Delete Feature", key="manage_delete"):
            f = db.query(Feature).filter(Feature.name == selected_name).first()
            if f:
                db.delete(f)
                db.commit()
                st.success(f"✅ Feature '{selected_name}' deleted.")
            else:
                st.error("❌ Feature not found in DB.")
