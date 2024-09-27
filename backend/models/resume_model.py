from sqlalchemy import Column, Integer, String, ForeignKey, TEXT
from sqlalchemy.orm import relationship
from database import db

class Resume(db.Model):
    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    summary = Column(TEXT, nullable=True)  # Summary or objective statement
    education = Column(TEXT, nullable=True)  # Educational background
    experience = Column(TEXT, nullable=True)  # Work experience
    skills = Column(TEXT, nullable=True)  # Relevant skills

    user = relationship("User", back_populates="resumes")

    def __repr__(self):
        return f'<Resume {self.id}>'
