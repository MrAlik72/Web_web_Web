from flask import Flask
from flask import render_template
from flask import redirect
from flask import abort
from random import randint

app = Flask(__name__)

users_list = [{'name': 'Albert', 'surname': 'Einstein', 'age': randint(10, 60)},
              {'name': 'Wolfgang', 'surname': 'Pauli', 'age': randint(10, 50)},
              {'name': 'Georg', 'surname': 'Riemann', 'age': randint(10, 50)}]


@app.route('/<users>')
def users(users):
    return render_template("users.html", users=users_list)


@app.route('/')
def hello_world():
    return redirect('/users')


@app.route('/user/<username>')
def user(username):
    for user in users_list:
        if user['surname'] == username:
            return render_template('user.html', username=user['surname'])
    abort(404)


app.run()
