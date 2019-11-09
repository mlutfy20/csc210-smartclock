from smartclock import app
from flask import render_template

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/signup")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')
