import sqlite3
db_locale = 'student.db'
con=sqlite3.connect(db_locale)
c=con.cursor()

c.execute('''
create table contact_details
(id integer primary key,
firstname text,
surname text,
address text,
suburb text)
''')

con.commit()
con.close()


