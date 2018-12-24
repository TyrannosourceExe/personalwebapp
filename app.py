# https://youtu.be/cYWiDiIUxQc?t=1056

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

#global objects
usr_char_limit = 20
email_char_limit = 120
picture_hash_limit = 20
password_hash_limit = 60
post_title_limit = 100

#webapp
app = Flask(__name__)
# secret key to protect against cross site forgery attacks
app.config['SECRET_KEY'] = '193d0f87084aa73c395f89fb8a31c30c'
# database setup using SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'squlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(usr_char_limit), unique=True, nullable=False)
	email = db.Column(db.String(email_char_limit), unique=True, nullable=False)
	profile_pic = db.Column(db.String(picture_hash_limit), nullable=False, default='default.jpg')
	password = db.Column(db.string(password_hash_limit), nullable=False)
	# one to many query of author to post class, backreference allows post to go to author attribute
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	# user.id is lowercase because it is linked to tablename
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}')"

# mock posts created
posts = [
	{
		'author': 'Terry Thurk',
		'title': 'For the Sake of New Experiences',
		'content': '“How many of you have wanted to travel across America?” ' 
		'The audience raised their hands unanimously in response to the speaker question. '
		'The brown bearded man took time to acknowledge the audience’s enthusiastic response before continuing.'
		'“So I asked, why not me? And simply went about to do it." '
		'Why not indeed.  Standing in front of me was a middle aged man wearing a tie-die shirt,'
		' playing a flute, talking to an audience of software engineers about treating battery voltages'
		' as compatibility layers in programming. He had sprung from a background in political science major,'
		' yet managed not only to master himself as a software consultant, '
		'but also traveled across the United States while doing so. The bearded consultant left in a school bus'
		' he built himself, with a small server energized by solar panels, batteries, and its power governed by'
		' algorithms running on a thirty five dollar Raspberry Py. '
		'(Much like the Py this website is hosted on) '
		'It was him who reminded me just how short life is,'
		' how important it was to always learn new skill-sets, and how important it was to challenge my assumptions'
		' and continue to explore.',
		'date_posted': 'July 17, 2018'
	},
	{
		'author': 'TyrannosourceExe',
		'title': 'Test Post',
		'content': 'My commencement speech can be found at https://www.youtube.com/watch?v=K8El16a_Z4g',
		'date_posted': 'April 21, 2018'
	}
]

@app.route('/')
def home():
    return render_template('under_dev.html')

@app.route('/blog')
def blog():
	return render_template('blog.html', title='Blog', posts=posts)

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
