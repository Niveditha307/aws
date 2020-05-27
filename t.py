class Pets:
    dogs=[]
    
    def __init__(self,dogs):
        self.dogs=dogs
        
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class BullDog(Dog):
    def run(self,speed):
        self.speed=speed
        
class RusselDog(Dog):
    
    def run(self,speed):
        self.speed=speed

mydogs=[BullDog('tommy',6),RusselDog('puppy',8),Dog('kitty',10)]
mypets=Pets(mydogs)

def gratest_number(*args):
    return max(args)
    
c=-9999
k=""    
for dog in mypets.dogs:
    print('{} {}'.format(dog.name,dog.age))
    if(c<dog.age):
        c=dog.age
        k=dog.name
        
print('{} years older dog is {}'.format(k,c))
    
    