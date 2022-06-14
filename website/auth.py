from crypt import methods
from turtle import home
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("signup.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")