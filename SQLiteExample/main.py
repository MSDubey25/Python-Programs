from flask import Flask, render_template, request, flash, url_for, redirect
import sqlite3 as sql
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'Random String'
db = SQLAlchemy(app)

class students(db.Model):

    # id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True)
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.addr = addr
        self.city = city
        self.pin = pin

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    msg = ''
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            add = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?, ?, ?, ?)", (nm, add, city, pin))
                con.commit()
                msg = "Record Successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            con.close()
            return render_template('result.html', msg=msg)


@app.route('/list_result')
def list_result():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


# for sqlAlchemy

@app.route('/alchemy_home')
def show_all():
    return render_template('show_all.html', students=students.query.all())


@app.route('/new', methods=['POST','GET'])
def new():
    if request.method == 'POST':
        flash("Please Enter all the fields", "error")
    else:
        student = students(request.form['nm'],
                           request.form['city'],
                           request.form['addr'],
                           request.form['pin'])
        db.session.add(student)
        db.session.commit()
        flash("Record was added successfully by SQLAlchemy method")
        return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
