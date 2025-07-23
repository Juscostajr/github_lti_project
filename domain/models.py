from dataclasses import dataclass
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

@dataclass
class Commit:
    sha: str
    author: str
    message: str
    date: datetime

@dataclass
class Contributor:
    login: str
    avatar_url: str
    contributions: int

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    github_repo_url = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    last_modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    deliveries = relationship("Delivery", back_populates="activity")
    histories = relationship("ActivityHistory", back_populates="activity")

class Delivery(Base):
    __tablename__ = "deliveries"
    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    student_id = Column(Integer, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    last_modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    activity = relationship("Activity", back_populates="deliveries")

class ActivityHistory(Base):
    __tablename__ = "activity_histories"
    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    activity = relationship("Activity", back_populates="histories")

if __name__ == "__main__":
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///test_manual.db", echo=True)
    print("Creating tables manually...")
    Base.metadata.create_all(bind=engine)
    print("Done.")