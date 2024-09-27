from sqlalchemy import Column, Integer, String, ARRAY, JSON
from sqlalchemy.orm import relationship
from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    skills = Column(ARRAY(String), nullable=True)
    interests = Column(ARRAY(String), nullable=True)
    personality_quiz_results = Column(JSON, nullable=True)
    career_preferences = Column(JSON, nullable=True)

    # Relationship to Resume
    resumes = relationship("Resume", back_populates="user")

    def __repr__(self):
        return f'<User {self.name}>'
