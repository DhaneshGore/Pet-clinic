import os

class Config:
    # Update this with the correct path to your database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///petclinic.db'  # Or another database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
