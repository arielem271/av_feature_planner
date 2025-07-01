AV Feature Planner

Overview

This project implements a database-backed planner for managing AV features, Sys2 requirements, and their domain alignments. The design supports:

Feature hierarchy: Features can be parents or children of other features, and belong to one theme.

Sys2Req master-instance model: A master Sys2Req defines canonical data; instances link features to masters. Only masters hold domain data.

Domain data: Each Sys2Req master links optionally to domain records (Policy, Perception, AVX, Safety, Arch, AVV).

Full history tracking: Every change to Sys2ReqMaster and domain records is logged in history tables.

Audit fields: All records store created_at, updated_at, updated_by.

ER Diagram

See av_feature_planner_db_diagram.png for a visual overview.

Key Tables

Feature: Functional unit, with theme + hierarchy

Sys2ReqMaster: Canonical requirement definition

Sys2ReqInstance: Links feature to Sys2Req master

Domain tables: Policy, Perception, AVX, Safety, Arch, AVV — optional per Sys2ReqMaster

History tables: track changes to Sys2ReqMaster + domains

Getting Started

Ensure you have Python 3.8+ and required packages:

pip install sqlalchemy

Run db.py to create the database schema.

Use app.py or other modules to interact with the system.

To Do

Add role-based access control

Build views for each user role

Implement change history viewers

Files

db.py: Database models + schema creation

av_feature_planner_db_diagram.png: ER diagram

app.py, feature_definition.py: UI modules

Notes

Domain records must be explicitly opted out if not used.

Sys2Req inheritance is managed through instance links — updating the master propagates conceptually to all linked features.

