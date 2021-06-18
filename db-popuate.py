import sqlite3
db_locale = 'student.db'
con=sqlite3.connect(db_locale)
c=con.cursor()

c.execute('''
insert into contact_details (firstname, surname, address, suburb) values
('David', 'deefe', 'dededefrfrrg', 'fefrfefe'),
('johny', 'mode', '45frfrf' , 'ujjfrfr')
''')

con.commit()
con.close()