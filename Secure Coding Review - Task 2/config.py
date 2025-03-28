import os

class Config:
    SECRET_KEY = '12345'  # Change this to a random secret
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
