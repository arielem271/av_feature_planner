from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite DB for easy prototyping; swap URL for Postgres/MySQL later
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

def init_db():
    Base.metadata.create_all(bind=engine)