from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)


@app.route('/login')
def show_login_form():
    return render_template('login_form.template.html')

@app.route('/calculate')
def show_calculate_form():
    return render_template('calculate.template.html')

# this route process is to allow a post request to the /login url


@app.route('/login', methods=['POST'])
def process_login_form():
    print('data received')
    print(request.form)  # to retrieve information from html
    username = request.form.get("username")
    password = request.form.get("password")
    print("Username is {} and password is {}".format(username,password))
    return 'data received'  # MUST ALWAYS PROVIDES A RETURN STATEMENT

@app.route('/calculate', methods=['POST'])
def process_calculate():
    print('data received')
    print(request.form)  # to retrieve information from html
    input1 = request.form.get("input1")
    input2 = request.form.get("input2")
    totalsum = int(input1)+int(input2)
    print("Total sum is {}".format(totalsum))
    return render_template('calculate.template.html',totalsum=totalsum)



if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
