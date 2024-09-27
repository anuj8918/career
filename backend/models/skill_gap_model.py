from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.mysql import JSON  # Use JSON type for MySQL
from sqlalchemy.orm import relationship
from app import db

class SkillGap(db.Model):
    __tablename__ = 'skill_gaps'

    id = Column(Integer, primary_key=True)
    gap_skills = Column(JSON, nullable=False)  # Change ARRAY to JSON for MySQL
    career_id = Column(Integer, ForeignKey('careers.id'))

    def __init__(self, gap_skills, career_id):
        self.gap_skills = gap_skills
        self.career_id = career_id

    def __repr__(self):
        return f"<SkillGap {self.gap_skills}>"
