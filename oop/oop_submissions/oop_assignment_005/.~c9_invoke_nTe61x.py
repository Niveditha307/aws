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
    list=[]  
    qr = []
    def __init__(self):
        pass
        #super().__init__(self,name,price,category)
    
    def add_item(self,obj):
        self.obj=obj
        Store.list.append(obj)
        
    def filter(self,query):
        self.query=q
        query=list(query)
        #a,b,c=query.split(" ")
        print(self.query)
        
    def __str__(self):
        return '\n'.join(map(str,Store.list))    
        
        
query = Query(field='name',operation='EQ',value='oreo Biscuits')

item = Item(name = 'oreo',price = 10,category = 'Food')
que = Item(name = 'bingo',price = 10,category = 'Food')


store = Store()
store.filter(query)
store.add_item(item)
store.add_item(que)
print(store)


    