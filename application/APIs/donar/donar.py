from flask import Flask, render_template, json, request, g, jsonify
from application import main

@main.app.route('/api/1.0/donar/<id>', methods=['GET'])
def donar_read(id):

    #Return all columns for this child
    g.c.execute('''SELECT * FROM donor WHERE id = ?''',(id))
    data = g.c.fetchone()

    #return in Json format
    return jsonify(data)

#Insert single donor record
@main.app.route('/api/1.0/donar', methods=['post'])
def donar_insert():

    donarData = request.json
    #donar input
    email = donarData['email']
    username = donarData['username']
    password = donarData['password']
    phone = donarData['phone']
    name = donarData['name']

    g.c.execute('''INSERT INTO donor (email, username, password, phone, name) VALUES (?, ?, ?, ?, ?)''',(email, username, password, phone, name))

    rowid = g.c.lastrowid

    g.conn.commit()
    return jsonify({'success': True, 'donar_id':rowid})
