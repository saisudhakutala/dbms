class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
class Student:
    
    def __init__(self,name,age,score):
        
        self.student_id=None
        self.name=name
        self.age=age
        self.score=score
    
    @staticmethod
    def get(student_id=0,name="",age=0,score=-1,**kwargs):
        if type(student_id)==int and student_id!=0:
            record=read_data("select * from Student where student_id={}".format(student_id))
        elif type(name)==str and name!="":
            record=read_data("select * from Student where name='{}'".format(name))
        elif type(age)==int and age!=0:
            record=read_data("select * from Student where age={}".format(age))
        elif type(score)==int and score!=-1:
            record=read_data("select * from Student where score={}".format(score))
        else:
            raise InvalidField
        
        if len(record)==0:
            raise DoesNotExist
        
        elif len(record)==1:
            output=Student(record[0][1],record[0][2],record[0][3])
            output.student_id=record[0][0]
            return output
        else:
            raise MultipleObjectsReturned
            
    def save(self):
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
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
        
    @classmethod
    def filter(cls,**kwargs):
        fields_list=['student_id','name','age','score']
        for key,value in kwargs.items():
            k=key
            v=value
            field=k.split("__")
            #print(field)
            if (field[0] not in fields_list):
                raise InvalidField
            elif k in fields_list:
                if field[0]!='name':
                    query=(f"select * from student where {k}={v}")
                else:
                    query=(f"select * from student where {field[0]} = '{v}'")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='lt':
                query=(f"select * from student where {field[0]} < {v}")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='lte':
                query=(f"select * from student where {field[0]} <= {v}")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='gt':
                query=(f"select * from student where {field[0]} > {v}")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='gte':
                query=(f"select * from student where {field[0]} >= {v}")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='neq':
                if field[0]!='name':
                    query=(f"select * from student where {field[0]} != {v}")
                else:
                    query=(f"select * from student where {field[0]} != '{v}'")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='in':
                query=(f"select * from student where {field[0]} in {tuple(v)}")
                record=read_data(query)
            elif field[0] in fields_list and field[1]=='contains':
                query=(f"select * from student where {field[0]} like '%{v}%'")
                record=read_data(query)
            
            records_list=[]
        
            if len(record)>0:
                for i in record:
                    res=Student(i[1],i[2],i[3])
                    res.student_id=i[0]
                    records_list.append(res)
                
            else:
                return records_list
                
        return records_list
            
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(self.student_id,self.name,self.age,self.score)
    
    
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit() 
    connection.close()
    	
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans

'''s1=Student(name="sid",age=20,score=95)
s1.save()
s1=Student(name="ram",age=19,score=98)
s1.save()
ages=[20,22]
selected_students = Student.filter(age__in=ages)
print(selected_students)
#print(read_data("select * from student"))
'''