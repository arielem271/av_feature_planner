import streamlit as st
import streamlit.components.v1 as components
import json

# --- Main UI function ---
def show_main_ui():
    st.title("🚀 Main Flow")
    st.write("This is your main app UI.")

# --- Tree View Pilot with focused tree and icons ---
def show_tree_view_pilot():
    st.title("🌳 Feature & Sys2 Tree View (Pilot)")

    if "tree_data" not in st.session_state:
        st.session_state.tree_data = [
            {"id": "lateral", "parent": "#", "text": "Lateral", "icon": "jstree-folder"},
            {"id": "longitudinal", "parent": "#", "text": "Longitudinal", "icon": "jstree-folder"},
            {"id": "urban_rural", "parent": "#", "text": "Urban/Rural", "icon": "jstree-folder"},
            {"id": "system", "parent": "#", "text": "System", "icon": "jstree-folder"}
        ]

    # Render fancy tree using jsTree via iframe
    tree_data_json = json.dumps(st.session_state.tree_data)
    html_code = f"""
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.12/themes/default/style.min.css\" />
    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js\"></script>
    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.12/jstree.min.js\"></script>
    <div id=\"jstree_demo\"></div>
    <script>
    $(function() {{
        $('#jstree_demo').jstree({{
            'core': {{
                'data': {tree_data_json}
            }}
        }});
    }});
    </script>
    """
    components.html(html_code, height=500)

    with st.expander("➕ Add / Remove Elements"):
        add_type = st.radio("Type", ["Feature", "Sys2"], horizontal=True)
        new_name = st.text_input("Name of new element")
        parent = st.selectbox("Parent Node", [node['text'] for node in st.session_state.tree_data])

        if st.button("Add"):
            if not new_name.strip():
                st.warning("Name cannot be empty.")
            else:
                parent_id = next((node['id'] for node in st.session_state.tree_data if node['text'] == parent), None)
                new_id = f"{parent_id}_{new_name.lower().replace(' ', '_')}"
                icon = "jstree-folder" if add_type == "Feature" else "jstree-file"
                st.session_state.tree_data.append({
                    "id": new_id,
                    "parent": parent_id,
                    "text": new_name,
                    "icon": icon
                })
                st.success(f"Added {add_type}: {new_name}")

# --- App layout ---
tab1, tab2 = st.tabs(["🚀 Main Flow", "🌳 Tree View Pilot"])

with tab1:
    show_main_ui()

with tab2:
    show_tree_view_pilot()
