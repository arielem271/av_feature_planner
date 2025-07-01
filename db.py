from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///app_data.db')
SessionLocal = sessionmaker(bind=engine)

# --- Theme ---
class Theme(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

# --- Feature ---
class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    theme_id = Column(Integer, ForeignKey('themes.id'))
    parent_id = Column(Integer, ForeignKey('features.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = Column(String)

    theme = relationship('Theme')
    parent = relationship('Feature', remote_side=[id])

# --- Sys2ReqMaster ---
class Sys2ReqMaster(Base):
    __tablename__ = 'sys2req_master'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    planning_status = Column(String)
    alignment_status = Column(String)
    arch_status = Column(String)
    safety_status = Column(String)
    development_status = Column(String)
    validation_status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = Column(String)

# --- Sys2ReqMasterHistory ---
class Sys2ReqMasterHistory(Base):
    __tablename__ = 'sys2req_master_history'
    id = Column(Integer, primary_key=True)
    sys2req_master_id = Column(Integer, ForeignKey('sys2req_master.id'))
    description = Column(String)
    planning_status = Column(String)
    alignment_status = Column(String)
    arch_status = Column(String)
    safety_status = Column(String)
    development_status = Column(String)
    validation_status = Column(String)
    changed_at = Column(DateTime, default=datetime.utcnow)
    changed_by = Column(String)

# --- Sys2ReqInstance ---
class Sys2ReqInstance(Base):
    __tablename__ = 'sys2req_instance'
    id = Column(Integer, primary_key=True)
    feature_id = Column(Integer, ForeignKey('features.id'))
    sys2req_master_id = Column(Integer, ForeignKey('sys2req_master.id'))

# --- Domain template ---
def create_domain_classes():
    domain_defs = {
        'policy': ['planning_status', 'development_status'],
        'perception': ['planning_status', 'development_status'],
        'avx': ['planning_status', 'development_status'],
        'safety': ['alignment_status', 'development_status', 'verification_status'],
        'arch': ['alignment_status', 'arch_status', 'verification_status'],
        'avv': ['test_strategy', 'test_plan', 'test_report']
    }

    for domain, fields in domain_defs.items():
        attrs = {
            '__tablename__': domain,
            'id': Column(Integer, primary_key=True),
            'sys2req_master_id': Column(Integer, ForeignKey('sys2req_master.id')),
            'opted_out': Column(Boolean, default=False),
            'created_at': Column(DateTime, default=datetime.utcnow),
            'updated_at': Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
            'updated_by': Column(String)
        }
        for f in fields:
            attrs[f] = Column(String)
        DomainClass = type(domain.capitalize(), (Base,), attrs)

        # History class
        hist_attrs = {
            '__tablename__': f'{domain}_history',
            'id': Column(Integer, primary_key=True),
            f'{domain}_id': Column(Integer, ForeignKey(f'{domain}.id')),
            'changed_at': Column(DateTime, default=datetime.utcnow),
            'changed_by': Column(String)
        }
        for f in fields:
            hist_attrs[f] = Column(String)
        hist_attrs['opted_out'] = Column(Boolean)
        type(f'{domain.capitalize()}History', (Base,), hist_attrs)

create_domain_classes()

# --- Create tables ---
Base.metadata.create_all(engine)
