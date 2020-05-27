import re
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
        
    def add_item(self,obj):
        self.obj=obj
        self.list_item.append(obj)
        
        
    def __str__(self):
        if(len(self.list_item)>0):
            return '\n'.join(map(str,self.list_item)) 
        else:
            return ('No items')
            
    def count(self):
        return (len(self.list_item))
    
        
        
    def filter(self,query):
        self.query=query
        result = Store()
        
        if(query.operation == 'EQ'):
            for i in self.list_item:
                if(i.name == query.value or i.price == query.value or i.category == query.value):
                    result.add_item(i)
                        
        elif(query.operation == 'IN'):
            for i in self.list_item:
                if(query.field == 'name'):
                    for j in query.value:
                        if(j == i.name):
                            result.add_item(i)
                                
                elif(query.field == 'price'):
                    for j in query.value:
                        if(j == i.price):
                            result.add_item(i)
                                
                elif(query.field == 'category'):
                    for j in query.value:
                        if(j == i.category):
                            result.add_item(i)
                                
                        
                    
        elif(query.operation == 'GT'):
            for i in self.list_item:
                if(i.price > query.value):
                    result.add_item(i)
                            
        elif(query.operation == 'LT'):
            for i in self.list_item:
                if(i.price < query.value):
                    result.add_item(i)
                            
        elif(query.operation == 'GTE'):
            for i in self.list_item:
                if(i.price >= query.value):
                    result.add_item(i)
                            
        elif(query.operation == 'LTE'):
            for i in self.list_item:
                if(i.price <= query.value):
                    result.add_item(i)
                        
        elif(query.operation == 'STARTS_WITH'):
            for i in self.list_item:
                if((i.name).startswith(query.value) or (i.category).startswith(query.value)):
                        result.add_item(i)
                    
        elif(query.operation == 'ENDS_WITH'):
            for i in self.list_item:
                if((i.name).endswith(query.value) or (i.category).endswith(query.value)):
                        result.add_item(i)
                        
        elif(query.operation == 'CONTAINS'):
            for i in self.list_item:
                if query.field == 'name' :
                    if query.value in i.name :
                        result.add_item(i)
            for i in self.list_item:
                if query.field == 'category':
                    if query.value in i.category :
                        result.add_item(i)
                
        
        return result
        
        
        
        
    def exclude(self,query):
        self.query = query
                
        res = Store()        
        exclude = self.filter(query)
        for item in self.list_item:
            if item not in exclude.list_item :
                res.add_item(item)
        return res
           
        
           
        
        
            
                        
            
        
        
        
       
query = Query(field='price',operation='GT',value=20)

item1 = Item(name = 'oreo',price = 30,category = 'Food')
que = Item(name = 'bingo',price = 20,category = 'Food')
item2 = Item(name = 'butter',price = 10,category = 'Food')



store = Store()
store.add_item(item1)
store.add_item(que)
store.add_item(item2)
print(store.exclude(query))
#print(store)


    