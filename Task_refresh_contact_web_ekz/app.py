from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import psycopg2
#Апдейт пользователя -> создать страницу на кототрой можно обновить пользователь:
#страница заносим id пользователя и все новые данные-> после этого он refresh/
app = Flask(__name__)
db = psycopg2.connect(dbname="TelephoneKniga",
                        user="postgres",
                        password="Danilka123",
                        host="127.0.0.1",
                        port="5432")

@app.route('/')
def index():
    cur = db.cursor()
    cur.execute("select uid, last_name_val, first_name_val, middle_name_val, street_val,"
                "build, build_k, apartment, telephone "
                "from main "
                "join last_name on main.last_name = last_name_id "
                "join first_name on main.first_name = first_name_id "
                "join middle_name on main.middle_name = middle_name_id "
                "join street on main.street = street_id")
    users_list = cur.fetchall()
    return render_template('index.html', users_list=users_list)

@app.route('/contact/<uid>', methods=['GET'])
def get_contact(uid):
    cur = db.cursor()
    cur.execute("select uid, last_name_val, first_name_val, middle_name_val, street_val,"
                "build, build_k, apartment, telephone "
                "from main "
                "join last_name on main.last_name = last_name_id "
                "join first_name on main.first_name = first_name_id "
                "join middle_name on main.middle_name = middle_name_id "
                "join street on main.street = street_id "
                "where uid = %s", (uid,))
    contact = cur.fetchone()
    return render_template('contact.html', contact=contact)

@app.route('/contact/<uid>', methods=['POST'])
def update_contact(uid):
    cur = db.cursor()
    last_name = request.form['lname']
    first_name = request.form['fname']
    middle_name = request.form['mname']
    street = request.form['street']
    build = request.form['build']
    build_k = request.form['build_k']
    apartment = request.form['apartment']
    telephone = request.form['telephone']
    
    cur.execute("SELECT last_name_id FROM last_name WHERE last_name_val = %s", (last_name,))
    last_name_id = cur.fetchone()
    if last_name_id is None:
        cur.execute("INSERT INTO last_name (last_name_id, last_name_val) VALUES (default, %s)", (last_name,))
        cur.execute("SELECT last_name_id FROM last_name WHERE last_name_val = %s", (last_name,))
        last_name_id = cur.fetchone()
        last_name_id = last_name_id[0]
    else:
        last_name_id = last_name_id[0]

    cur.execute("SELECT first_name_id FROM first_name WHERE first_name_val = %s", (first_name,))
    first_name_id = cur.fetchone()
    if first_name_id is None:
        cur.execute("INSERT INTO first_name (first_name_val) VALUES (%s)", (first_name,))
        cur.execute("SELECT first_name_id FROM first_name WHERE first_name_val = %s", (first_name,))
        first_name_id = cur.fetchone()
        first_name_id = first_name_id[0]
    else:
        first_name_id = first_name_id[0]

    cur.execute("SELECT middle_name_id FROM middle_name WHERE middle_name_val = %s", (middle_name,))
    middle_name_id = cur.fetchone()
    if middle_name_id is None:
        cur.execute("INSERT INTO middle_name (middle_name_val) VALUES (%s)", (middle_name,))
        cur.execute("SELECT middle_name_id FROM middle_name WHERE middle_name_val = %s", (middle_name,))
        middle_name_id = cur.fetchone()
        middle_name_id = middle_name_id[0]
    else:
        middle_name_id = middle_name_id[0]

    cur.execute("SELECT street_id FROM street WHERE street_val = %s", (street,))
    street_id = cur.fetchone()
    if street_id is None:
        cur.execute("INSERT INTO street (street_val) VALUES (%s)", (street,))
        cur.execute("SELECT street_id FROM street WHERE street_val = %s", (street,))
        street_id = cur.fetchone()
        street_id = street_id[0]
    else:
        street_id = street_id[0]

    cur.execute("UPDATE main SET last_name = %s, first_name = %s, middle_name = %s, street = %s, build = %s, build_k = %s, apartment = %s, telephone = %s WHERE uid = %s",
                (last_name_id, first_name_id, middle_name_id, street_id, build, build_k, apartment, telephone, uid))
    db.commit()
    return redirect(url_for('index'))
    

@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    cur = db.cursor()
    last_name = request.form['lname']
    first_name = request.form['fname']
    middle_name = request.form['mname']
    street = request.form['street']
    build = request.form['build']
    build_k = request.form['build_k']
    apartment = request.form['apartment']
    telephone = request.form['telephone']

    cur.execute("SELECT last_name_id FROM last_name WHERE last_name_val = %s", (last_name,))
    last_name_id = cur.fetchone()
    if last_name_id is None:
        cur.execute("INSERT INTO last_name (last_name_id, last_name_val) VALUES (default, %s)", (last_name,))
        cur.execute("SELECT last_name_id FROM last_name WHERE last_name_val = %s", (last_name,))
        last_name_id = cur.fetchone()
        last_name_id = last_name_id[0]
    else:
        last_name_id = last_name_id[0]

    cur.execute("SELECT first_name_id FROM first_name WHERE first_name_val = %s", (first_name,))
    first_name_id = cur.fetchone()
    if first_name_id is None:
        cur.execute("INSERT INTO first_name (first_name_val) VALUES (%s)", (first_name,))
        cur.execute("SELECT first_name_id FROM first_name WHERE first_name_val = %s", (first_name,))
        first_name_id = cur.fetchone()
        first_name_id = first_name_id[0]
    else:
        first_name_id = first_name_id[0]

    cur.execute("SELECT middle_name_id FROM middle_name WHERE middle_name_val = %s", (middle_name,))
    middle_name_id = cur.fetchone()
    if middle_name_id is None:
        cur.execute("INSERT INTO middle_name (middle_name_val) VALUES (%s)", (middle_name,))
        cur.execute("SELECT middle_name_id FROM middle_name WHERE middle_name_val = %s", (middle_name,))
        middle_name_id = cur.fetchone()
        middle_name_id = middle_name_id[0]
    else:
        middle_name_id = middle_name_id[0]

    cur.execute("SELECT street_id FROM street WHERE street_val = %s", (street,))
    street_id = cur.fetchone()
    if street_id is None:
        cur.execute("INSERT INTO street (street_val) VALUES (%s)", (street,))
        cur.execute("SELECT street_id FROM street WHERE street_val = %s", (street,))
        street_id = cur.fetchone()
        street_id = street_id[0]
    else:
        street_id = street_id[0]

    cur.execute(
        "INSERT INTO main (uid, last_name, first_name, middle_name, street, build, build_k, apartment, telephone)"
        " VALUES (default, %s, %s, %s, %s, %s, %s, %s, %s)",
        (last_name_id, first_name_id, middle_name_id, street_id, build, build_k, apartment, telephone))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<string:uid>', methods=['POST', 'GET'])
def delete_student(uid):
    cur = db.cursor()
    cur.execute("DELETE FROM main WHERE u_id = %s", (uid,))
    db.commit()
    return redirect(url_for('index'))

app.run(port=5005)
