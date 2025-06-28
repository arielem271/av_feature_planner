from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Setup DB
engine = create_engine("sqlite:///app_data.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Feature model
class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    theme = Column(String)
    goal = Column(String)
    usefulness = Column(Integer)
    quality = Column(String)
    timeline_required = Column(String)

    requirements = relationship("Requirement", back_populates="feature")
    alignments = relationship("Alignment", back_populates="feature")

# Requirement model
class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, index=True)
    feature_id = Column(Integer, ForeignKey("features.id"))
    spec = Column(String)
    verification = Column(String)
    status = Column(String)

    feature = relationship("Feature", back_populates="requirements")

# Alignment model
class Alignment(Base):
    __tablename__ = "alignments"

    id = Column(Integer, primary_key=True, index=True)
    feature_id = Column(Integer, ForeignKey("features.id"))
    system = Column(String)
    design_status = Column(String)
    design_upload = Column(String)
    polarion_link = Column(String)

    feature = relationship("Feature", back_populates="alignments")

# Initialize DB (create tables)
def init_db():
    Base.metadata.create_all(bind=engine)
