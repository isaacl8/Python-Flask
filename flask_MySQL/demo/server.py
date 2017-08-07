from flask import Flask,render_template,request,redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'twitter')

@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    for user in users:
        #print user['first_name']
        return render_template('index.html', all_users = users)

@app.route('/create_user', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    handle = request.form['handle']

    query = "INSERT INTO users (first_name, last_name, handle) VALUES(:f_name, :l_name, :handle) "
    data = {
        "f_name": first_name,
        "l_name": last_name,
        "handle": handle
    }

    mysql.query_db(query,data)

    return redirect('/')

app.run(debug=True)
