from sqlalchemy import Column, Integer, String, JSON
from database import db

class JobMarket(db.Model):
    __tablename__ = 'job_market'

    id = Column(Integer, primary_key=True)
    role = Column(String(100), nullable=False)
    market_data = Column(JSON, nullable=False)  # Includes demand, salary trends, etc.

    def __repr__(self):
        return f'<JobMarket {self.role}>'
