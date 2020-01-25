from flask import Flask, render_template, json
from application import main

@main.app.route('/test')
def test():
    my_dict = {"name" : "Rocky", "gener" : "M"}
    return json.dumps(my_dict)