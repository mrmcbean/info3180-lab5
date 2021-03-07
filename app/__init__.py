from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost/database"


db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(Config)
from app import views
