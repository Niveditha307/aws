class Person:
    
    def __init__(self,age = 0):
        self.age = age;
        if(self.age < 0):
            print('Invalid age')
            
        self.age += 3
        if (self.age < 13):
            print('child')
        else:
            print('adult')
            
            
a = Person(age = -1)
print(a.age)