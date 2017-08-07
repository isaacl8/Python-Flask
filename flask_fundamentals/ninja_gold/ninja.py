import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ninja_game'


@app.route('/')
def index():
    if 'my_coins' not in session:
        session['my_coins'] = 0
        # print session['coin']
    if 'activity_log' not in session:
        session['activity_log'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process():
    if request.form['action'] == 'farm':
        farm_add = random.randrange(10, 21)
        session['my_coins'] += farm_add
        log = 'You have earned ' + \
            str(farm_add) + ' gold coins.' + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(log)

    elif request.form['action'] == 'cave':
        farm_add = random.randrange(5, 11)
        session['my_coins'] += farm_add
        log = 'You have earned ' + str(farm_add) + ' gold coins.' + \
            str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(log)

    elif request.form['action'] == 'house':
        farm_add = random.randrange(2, 6)
        session['my_coins'] += farm_add
        log = 'You have earned ' + str(farm_add) + ' gold coins.' + \
            str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(log)

    elif request.form['action'] == 'casino':
        chance = random.randrange(1, 3)
        if chance == 1:
            farm_add = random.randrange(1, 51)
            session['my_coins'] += farm_add
            log = 'You have earned ' + str(farm_add) + ' gold coins.' + \
                str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            session['activity_log'].append(log)
        elif chance == 2:
            farm_add = random.randrange(1, 51)
            session['my_coins'] -= farm_add
            log = 'You have lost ' + str(farm_add) + ' gold coins.' + \
                str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            session['activity_log'].append(log)

    return redirect('/')


app.run(debug=True)
