from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'hello_world'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def result():
    email = request.form['email']
    fname = request.form['fname']
    lname = request.form['lname']
    password = request.form['password']
    cpword = request.form['cpword']
    if (len(email) < 1):
        flash('Email cannot be empty', 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
    if not NAME_REGEX.match(request.form['fname']) or not NAME_REGEX.match(request.form['lname']):
        flash('First and last name must only include letters.', 'error')
    # else:
    #     flash("Success!")
    if (len(fname) < 1):
        flash('First name cannot be empty!', 'error')
    if(len(lname) < 1):
        flash('Last name cannot be empty!', 'error')
    if(len(password) < 8):
        flash('Password is too short!', 'error')
    if request.form['password'] != request.form['cpword']:
        flash('Confirm password must match password.', 'error')
    # else:
    #     flash('You have successfully logged in!', 'success')
    if '_flashes' in session:
        return redirect('/')
    else:
        flash('Thanks for submitting your information.', 'success')
        return redirect('/')
    return redirect('/')


app.run(debug=True)
