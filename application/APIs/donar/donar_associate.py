from flask import Flask, render_template, json, request, g, jsonify
from application import main

@main.app.route('/donars/<donar_id>/children/<children_id>', methods=['POST'])
def LinkDonarToChild(donar_id, children_id):

    # Return the all columns for this child
    g.c.execute('''
    INSERT INTO donar_sponsor_children (donar_id, children_id) VALUES (?,?)

     ''', (donar_id, children_id))
    g.conn.commit()
    
    new_id = g.c.lastrowid
    
    return jsonify({'success': True,  'donar_sponsor_children_id': new_id})