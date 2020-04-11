from flask import Flask, jsonify, render_template
import aws_controller
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from flask_bootstrap import Bootstrap
# ...



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
    
    return "This is the main page.<br> <a href='/get-items'> get items</a> "
    
@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_item('gaming_nationals_zaf'))

@app.route('/do_items')
def do_items(tableName):
    response=aws_controller.create_table(tableName)
    return response

@app.route('/get_all')
def get_all():
    response=aws_controller.get_all()
    return response


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run()