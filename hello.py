from flask import Flask, request, make_response, redirect, abort, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/user_agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', first_name=name)

@app.route('/badbadbad')
def bad():
    return '<h1>Bad Bad Request</h1>', 400

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirectme')
def redirectme():
    return redirect('http://janmilosh.com')

if __name__ == '__main__':
    manager.run()
