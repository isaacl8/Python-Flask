from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if(len(name) < 1):
        flash("Name cannot be empty!")
        return redirect('/')
    if(len(comment) < 1):
        flash("Comment cannot be empty!")
        return redirect('/')
    if(len(comment) > 120):
        flash("Comments can only be 120 characters.")
        return redirect('/')
    return render_template('result.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)
