from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninjas')
def ninja():
    return render_template('ninjas.html')


@app.route('/ninjas/<color>')
def ninja_color(color):
    print color
    if color == 'purple':
        color = 'img/donatello.jpg'
    elif color == 'red':
        color = 'img/raphael.jpg'
    elif color == 'blue':
        color = 'img/leonardo.jpg'
    elif color == 'orange':
        color = 'img/michelangelo.jpg'
    else:
        color = 'img/notapril.jpg'
    return render_template('colors.html', src=color)


app.run(debug='True')
