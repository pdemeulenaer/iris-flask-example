from app import app
from flask import Flask, request, jsonify, render_template

# @app.route("/")
# def index():
#     return "Hello world"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return "All about Flask"
