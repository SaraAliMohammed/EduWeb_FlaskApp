"""
Holds eduWeb Classes	
"""
from datetime import datetime
from eduWeb import db, login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
	'''Loads the user with specific id'''
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	"""Representation of User Class """
	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(25), nullable=False)
	lname = db.Column(db.String(25), nullable=False)
	username = db.Column(db.String(25), nullable=False, unique=True)
	email = db.Column(db.String(125), nullable=False, unique=True)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	bio = db.Column(db.Text, nullable=True)
	lessons = db.relationship("Lesson", backref='author', lazy=True)
	# courses = db.relationship("Course", backref="author", lazy=True)

	def __init__(self, **kwargs):
		''' Intialization method'''
		for key, value in kwargs.items():
			setattr(self, key, value)


	def get_reset_token(self):
		'''Gets a reset token'''
		s = Serializer(current_app.config['SECRET_KEY'], salt='pw-reset')
		return s.dumps({'user_id': self.id})

	
	@staticmethod
	def verify_reset_token(token, age=3600):
		'''Verifies the reset token'''
		s = Serializer(current_app.config['SECRET_KEY'], salt='pw-reset')
		try:
			user_id = s.loads(token, max_age=age)['user_id']
		except Exception:
			return None
		return User.query.get(user_id)


	def __repr__(self):
		'''String representation of User object'''
		return f"USER('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"


class Lesson(db.Model):
	"""Representation of Lesson Class """
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	thumbnail = db.Column(db.String(20), nullable=False, default='default_thumbnail.jpg')
	slug = db.Column(db.String(32), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

	def __init__(self, **kwargs):
		''' Intialization method'''
		for key, value in kwargs.items():
			setattr(self, key, value)

	def __repr__(self):
		'''String representation of Lesson object'''
		return f"LESSON('{self.title}', '{self.date_posted}')"


class Course(db.Model):
	"""Representation of Course Class """
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), unique=True, nullable=False)
	description = db.Column(db.String(150), nullable=False)
	icon = db.Column(db.String(20), nullable=False, default="default_icon.jpg")
	# user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	lessons = db.relationship("Lesson", backref="course_name", lazy=True)

	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

	def __repr__(self):
		"""String representation of Course object"""
		return f"COURSE('{self.title}')"