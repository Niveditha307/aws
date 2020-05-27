'''import re
class Item:
    def __init__(self,name=None,price=0,category=None):
        self.name=name
        self.price=price
        self.category=category
        
        if(self.price <= 0):
            raise ValueError('Invalid value for price, got {}'.format(self.price))



    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"
        
class Query:
    
    li=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
    def __init__(self,field=None,operation=None,value=None):
        self.field = field
        self.operation = operation
        self.value = value
        
        if operation not in Query.li:
            raise ValueError('Invalid value for operation, got {}'.format(self.operation))
            
    
        
    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"
        
        
class Store:
    qr = []
    def __init__(self):
        self.list_item =[]
        self.list_item1 = []
        self.opposite_list = []
        #super().__init__(self,name,price,category)
    
    def add_item(self,obj):
        self.obj=obj
        self.list_item.append(obj)
        
        
    def filter(self,query):
        self.query=query
        result = Store()
        
        if(query.operation == 'EQ'):
            for i in range(len(self.list_item)):
                if(self.list_item[i].name == query.value or self.list_item[i].price == query.value or 
                self.list_item[i].category == query.value):
                    self.list_item1.append(self.list_item[i])
                else:
                    
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_59',self.opposite_list)
                        
        elif(query.operation == 'IN'):
            for i in range(len(self.list_item)):
                if(query.field == 'name'):
                    for j in query.value:
                        if(j == self.list_item[i].name):
                            self.list_item1.append(self.list_item[i])
                        else:
                            #self.obj.opposite(self.list_item[i])
                            self.opposite_list.append(self.list_item[i])
                            #print('line_70',self.opposite_list)
                                
                elif(query.field == 'price'):
                    for j in query.value:
                        if(j == self.list_item[i].price):
                            self.list_item1.append(self.list_item[i])
                        else:
                            self.obj.opposite(self.list_item[i])
                            #self.opposite_list.append(self.list_item[i])
                            #print('line_79',self.opposite_list)
                                
                elif(query.field == 'category'):
                    for j in query.value:
                        if(j == self.list_item[i].category):
                            self.list_item1.append(self.list_item[i])
                        else:
                            #self.obj.opposite(self.list_item[i])
                            self.opposite_list.append(self.list_item[i])
                           # print('line_88',self.opposite_list)
                                
                        
                    
        elif(query.operation == 'GT'):
            for i in range(len(self.list_item)):
                if(self.list_item[i].price > query.value):
                    self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_99',self.opposite_list)
                            
        elif(query.operation == 'LT'):
            for i in range(len(self.list_item)):
                if(self.list_item[i].price < query.value):
                    self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_108',self.opposite_list)
                            
        elif(query.operation == 'GTE'):
            for i in range(len(self.list_item)):
                if(self.list_item[i].price >= query.value):
                    self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_117',self.opposite_list)
                            
        elif(query.operation == 'LTE'):
            for i in range(len(self.list_item)):
                if(self.list_item[i].price <= query.value):
                    self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_126',self.opposite_list)
                        
        elif(query.operation == 'STARTS_WITH'):
            for i in range(len(self.list_item)):
                if((self.list_item[i].name).startswith(query.value) or 
                    (self.list_item[i].category).startswith(query.value)):
                        self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_136',self.opposite_list)
                    
        elif(query.operation == 'ENDS_WITH'):
            for i in range(len(self.list_item)):
                if((self.list_item[i].name).endswith(query.value) or 
                    (self.list_item[i].category).endswith(query.value)):
                        self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i]) 
                    #print('line_146',self.opposite_list)
                        
        elif(query.operation == 'CONTAINS'):
            for i in range(len(self.list_item)):
                x=self.list_item[i].name
                z=self.list_item[i].category
                y=re.findall(query.value,x)
                k=re.findall(query.value,z)
                if(y):
                    self.list_item1.append(self.list_item[i])
                else:
                    self.opposite_list.append(self.list_item[i])
                    #print('line_158',self.opposite_list)
                if(k):
                    self.list_item1.append(self.list_item[i])
                else:
                    #self.obj.opposite(self.list_item[i])
                    self.opposite_list.append(self.list_item[i])
                    #print('line_163',self.opposite_list)    
                        #print(Store.list_item[i])
                        
            
        
        return '\n'.join(map(str,self.list_item1)) 
        
        
        
        
    def exclude(self,query):
        #print('call to exclude')
        self.filter(query)
        return '\n'.join(map(str,self.opposite_list))
        #print(self.opposite_list)
        
        
            
                        
            
        
    def __str__(self):
    return '\n'.join(map(str,self.list_item))    
       
query = Query(field='category',operation='EQ',value='Food')

item1 = Item(name = 'oreo',price = 30,category = 'Food')
que = Item(name = 'bingo',price = 20,category = 'Food')
item2 = Item(name = 'butter',price = 10,category = 'grocry')



store = Store()
store.add_item(item1)
store.add_item(que)
store.add_item(item2)
#print(store.filter(query))
print(store.exclude(query))
#print(store)'''


class Fruits:
    def __init__(self,fruit_name,fruit_cost,fruit_color):
        self.fruit_name = fruit_name
        self.fruit_cost = fruit_cost
        self.fruit_color = fruit_color
        
    def display(self,msg):
        self.msg = msg
        print('eating fruits are very {}'.format(self.msg))
        
    
fr = Fruits('apple',30,'Red')
fr.display('healthy')

        

    