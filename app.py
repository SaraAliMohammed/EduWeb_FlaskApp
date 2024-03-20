"""
starts a Flask web application
"""

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '972c87379d16a8a27665666e1cf17a35c44d39d4feddceda9d600c4d8b304436'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduweb.db'
db = SQLAlchemy(app)
lessons = [{
    'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
]

courses = [
{
        'name': 'Python',
        'icon': 'python.svg',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Data Analysis',
        'icon': 'analysis.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Machine Learning',
        'icon': 'machine-learning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Web Design',
        'icon': 'web.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Blockchain',
        'icon': 'blockchain.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Tips & Tricks',
        'icon': 'idea.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', lessons=lessons, courses=courses)


@app.route("/about")
def about():
	return render_template('about.html', title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account created successfully for {form.username.data}", "success")
		return redirect(url_for("home"))
	return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if (
            form.email.data == "sara@gmail.com"
            and form.password.data == "P@ssw0rd"
        ):
			flash("You have been logged in!", "success")
			return redirect(url_for("home"))
		else:
			flash("Login Unsuccessful. Please check credentials", "danger")
	return render_template('login.html', title="Login", form=form)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(25), nullable=False)
	lname = db.Column(db.String(25), nullable=False)
	username = db.Column(db.String(25), nullable=False, unique=True)
	email = db.Column(db.String(125), nullable=False, unique=True)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	lessons = db.relationship("Lesson", backref='author', lazy=True)

	def __repr__(self):
		return f"USER('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"


class Lesson(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	thumbnail = db.Column(db.String(20), nullable=False, default='default_thumbnail.jpg')
	slug = db.Column(db.String(32), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

	def __repr__(self):
		return f"LESSON('{self.title}', '{self.date_posted}')"


class Course(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False, unique=True)
	description = db.Column(db.String(150), nullable=False)
	icon = db.Column(db.String(20), nullable=False, default='default_icon.jpg')
	lessons = db.relationship("Lesson", backref='course_name', lazy=True)

	def __repr__(self):
		return f"COURSE('{self.title}')"


if __name__ == "__main__":
	app.run(debug=True)