from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = '247bfbb3-8a6a-450d-94cc-27fcc5d736ee'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    is_uoft_email = True  # Set default value

    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        # Check if the email is a UofT email
        if not form.email.data.endswith('utoronto.ca'):
            is_uoft_email = False

        # Store data in session
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['is_uoft_email'] = is_uoft_email  # Store the flag in session

        return redirect(url_for('index'))

    # Retrieve the flag from the session (set default to True if not in session)
    is_uoft_email = session.get('is_uoft_email', True)

    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           email=session.get('email'),
                           currentTime=datetime.utcnow(),
                           is_uoft_email=is_uoft_email)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
