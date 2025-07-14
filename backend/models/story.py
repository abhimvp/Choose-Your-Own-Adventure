from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, JSON
# sqlalchemy is an ORM(which is an Object Relational Mapping) similarly how we mapped the settings from our environment
# variables into this kind of python class. FASTAPI has these modules like sqlalchemy that allow us to map data into
# these python classes so we don't need to write sql code. we can use standard python operations and this library will
# handle all of the complexity of converting that into SQL and working with our Database.
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base


class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship("StoryNode", back_populates="story")


class StoryNode(Base):
    __tablename__ = 'story_nodes'
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey('stories.id'), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)

    story = relationship("Story", back_populates="nodes")
