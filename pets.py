class pets:
    dogs=[]
    
    def __init__(self,dogs):
        self.dogs=dogs
        
class Dog:
    species='mammal'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def description(self):
        return self.name,self.age
        
    def eat(self):
        self.is_hungry=False
        
class RussellTerrier(Dog):
    def run(self,speed):
        return '%s says %s ' %(self.name,speed)

class Bulldog(Dog):
    def run(self,speed):
        return '%s says %s' %(self.name,speed)

mydogs=[Bulldog('Tom',6),
RussellTerrier('Fletcher',7),Dog('Larry',9)]

mypets=pets(mydogs)

print('I have {} dogs.'.format(len(mypets.dogs)))
for dog in mypets.dogs:
    print('{} is {}.'.format(dog.name,dog.age))
    #dog.eat()
    
print('And they are all {} ,of course'.format(dog.species))
d=Dog("fdb",3)
print('{} is a {} '.format(dog.name,dog.age))

are_my_dogs_hungry=False

for dog in mypets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry=True
        
if are_my_dogs_hungry:
    print('My dogs are hungry')
else:
    print('My dogs are not hungry')