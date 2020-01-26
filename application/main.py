from flask import Flask, render_template, json

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organizer')
def organizer():
    return render_template('organizer/organizer.html')

@app.route('/donar')
def doner():
    return render_template('donar/donar.html')

@app.route('/children')
def children():
    return render_template('children/children.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

from application.APIs.children import children
from application.APIs.donar import donar
from application.APIs.organizer import organizer
