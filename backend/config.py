import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Anuj@123@localhost:3306/career_advisor_db'
)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
