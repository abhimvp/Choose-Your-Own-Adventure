# frontend submits the job ->  backend returns the job -> frontend asks for status of job & backend sends the status of job
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from backend.db.database import Base


class StoryJob(Base):
    __tablename__ = 'story_jobs'

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String)
    story_id = Column(Integer, nullable=True)
    error = Column(String, nullable=True)  # nullable = True means it can have no value.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_job = Column(DateTime(timezone=True), nullable=True)
