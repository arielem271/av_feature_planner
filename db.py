from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///app_data.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    status = Column(String)

    goal = Column(Text)
    customer_internal = Column(Text)
    feature_spec_link = Column(String)
    activity_type = Column(String)
    stage = Column(String)
    usefulness = Column(Integer)
    quality = Column(Text)
    timeline_required = Column(String)
    timeline_planned = Column(String)
    timeline_committed = Column(String)

    sys1_status = Column(String)
    sys2_status = Column(String)

    trigger = Column(String)
    owned_by = Column(String)
    alignment_notes = Column(Text)

    updated_at = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
