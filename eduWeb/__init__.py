"""
initialize the eduWeb package
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
from flask_mail import Mail
from eduWeb.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
ckeditor = CKEditor()
modal = Modal()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


def create_app(config_calss=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	migrate.init_app(app, db)
	login_manager.init_app(app)
	ckeditor.init_app(app)
	modal.init_app(app)
	mail.init_app(app)

	from eduWeb.main.routes import main
	from eduWeb.users.routes import users
	from eduWeb.lessons.routes import lessons
	from eduWeb.courses.routes import courses_bp

	app.register_blueprint(main)
	app.register_blueprint(users)
	app.register_blueprint(lessons)
	app.register_blueprint(courses_bp)

	return app
