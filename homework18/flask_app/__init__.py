from flask import Flask
from .config import AppConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(AppConfig)
db.init_app(app)

from .views import *
from .class_based_views import *
from .models import *

with app.app_context():
    db.create_all()