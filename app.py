"""
starts a Flask web application
"""

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '972c87379d16a8a27665666e1cf17a35c44d39d4feddceda9d600c4d8b304436'

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
	return render_template('login.html', title="Login", form=form)


if __name__ == "__main__":
	app.run(debug=True)