class Pets:
    dogs=[]
    
    def __init__(self,dogs):
        self.dogs=dogs
        
    def walk(self):
        for dog in self.dogs:
            print(dog.walk())
        
class Dog:
    
    species='mammal'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sound=''
        self.is_hungry=True
        
        
    def description(self):
        return (self.name,self.age)
        
    def eat(self):
        self.is_hungry=False
        
    def run(self,sound):
        self.sound=sound
        return '{} runs {}'.format(self.name,self.sound)
        
    def walk(self):
        return '{} is walking'.format(self.name)
        
        
class RuusselDog(Dog):
    
    def run(self,sound):
        self.sound=sound
        return '{} runs {}'.format(self.name,self.sound)
        
class BullDog(Dog):
    
    def run(self,sound):
        self.sound=sound
        print(self.name)
        return '{} runs {}'.format(self.name,self.sound)
        
        
        
pet=[BullDog('tom',9),RuusselDog('pup',8),Dog('kit',10)]
mypets=Pets(pet)

print('i have {} dogs'.format(len(mypets.dogs)))
for dog in mypets.dogs:
    dog.eat()
    dog.walk()
    print('{} {}'.format(dog.name,dog.age))
print('of course all are {} '.format(Dog.species))

are_all_hungry=True

if(dog.is_hungry==False):
    are_all_hungry=False
if are_all_hungry==False:
    print('my dogs are not hungry')
else:
    print('dogs are hungry')

for dog in mypets.dogs:    
    print(dog.run('slowly'))
    print(dog.walk())
    
#d = BullDog()    
#print(d.run('slowly'))