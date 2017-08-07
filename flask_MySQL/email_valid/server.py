from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)

app.secret_key = 'Thisiscool'

mysql = MySQLConnector(app,'the_wall')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def loginreg():
    return render_template('index.html')
