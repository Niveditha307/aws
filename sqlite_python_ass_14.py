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


class InvalidField(Exception):
    pass


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score

    @classmethod
    def aggregation(cls,attr = None,field = "",**kwargs):
           
        list = ['name','age','score','student_id','']
        if field not in list:
            raise InvalidField
        
        if(len(kwargs) == 0):
            if field in ['age','score','student_id','name']:
                data = read_data('''select {}({}) from student'''.format(attr,field))
                return data[0][0]
                
            else :
                raise InvalidField
                
        else :
            keys_li = []
            mc = kwargs
            for k,v in kwargs.items():
                keys_li.append(k)
                
                
            if(len(keys_li) == 1):
                
                for k,v in kwargs.items():
                    key = (k.split('__'))
                    value = v
                    print(key,value)
                    
                    if len(key) == 1:
                        if key[0] in ['student_id','age','score']:
                            data = read_data('''select {}({}) from Student where {} = {}'''.format(attr,field,key[0],v))
                        
                        elif key[0] == 'name':
                            data = read_data('''select {}({}) from Student where {} like '%{}%' '''.format(attr,field,key[0],v))
                    
                        else : 
                            raise InvalidField
                    
                    elif len(key) >= 1:
                 
                        if field in ['age','score','student_id'] :  
                            if key[1] == 'lt':
                                if key[0] in ['age','score','student_id']:
                                    data = read_data('''select {}({}) from Student where {} < {}'''.format(attr,field,key[0],v))
                                
                                else : 
                                    raise InvalidField
                                            
                                        
                            elif key[1] == 'gt':
                                if key[0] in ['age','score','student_id']:
                                    data = read_data('''select {}({}) from Student where {} > {}'''.format(attr,field,key[0],v))
        
                                else :
                                    raise InvalidField
                                                    
                            elif key[1] == 'lte':
                                if key[0] in ['age','score','student_id']:
                                    data = read_data('''select {}({}) from Student where {} <= {}'''.format(attr,field,key[0],v))
                                    
                                else :
                                    raise InvalidField
                                                    
                            elif key[1] == 'gte':
                                if key[0] in ['age','score','student_id']:
                                    data = read_data('''select {}({}) from Student where {} >= {}'''.format(attr,field,key[0],v))
                                
                                else :
                                    raise InvalidField
                                        
                            elif key[1] == 'in':
                                if key[0] in ['name','age','score','student_id']:
                                    data = read_data('''select {}({}) from Student where {} in {}'''.format(attr,field,key[0],tuple(v)))
                                    
                                else :
                                    raise InvalidField
                                
                            elif key[1] == 'neq':
                                if key[0] in ['age','score','student_id']:
                                    data = read_data('''select {}({}) from Student where {} <> {}'''.format(attr,field,key[0],v))
                                    
                                        
                                elif key[0] == 'name':
                                    data = read_data('''select {}({}) from Student where {} <> '{}' '''.format(attr,field,key[0],v))
                                    
                                    
                                else :
                                    raise InvalidField
                                
                                        
                            elif key[1] == 'contains' :
                                
                                if key[0] == 'name':
                                    data = read_data('''select {}({}) from Student where {} like '%{}%' '''.format(attr,field,key[0],v))
                                
                                else :
                                    raise InvalidField
                            
                            return data[0][0]            
                                    
                                
                else :
                        
                    symboles = {'lt':'<','gt':'>','lte':'<=','gte':'>=','eq':'='}
                    joining = []
                    for i in range(len(keys_li)):
                        k = keys_li[i].split('__')
                        if k[1] in ['lt','gt','lte','gte'] :
                            sql = '{} {} {}'.format(k[0],symboles[k[1]],mc[keys_li[i]])
                            joining.append(sql)
                                        
                            l = (' and '.join(joining))
                                        
                                        
                    data = read_data('''select {}({}) from student where {}'''.format(attr,field,l))
                        #print(data[0][0])
                    return(data[0][0])
                
                
            
            else :
                        
                symboles = {'lt':'<','gt':'>','lte':'<=','gte':'>=','eq':'='}
                joining = []
                for i in range(len(keys_li)):
                    k = keys_li[i].split('__')
                    if k[1] in ['lt','gt','lte','gte'] :
                        sql = '{} {} {}'.format(k[0],symboles[k[1]],mc[keys_li[i]])
                        joining.append(sql)
                                        
                        l = (' and '.join(joining))
                                        
                                        
                data = read_data('''select {}({}) from student where {}'''.format(attr,field,l))
                        #print(data[0][0])
                return(data[0][0])
                
                                        
                        
    @classmethod
    def avg(cls,field,**kwargs):
        return cls.aggregation('AVG',field,**kwargs)
                                
                                
    @classmethod
    def sum(cls,field,**kwargs):
        return cls.aggregation('SUM',field,**kwargs)
    
    @classmethod
    def count(cls,field="",**kwargs):
        return cls.aggregation('COUNT',field,**kwargs)
    
    @classmethod
    def min(cls,field,**kwargs):
        return cls.aggregation('MIN',field,**kwargs)
    
    @classmethod
    def max(cls,field,**kwargs):
        return cls.aggregation('MAX',field,**kwargs)
 
        
'''      
avg_age = Student.avg('age',age__gt = 18)
print(avg_age)'''

'''
avg_age = Student.avg('age', age__gt=18, age__lt=21)
print(avg_age)'''

'''
min_age = Student.min('age', age__gt=18)
print(min_age)

sum_of_age = Student.sum('age', score__gt=30)
print(sum_of_age)'''

'''
sum_of_age = Student.sum('age', score__gt=30, age__lt=30)
print(sum_of_age)


count = Student.count('age', score__gt=30, age__lt=30)
print(count)'''


count = Student.count()
print(count)
