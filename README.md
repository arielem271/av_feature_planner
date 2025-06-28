# AV Feature Planner

This is a starter project for managing AV features with Streamlit + SQLite.

## Run locally
```
streamlit run app.py
```

## Deployment target
- Streamlit Cloud (https://streamlit.io/cloud)

## DB
- Starts with SQLite, easy to migrate to Postgres/MySQL

## Structure
- `app.py` main entry
- `db.py` database models
- `feature_view.py` view logic
- `feature_edit.py` edit logic
- `jira_integration.py` placeholder for future Jira API