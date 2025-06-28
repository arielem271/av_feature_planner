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
    theme = Column(String)
    goal = Column(Text)
    usefulness = Column(Integer)
    quality = Column(Text)
    timeline_required = Column(String)

    # SYS1 per platform
    sys1_61_link = Column(Text)
    sys1_61_total = Column(Integer)
    sys1_61_in_review = Column(Integer)
    sys1_61_approved = Column(Integer)
    sys1_61_rejected = Column(Integer)
    sys1_61_covered_sys2 = Column(Integer)
    sys1_61_partly_agreed = Column(Integer)
    sys1_61_to_be_clarified = Column(Integer)
    sys1_61_implemented = Column(Integer)

    sys1_62_link = Column(Text)
    sys1_62_total = Column(Integer)
    sys1_62_in_review = Column(Integer)
    sys1_62_approved = Column(Integer)
    sys1_62_rejected = Column(Integer)
    sys1_62_covered_sys2 = Column(Integer)
    sys1_62_partly_agreed = Column(Integer)
    sys1_62_to_be_clarified = Column(Integer)
    sys1_62_implemented = Column(Integer)

    sys1_63_link = Column(Text)
    sys1_63_total = Column(Integer)
    sys1_63_in_review = Column(Integer)
    sys1_63_approved = Column(Integer)
    sys1_63_rejected = Column(Integer)
    sys1_63_covered_sys2 = Column(Integer)
    sys1_63_partly_agreed = Column(Integer)
    sys1_63_to_be_clarified = Column(Integer)
    sys1_63_implemented = Column(Integer)

    sys1_64_link = Column(Text)
    sys1_64_total = Column(Integer)
    sys1_64_in_review = Column(Integer)
    sys1_64_approved = Column(Integer)
    sys1_64_rejected = Column(Integer)
    sys1_64_covered_sys2 = Column(Integer)
    sys1_64_partly_agreed = Column(Integer)
    sys1_64_to_be_clarified = Column(Integer)
    sys1_64_implemented = Column(Integer)

    # SYS2
    sys2_link = Column(Text)
    sys2_defined = Column(Integer)
    sys2_implemented = Column(Integer)
    sys2_verified = Column(Integer)

    # Owner alignment
    avx_status = Column(String)
    avx_quality = Column(String)
    avx_velocity = Column(String)

    policy_status = Column(String)
    policy_quality = Column(String)
    policy_velocity = Column(String)

    perception_status = Column(String)
    perception_quality = Column(String)
    perception_velocity = Column(String)

    # Triggered alignment
    avv_swe5_status = Column(String)
    avv_swe5_quality = Column(String)
    avv_swe5_velocity = Column(String)

    arch_sys3_status = Column(String)
    arch_sys3_quality = Column(String)
    arch_sys3_velocity = Column(String)

    safety_sys2_swe1_status = Column(String)
    safety_sys2_swe1_quality = Column(String)
    safety_sys2_swe1_velocity = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
