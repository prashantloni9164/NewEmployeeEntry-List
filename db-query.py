import sqlite3
db_locale = 'student.db'
con=sqlite3.connect(db_locale)
c=con.cursor()

c.execute('''
select * from contact_details
''')

student=c.fetchall()

for student in student:
    print(student)

con.commit()
con.close()