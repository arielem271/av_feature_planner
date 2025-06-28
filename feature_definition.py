import streamlit as st
from PIL import Image, UnidentifiedImageError
from db import SessionLocal, Feature, init_db
from feature_constants import FEATURE_CONSTANTS
from datetime import date, datetime

def safe_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return date.today()

def show_feature_definition():
    st.title("🔧 Feature Definition")
    init_db()
    db = SessionLocal()

    # Add / Remove Feature
    with st.expander("➕➖ Manage Features for Theme"):
        theme = st.selectbox("Theme for Management", list(FEATURE_CONSTANTS.keys()), key="theme_mgmt")
        if "features_custom" not in st.session_state:
            st.session_state.features_custom = FEATURE_CONSTANTS.copy()

        new_name = st.text_input("New Feature Name")
        new_id = st.text_input("New Feature ID")
        if st.button("Add Feature"):
            if new_name and new_id:
                st.session_state.features_custom[theme].append({"name": new_name, "id": new_id})
                st.success(f"Added {new_name} to {theme}")

        existing_names = [f["name"] for f in st.session_state.features_custom[theme]]
        remove_name = st.selectbox("Remove Feature", existing_names)
        if st.button("Remove Selected Feature"):
            st.session_state.features_custom[theme] = [f for f in st.session_state.features_custom[theme] if f["name"] != remove_name]
            st.success(f"Removed {remove_name}")

    # Main form
    theme = st.selectbox("Select Theme", list(FEATURE_CONSTANTS.keys()), key="theme_select")
    feature_list = st.session_state.get("features_custom", FEATURE_CONSTANTS)[theme]
    cols = st.columns(3)

    if "selected_feature" not in st.session_state:
        st.session_state.selected_feature = None

    for idx, feature in enumerate(feature_list):
        col = cols[idx % 3]
        existing = db.query(Feature).filter(Feature.name == feature["name"]).first()
        label = f"{'✅' if existing else '🆕'} {feature['name']} ({feature['id']})"
        if col.button(label, key=f"btn_{feature['id']}", use_container_width=True):
            st.session_state.selected_feature = feature

    if st.session_state.selected_feature:
        st.success(f"✅ Selected: {st.session_state.selected_feature['name']}")
        if st.button("🗑 Clear Selection"):
            st.session_state.selected_feature = None
            st.experimental_rerun()

        existing = db.query(Feature).filter(Feature.name == st.session_state.selected_feature["name"]).first()

        with st.form("feature_form"):
            data = {}
            data["name"] = st.session_state.selected_feature["name"]
            data["goal"] = st.text_area("Goal", existing.goal if existing else "")
            data["customer_internal"] = st.text_area("Customer/Internal", existing.customer_internal if existing else "")
            data["feature_spec_link"] = st.text_input("Spec Link", existing.feature_spec_link if existing else "")
            data["activity_type"] = st.selectbox("Activity Type", ["Initiation", "Ongoing", "Change Request"])
            data["stage"] = st.selectbox("Stage", ["Planning", "Development", "Both"])
            data["usefulness"] = st.slider("Usefulness", 1, 100, existing.usefulness if existing and existing.usefulness else 50)
            data["quality"] = st.text_area("Quality", existing.quality if existing else "")

            data["timeline_required"] = st.date_input("Timeline Required", safe_date(existing.timeline_required if existing else None)).isoformat()
            data["timeline_planned"] = st.date_input("Timeline Planned", safe_date(existing.timeline_planned if existing else None)).isoformat()
            data["timeline_committed"] = st.date_input("Timeline Committed", safe_date(existing.timeline_committed if existing else None)).isoformat()

            with st.expander("Requirements"):
                data["sys1_status"] = st.selectbox("Sys1 Status", ["Defined", "In Progress", "Done"],
                                                   index=["Defined", "In Progress", "Done"].index(existing.sys1_status) if existing and existing.sys1_status else 0)
                data["sys2_status"] = st.selectbox("Sys2 Status", ["Defined", "In Progress", "Done"],
                                                   index=["Defined", "In Progress", "Done"].index(existing.sys2_status) if existing and existing.sys2_status else 0)

            with st.expander("Alignment"):
                data["trigger"] = st.text_input("Trigger", existing.trigger if existing else "")
                data["owned_by"] = st.text_input("Owned By", existing.owned_by if existing else "")
                data["alignment_notes"] = st.text_area("Alignment Notes", existing.alignment_notes if existing else "")

            data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if st.form_submit_button("💾 Save Feature"):
                if existing:
                    for k, v in data.items():
                        setattr(existing, k, v)
                    st.success("✅ Feature updated!")
                else:
                    f = Feature(**data)
                    db.add(f)
                    st.success("✅ Feature added!")
                db.commit()
