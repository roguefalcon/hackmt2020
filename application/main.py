from flask import Flask, render_template, json

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organization')
def organization():
    return render_template('organization/organization.html')

@app.route('/donar')
def doner():
    return render_template('donar/donar.html')

@app.route('/welcome_child')
def welcome():
    return render_template('children/welcome.html')

@app.route('/donar/<id>/children')
def doner_children(id):
    return render_template('donar/childrenPhoto.html')

@app.route('/children')
def children():
    return render_template('children/children.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

from application.APIs.children import children
from application.APIs.donar import donar
from application.APIs.organization import organization
