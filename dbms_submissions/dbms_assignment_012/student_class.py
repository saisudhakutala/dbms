'''import sqlite3

conn=sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""Create table Students
             (student_id integer primary key,
             name text,
             age integer,
             score integer)
             """)
c.execute("""
          insert into students 
          values(1,'sai sudha',21,100)
          """)
c.execute('select * from students')
print(c.fetchall())
conn.commit()
conn.close()
'''
