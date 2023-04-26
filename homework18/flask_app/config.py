import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DEBUG = os.getenv('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')