from flask import Flask, render_template
import sqlite3

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    student_data = query1()
    return render_template('home.html', student_data = student_data)

@app.route('/add', methods = ['GET', 'POST'])
def add_student():
    if request.method
    return render_template('add_student.html')

def query1():
    db_locale = 'student.db'
    con = sqlite3.connect(db_locale)
    c = con.cursor()

    c.execute('''
    select * from contact_details
    ''')

    student = c.fetchall()
    return student

if __name__=='__main__':
    app.run()

