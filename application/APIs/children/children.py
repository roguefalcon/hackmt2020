from flask import Flask, render_template, json, request, g
from application import main

@main.app.route('/api/1.0/children/<id>', methods=['GET'])
def child_read(id):

    # Return the all columns for this child
    g.c.execute('''
    SELECT * FROM children
    WHERE id = ? ''',(id))
    data = g.c.fetchone()

    #return in Json format
    return jsonify(data)
# Update Single child record(Edit)======

@main.app.route('/api/1.0/childern/<id>', methods=['PUT'])
def child_edit(id):

    #child input
    email = request.form.get('email')
    age = request.form.get('age')
    name = request.form.get('name')
    about_me = request.form.get('about_me')
    adress = request.form.get('adress')
    cloth_size = request.form.get('cloth_size')
    sex = request.form.get('sex')
    gender = request.form.get('gender')
    pant_size = request.form.get('pant_size')
    shoes_size = request.form.get('shoes_size')
    fav_color = request.form.get('fav_color')


   """ if not email or not age or not name or not about_me
    or not adress or not cloth_size or not sex or not gender
    or not pant_size, or not shoes_size, or not fav_color:
        return jsonify({'success': False, 'error': 
        'Missing value'}) """
    # Update the child in the database
    g.c.execute('''
    UPDATE children set email=?, age=?, name=?, about_me=?
    adress=?, cloth_size=?, sex=?, gender=?,pant_size,
    shoes_size=?, fav_color=? WHERE child_id=?''', (
        email,age,name,about_me, adress, cloth_size, sex,
        gender, pant_size, shoes_size, fav_color, id
    )
    g.conn.commit()
    return jsonify({'success': True,  'child_id': id})


#Insert Single child record
@main.app.route('/api/1.0/childern', methods=['post'])
def child_edit():

    #child input
    email = request.form.get('email')
    age = request.form.get('age')
    name = request.form.get('name')
    about_me = request.form.get('about_me')
    adress = request.form.get('adress')
    cloth_size = request.form.get('cloth_size')
    sex = request.form.get('sex')
    gender = request.form.get('gender')
    pant_size = request.form.get('pant_size')
    shoes_size = request.form.get('shoes_size')
    fav_color = request.form.get('fav_color')

    #validation
   """ if not email or not age or not name or not about_me
    or not adress or not cloth_size or not sex or not gender
    or not pant_size, or not shoes_size, or not fav_color:
        return jsonify({'success': False, 'error': 
        'Missing value'}) """

    # Insert the child in the database
    g.c.execute('''
    INSERT INTO children 
        (email,age,name,about_me, adress, cloth_size, sex,
        gender, pant_size, shoes_size, fav_color)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
    (email,age,name,about_me, adress, cloth_size, sex,
        gender, pant_size, shoes_size, fav_color
    )
        g.conn.commit()
    # GET THE ID OF THE RECORD JUST CREATED
    rowid = g.c.lastrowid
    return jsonify({'success': True,  'child_id': id})


    # Delete Single CHILD REECORD (Delete) ============================================
@app.route('/api/1.0/children/<id>', methods=['DELETE'])
def destination_delete(id):

    # DELETE A REC FROM DB
    g.c.execute(''' DELETE FROM CHILDREN
                    WHERE id=? LIMIT 1''', id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})