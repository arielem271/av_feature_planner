import streamlit as st
from graphviz import Digraph

# Sample data structure
features = {
    "Lateral": [
        {"name": "Lane Keeping Assist", "owner": "Alice", "usefulness": 85, "status": "Implemented"},
        {"name": "Lane Change Assist", "owner": "Bob", "usefulness": 78, "status": "Defined"},
        {"name": "Emergency Lane Return", "owner": "Carol", "usefulness": 90, "status": "Verified"}
    ],
    "Longitudinal": [
        {"name": "Adaptive Cruise Control", "owner": "Dave", "usefulness": 88, "status": "Implemented"},
        {"name": "Traffic Jam Assist", "owner": "Eve", "usefulness": 76, "status": "Defined"},
        {"name": "Automatic Emergency Braking", "owner": "Frank", "usefulness": 92, "status": "Verified"}
    ],
    "Urban/Rural": [
        {"name": "Traffic Sign Recognition", "owner": "Grace", "usefulness": 80, "status": "Implemented"},
        {"name": "Pedestrian Detection", "owner": "Heidi", "usefulness": 89, "status": "Implemented"},
        {"name": "Cross Traffic Alert", "owner": "Ivan", "usefulness": 75, "status": "Defined"}
    ],
    "System": [
        {"name": "Driver Monitoring", "owner": "Judy", "usefulness": 84, "status": "Verified"},
        {"name": "OTA Update Support", "owner": "Ken", "usefulness": 77, "status": "Defined"},
        {"name": "Sensor Fusion Health", "owner": "Leo", "usefulness": 82, "status": "Implemented"}
    ]
}

st.title("Feature Tree Viewer")
st.sidebar.header("Filters")
status_filter = st.sidebar.multiselect("Select statuses to display:", ["Defined", "Implemented", "Verified"],
                                       default=["Defined", "Implemented", "Verified"])

# Build Graphviz tree
dot = Digraph()
dot.node("Root", "Features")

for family, feats in features.items():
    dot.node(family)
    dot.edge("Root", family)
    for feat in feats:
        if feat["status"] in status_filter:
            label = f"{feat['name']}\nOwner: {feat['owner']}\nUsefulness: {feat['usefulness']}\nStatus: {feat['status']}"
            dot.node(feat['name'], label)
            dot.edge(family, feat['name'])

st.graphviz_chart(dot)

# Editing form
st.sidebar.header("Edit Feature")
selected_family = st.sidebar.selectbox("Family:", list(features.keys()))
selected_feature = st.sidebar.selectbox("Feature:", [f["name"] for f in features[selected_family]])

for feat in features[selected_family]:
    if feat["name"] == selected_feature:
        new_owner = st.sidebar.text_input("Owner:", feat["owner"])
        new_usefulness = st.sidebar.slider("Usefulness:", 1, 100, feat["usefulness"])
        new_status = st.sidebar.selectbox("Status:", ["Defined", "Implemented", "Verified"],
                                          index=["Defined", "Implemented", "Verified"].index(feat["status"]))

        if st.sidebar.button("Update Feature"):
            feat["owner"] = new_owner
            feat["usefulness"] = new_usefulness
            feat["status"] = new_status
            st.experimental_rerun()

# Export (screenshot suggestion)
st.sidebar.markdown("To export the tree, use the browser's screenshot or print to PDF feature.")
