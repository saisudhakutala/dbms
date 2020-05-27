class InvalidField(Exception):
    pass

class Student:
    
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        self.student_id=None
    
    @staticmethod
    def filter(**kwargs):
        li=[]
        field_list=['student_id','name','age','score']
        operations={'gt':'>','lt':'<','lte':'<=','gte':'>=','neq':'!='}
        for k,v in kwargs.items():
            key=k.split("__")
            
            if key[0] not in field_list:
                raise InvalidField
                
            if k in field_list:
                if k !='name':
                    query=f'{k}={v}'
                else:
                    query=f'{k}="{v}"'
            elif key[1] in operations:
                query=f'{key[0]}{operations[key[1]]}{v}'
            elif key[1]=='in':
                query=f'{key[0]} in {tuple(v)}'
            elif key[1]=='contains':
                query=f'{key[0]} like "%{v}%"'
            li.append(query)
        return " and ".join(li)
    
    @classmethod
    def avg(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        elif len(kwargs.items())==0:
            query=f'select avg({field}) from student'
            
        else:
            f=Student.filter(**kwargs)
            query=f'select avg({field}) from student where {f}'
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def sum(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        elif len(kwargs)==0:
            query=f'select sum({field}) from student'
            
        else:
            f=Student.filter(**kwargs)
            query=f'select sum({field}) from student where {f}'
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def min(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
        elif len(kwargs)==0:
            query=f'select min({field}) from student'
            
        else:
            f=Student.filter(**kwargs)
            query=f'select min({field}) from student where {f}'
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def max(cls,field,**kwargs):
        field_list=['student_id','name','age','score']
        if field not in field_list:
            raise InvalidField
            
        elif len(kwargs)==0:
            query=f'select max({field}) from student'
            
        elif len(kwargs)>=1:
            f=Student.filter(**kwargs)
            query=f'select max({field}) from student where {f}'
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def count(cls,field=None,**kwargs):
        field_list=['student_id','name','age','score']
        if field==None:
            query=f'select count(*) from student'
            
        elif field not in field_list:
            raise InvalidField
            
        elif len(kwargs)==0:
            query=f'select count({field}) from student'
            
        else:
            f=Student.filter(**kwargs)
            query=f'select count({field}) from student where {f}'
        record=read_data(query)
        return record[0][0]
    

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
def aggregations(field=None,**kwargs):
    field_list=['student_id','name','age','score']
    if field not in field_list:
        raise InvalidField
    elif  len(kwargs)==0:
        query='select'
'''
s=Student.min('age',age=18)
print(s)'''