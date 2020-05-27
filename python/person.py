class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def description(self):
        print('{} age is {} '.format(self.name,self.age))
        
    def prit(self):
        print('hello from paretn')
    
class Tommy(Dog):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    def prit(self):
        print('hello from child1')
        
        
class  puppy(Dog):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    def prit(self):
        print('hello from child2')
        super().prit()
        
T1=Tommy('a',6,'abc')
p1=puppy('b',7,'xyz')
d=Dog('k',8)
#d.prit()
T1.prit()
p1.prit()

T1.description()
    