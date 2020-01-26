from flask import Flask, render_template, json, request, g, jsonify
from application import main

@main.app.route('/api/1.0/children', methods=['GET'])
def child_browse():

    # Return the all columns for this child
    g.c.execute('''
    SELECT id, name, age, sex FROM children 

     ''')
    data = g.c.fetchall()
    return jsonify(data)

@main.app.route('/api/1.0/children/<id>', methods=['GET'])
def child_read(id):

    # Return the all columns for this child
    g.c.execute('''
    SELECT * FROM children
    WHERE id = ? ''',(id))
    data = g.c.fetchone()

    g.c.execute('''
    SELECT id, name, amount FROM children_items
    WHERE children_id = ? ''',(id))
    items = g.c.fetchall()
    print(items)
    data["items"] = items
    print(data)
    
    #return in Json format
    return jsonify(data)
# Update Single child record(Edit)======

@main.app.route('/api/1.0/children/<id>', methods=['put'])
def child_edit(id):

    childrenData = request.json

    #child input
    email = childrenData['email']
    age = childrenData['age']
    name = childrenData['name']
    about_me = childrenData['about_me']
    address = childrenData['address']
    cloth_size = childrenData['cloth_size']
    sex = childrenData['sex']
    gender = childrenData['gender']
    pant_size = childrenData['pant_size']
    shoes_size = childrenData['shoes_size']
    fav_color = childrenData['fav_color']
    items = childrenData['items']
    '''if not email or not name or not name or not about_me
    or not adress or not cloth_size or not sex or not gender
    or not pant_size, or not shoes_size, or not fav_color:
        return jsonify({'success': False, 'error': 
        'Missing value'}) '''
    # Update the child in the database
    g.c.execute('''
    UPDATE children set email=?, name=?, age=?, about_me=?,
    address=?, cloth_size=?, sex=?, gender=?,pant_size=?,
    shoes_size=?, fav_color=? WHERE id=?''', (
        email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color, id
    ))
    g.conn.commit()

    for item in items:
        g.c.execute('''
        UPDATE children_items set name=?
        WHERE id = ?''',(item['name'], item['id'])
        )
        g.conn.commit()

    return jsonify({'success': True,  'child_id': id})


#Insert Single child record
@main.app.route('/api/1.0/children', methods=['post'])
def child_insert():

    childrenData = request.json
    #child input
    email = childrenData['email']
    age = childrenData['age']
    name = childrenData['name']
    about_me = childrenData['about_me']
    address = childrenData['address']
    cloth_size = childrenData['cloth_size']
    sex = childrenData['sex']
    gender = childrenData['gender']
    pant_size = childrenData['pant_size']
    shoes_size = childrenData['shoes_size']
    fav_color = childrenData['fav_color']
    items =  childrenData['items']

    #validation
    """if not email or not age or not name or not about_me
    or not address or not cloth_size or not sex or not gender
    or not pant_size, or not shoes_size, or not fav_color:
        return jsonify({'success': False, 'error': 
        'Missing value'}) """

    # Insert the child in the database
    g.c.execute('''
    INSERT INTO children 
        (email,name, age, about_me, address, cloth_size, sex,
        gender, pant_size, shoes_size, fav_color)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
    (email,name,age,about_me, address, cloth_size, sex,
        gender, pant_size, shoes_size, fav_color
    ))
    # GET THE ID OF THE RECORD JUST CREATED
    rowid = g.c.lastrowid

    for item in items:
        g.c.execute('''
        INSERT INTO children_items
        (name , amount, children_id) 
        VALUES (?,?,?)''',
        (item["name"], None, rowid)
    )
    g.conn.commit()
    return jsonify({'success': True,  'child_id': rowid})


    # Delete Single CHILD REECORD (Delete) ============================================

@main.app.route('/api/1.0/children/<id>', methods=['DELETE'])
def destination_delete(id):

    # DELETE A REC FROM DB
    g.c.execute(''' DELETE FROM CHILDREN
                    WHERE id=? LIMIT 1''', id)
    g.conn.commit()

    g.c.execute(''' DELETE FROM children_items
                    WHERE children_id=?''', id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
