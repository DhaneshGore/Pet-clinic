import os

class Config:
    # Set up the database URI (SQLite for this case)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///petclinic.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
