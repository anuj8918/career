from sqlalchemy import Column, Integer, String, ARRAY
from database import db

class CareerPath(db.Model):
    __tablename__ = 'career_paths'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    required_skills = Column(ARRAY(String), nullable=False)
    industry = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)

    def __repr__(self):
        return f'<CareerPath {self.name}>'
