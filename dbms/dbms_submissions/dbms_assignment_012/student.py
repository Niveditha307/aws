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


class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass



class Student:
    def __init__(self, student_id = None,name = None, age = None, score = None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score
        
    
    
    @classmethod    
    def get(cls,**kwargs):
        
        for k,v in kwargs.items():
            
            if 'score'== k :
                data = read_data('''select * from student where score = {}''' . format(v))
            
            elif 'name' == k :
                data = read_data('''select * from student where name like '%{}%' ''' . format(v))
                
            elif 'age'== k :
                data = read_data('''select * from student where age = {}''' . format(v))
            
            elif 'student_id' == k :
                data = read_data('''select * from student where student_id = {}''' . format(v))
                
            
            else : 
                raise InvalidField
                
            
                
            if len(data) > 1:
                raise MultipleObjectsReturned
                
            elif len(data) == 0:
                raise DoesNotExist
            
            else :
                
                obj = Student(*data[0])
                return (obj)
        
            
    def delete(self):
         write_data('''delete from student where student_id = {}'''.format(self.student_id))
         
         
    def save(self):
        
            import sqlite3
            conn = sqlite3.connect("students.sqlite3")
            c = conn.cursor()
            if(self.student_id == None):
                c.execute('''insert into student(name,age,score) values (?,?,?)''',(self.name,self.age,self.score))
                self.student_id = c.lastrowid
                
                
            
            
            elif (c.execute('select {}  in (select student_id from student) from student'.format(self.student_id))) :
                c.execute('''insert or REPLACE into student(student_id,name,age,score) values (?,?,?,?)''',(self.student_id,self.name,self.age,self.score))
           
           
            else :
                c.execute('''update student set name = ? ,age = ?,score = ? where student_id = ?''',(self.name,self.age,self.score,self.student_id))   
             
            
            conn.commit()
            conn.close()
            
'''           
stu = Student.get(student_id = 10)
stu.student_id = 51
stu.save()'''




