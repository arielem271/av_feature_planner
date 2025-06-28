import streamlit as st
from streamlit_tree_select import tree_select

# Initialize session state for the tree data if not already present
if "tree_data" not in st.session_state:
    st.session_state.tree_data = [
        {
            "label": "Lateral",
            "value": "lateral",
            "children": []
        },
        {
            "label": "Longitudinal",
            "value": "longitudinal",
            "children": []
        },
        {
            "label": "Urban/Rural",
            "value": "urban_rural",
            "children": []
        },
        {
            "label": "System",
            "value": "system",
            "children": []
        }
    ]

st.title("🌳 Feature & Sys2 Tree View (Pilot)")

# Show the tree view
selected = tree_select(
    tree=st.session_state.tree_data,
    checked=[],
    expanded=[node["value"] for node in st.session_state.tree_data],
)

st.write("Selected:", selected)

st.subheader("➕ Add Elements")

add_type = st.radio("What do you want to add?", ["Feature", "Sys2"])

new_name = st.text_input("Name of new element")

if st.button("Add"):
    if not selected.get("nodes"):
        st.warning("Please select a parent node to add under.")
    elif not new_name.strip():
        st.warning("Name cannot be empty.")
    else:
        # Find selected node and append
        def add_to_tree(tree, target_value, new_item):
            for node in tree:
                if node["value"] == target_value:
                    if "children" not in node:
                        node["children"] = []
                    node["children"].append(new_item)
                    return True
                if "children" in node:
                    if add_to_tree(node["children"], target_value, new_item):
                        return True
            return False

        parent_value = selected["nodes"][0]
        new_node = {
            "label": new_name,
            "value": f"{parent_value}_{new_name.lower().replace(' ', '_')}",
            "children": []
        } if add_type == "Feature" else {
            "label": new_name,
            "value": f"{parent_value}_{new_name.lower().replace(' ', '_')}"
        }

        added = add_to_tree(st.session_state.tree_data, parent_value, new_node)
        if added:
            st.success(f"Added {add_type}: {new_name}")
        else:
            st.error("Failed to add item. Please check your selection.")

st.write("Current Tree Data:")
st.json(st.session_state.tree_data)
