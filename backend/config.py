import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///nn_weights.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
