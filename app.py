from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    student_data = query1()
    return render_template('home.html', student_data = student_data)

@app.route('/add', methods = ['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        student_details = (
            request.form['firstname'],
            request.form['surname'],
            request.form['address'],
            request.form['suburb']
        )
        insert_student(student_details)
        return render_template('add-sucess.html')

def insert_student(student_details):
    db_locale = 'student.db'
    con = sqlite3.connect(db_locale)
    c = con.cursor()
    query2 = 'insert into contact_details (firstname, surname, address, suburb)  values (?, ?, ?, ?)'
    c.execute(query2, student_details)
    con.commit()
    con.close()

def query1():
    db_locale = 'student.db'
    con = sqlite3.connect(
        db_locale)
    c = con.cursor()

    c.execute('select * from contact_details')

    student = c.fetchall()
    return student

if __name__=='__main__':
    app.run()

