from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    for friend in friends:
        print['name']
    print friends
    return render_template('index.html', my_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    nameList = request.form['name'].split(' ')
    query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    data = {
             'first_name': nameList[0],
             'last_name':nameList[1],
             'age': request.form['age']
           }

    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
