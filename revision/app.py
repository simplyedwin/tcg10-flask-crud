from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/about-us')
def about():
    return '<h1>about-us<h1>'


@app.route('/lucky')
def luckyno():
    num = random.randint(1000, 9999)
    return 'Your lucky number is {}'.format(num)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
    # app.run(host='localhost', port=8080, debug=True)
