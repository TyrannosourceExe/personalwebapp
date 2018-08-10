from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# secret key to protect against cross site forgery attacks
app.config['SECRET_KEY'] = '193d0f87084aa73c395f89fb8a31c30c'

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
