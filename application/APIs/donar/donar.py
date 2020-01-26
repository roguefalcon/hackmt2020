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



@main.app.route('/api/1.0/donar/<id>', methods=['put'])
def donar_edit(id):

    donarData = request.json

#donar input
    email = donarData['email']
    username = donarData['username']
    password = donarData['password']
    phone = donarData['phone']
    name = donarData['name']

    g.c.execute('''UPDATE donor set email=?,username=?,password=?,phone=?,name=? where id=?''', (email,username,password,phone,name,id))

    g.conn.commit()
    return jsonify({'success': True, 'donar_id': id})


# Delete Single CHILD REECORD (Delete) ============================================

@main.app.route('/api/1.0/donar/<id>', methods=['DELETE'])
def donar_delete(id):
    # DELETE A REC FROM DB
    g.c.execute(''' DELETE FROM donor
                    WHERE id=? LIMIT 1''', id)
    g.conn.commit()

    #Tell the user it worked
    return jsonify({'success': True})
