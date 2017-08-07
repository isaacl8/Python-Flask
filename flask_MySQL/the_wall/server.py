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

@app.route('/wall')
def wall():
    # this is the loop is to check if the messages went thru
    # also SELECT is pulling info from the database
    messages_string= "SELECT messages.id, users.first_name, user.last_name, messages.content, messages.created_at From messages JOIN users ON messages.user_id = user.id"

    all_messages = mysql.query_db(query_string,)
    for a_message in all messages:
        comments_query= "SELECT comments.content, users.first_name, users.last_name, comments.created_at FROM comments JOIN users ON comments.user_id = user.id WHERE comments.message_id = :msg_id"
        data = {
        'msg_id': a_message['id']
        }
        a_message['comments']= mysql.query_db(comments_query, data)
    return render_template('wall.html', messages=all_messages)

@app.route('/register', methods=['POST'])
def register():
    print request.form
    # check errors in login
    has_errors = False
    if len(request.form['first_name']) == 0:
        flash("First name cannot be blank")
        has_errors = True
    if len(request.form['last_name']) == 0:
        flash("Last name cannot be blank")
        has_errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not in valid format")
        has_errors = True
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long")
        has_errors = True
    if len(request.form['password'] != request.form['password_confirm'])  :
        flash("Password must be at least 8 characters long")
        has_errors = True

    if has_errors:
        return redirect('/')
    else:
        hash_password=md5.new(request.form['password']).hexdigest()
        print hashed_password
        # email verif to check if there are any other users
        query_string = "SELECT * FROM users WHERE email = :emale"
        data = {
        'emale': request.form['email']
        }
        found_user = my.sql.query_db(query_string, data)
        if found_user:
            flash("Email is already inside the database")
            return redirect('/')
        else:
        #puts info into database
            query_string = "INSERT INTO users (first_name, last_name, email, passsword) VALUES (:f_name, :l_name, :emale, :pw)"
            data = {
            "f_name": request.form ['first_name'],
            "l_name": request.form ['last_name'],
            "emale": request.form ['email'],
            "pw": hashed_password
            }
            created_user = mysql.query_db(query_string,data)
            print created_user
            #modify session
            session['user_id'] = created_user_id
            query_string = "SELECT * FROM users WHERE id = :my_id"
            data = {
            'my_id': created_user_id
            }
            found_user = my.sql.query_db(query_string, data)
            session['user_name'] = found_user['first_name']
            return redirect('/wall')

# login valid
@app.route('/login', methods=["POST"])
def login():
    query_string = "SELECT * FROM users WHERE email = :emale"
    data = {
    'emale': request.form['email']
    }
    found_users = my.sql.query_db(query_string, data)
    if found_users:
        found_user = found_users[0]
        input_password = md5.new(request.form['password']).hexdigest()
        if input_password == found_user['password']:
            session['user_name']= found_user['first_name']
            session['user_id'] = found_user['id']
            return redirect ('/wall')
    else:
        flash('Invalid Login')
        return redirect('/')
# message posting
@app.route('/messages', methods=['POST'])
def create_message():
    query_string= "INSERT INTO messages(content, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())"
    data = {
    "content":request.form["content"],
    "user_id":session['user_id']
    }
    mysql.query_db(query_string,data)
    return redirect('/wall')


@app.route('/comments', methods=['POST'])
def create_comment():
    query_string = "INSERT INTO comments (user_id, message_id, content, created_at, updated_at) VALUES (:user_id, :msg_id, :content, NOW(), NOW())"
    data = {
    "user_id": session['user_id']
    "msg_id": request.form['message_id']
    "content": request.form['content']
    }
    mysql.query_db(query_string,data)
    return redirect('/wall')

app.run(debug=True)
