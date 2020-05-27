class InvalidField(Exception):
    pass

class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class Student:
    
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
        
    @staticmethod    
    def get(student_id=0,name="",age=0,score=-1,**kwargs):
        if student_id!=0:
            query=f"select * from student where student_id = {student_id}"
            record=read_data(query)
        elif name!="":
            query=f"select * from student where name = '{name}'"
            record=read_data(query)
        elif age!=0:
            query=f"select * from student where age = {age}"
            record=read_data(query)
        elif score!=-1:
            query=f"select * from student where score = {score}"
            record=read_data(query)
        else:
            raise InvalidField
        
        if len(record)==0:
            raise DoesNotExist
        elif len(record)>1:
            raise MultipleObjectsReturned
        else:
            result=Student(record[0][1],record[0][2],record[0][3])
            result.student_id=record[0][0]
            return result
            
    def save(self):
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;")
        if self.student_id==None:
            record="insert into student(name,age,score)values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(record)
            self.student_id=crsr.lastrowid
        
        elif("select {} from student where student_id not in (select student_id from student)".format(self.student_id)):
            record="""replace into student(student_id,name,age,score) values({},'{}',{},{})""".format(self.student_id,self.name,self.age,self.score)
            crsr.execute(record)
            self.student_id=crsr.lastrowid
        
        else:
            record="Update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.student_id)
            crsr.execute(record)
        
        connection.commit() 
        connection.close()
            
    def delete(self):
        record=f'delete from student where student_id={self.student_id}'
        write_data(record)
    
    
    
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit() 
    connection.close()
    	
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans
'''
s1=Student('vidya',21,95)
s1.save()
s=Student.get(student_id=22)
s.student_id=26
s.save()
print(read_data("select * from student"))'''


