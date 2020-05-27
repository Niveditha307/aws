class Animal:
    
    breath = None
    sound = None
    add_food =0
    def __init__(self,age_in_months =0,breed= None,required_food_in_kgs = 0):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
        if(self._age_in_months >= 10):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        if(self._required_food_in_kgs <=0):
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
   
   
    def grow(self):
        self.age_in_months += 1
        self.required_food_in_kgs += 8
        
    @classmethod
    def breathe(cls):
        print(cls.breath)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @property 
    def age_in_months(self):
        return self._age_in_months
        
    @property 
    def breed(self):
        return self._breed
        
    @property 
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
            
        
class HuntingAnimals:
    animal =""

    def hunt(self,zoo):
        c=0
        for i in zoo.list_animals :
            if type(i). __name__ == self.animal[0]:
                zoo.list_animals.remove(i)
                c=1
                break
        if(c==0):
            print ('No {} to hunt'.format(self.animal[1]))
            
            
class wateranimals :
    @classmethod
    def breathe(cls):
        print('Breathe oxygen from water')
        
class landanimals :
    @classmethod
    def breathe(cls):
        print('Breathe in air')
    
            
            
            
class Deer(Animal,landanimals):
    
    sound ='Buck Buck'
    
    def __init__(self,age_in_months = 0,breed = None,required_food_in_kgs = 0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        self._required_food_in_kgs += 2
        self._age_in_months += 1
        
        
        
class Lion(Animal,HuntingAnimals,landanimals):
    
    sound ='Roar Roar'
    animal =['Deer','deers']
    
    
    def __init__(self,age_in_months = 0,breed = None,required_food_in_kgs = 0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
        
    def grow(self):
        self._required_food_in_kgs += 4
        self._age_in_months += 1
        
    
        
        
            
                
        
class GoldFish(Animal,wateranimals):
    
    sound ='Hum Hum'
    
    def __init__(self,age_in_months = 0,breed = None,required_food_in_kgs = 0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        self._required_food_in_kgs += 0.2
        self._age_in_months += 1
        
class Shark(Animal,HuntingAnimals,wateranimals):
    
    sound ='Shark Sound'
    animal = ['GoldFish','GoldFish']
    
    def __init__(self,age_in_months = 0,breed = None,required_food_in_kgs = 0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        self._required_food_in_kgs += 8
        self._age_in_months += 1
        
        
        
class Snake(Animal,HuntingAnimals,landanimals) :
    
    sound ='Hiss Hiss'
    animal = ['Deer','deers']
    
    def __init__(self,age_in_months = 0,breed = None,required_food_in_kgs = 0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    def grow(self):
        self._required_food_in_kgs += 0.5
        self._age_in_months += 1
        
        
class Zoo(Animal):
    
    count_all = []
    
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.list_animals = []
        
    @property 
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
        
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs += food
        
    def add_animal(self,animal):
        self.list_animals.append(animal)
        self.count_all.append(self.list_animals)
    
    def feed(self,animal):
        if(self._reserved_food_in_kgs !=0):
            self.animal = animal
            self._reserved_food_in_kgs -= self.animal._required_food_in_kgs
            animal.grow()
        else:
            self._reserved_food_in_kgs =0
            
    def count_animals(self):
        return len(self.list_animals)
        
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.count_all)
        
    @staticmethod
    def count_animals_in_given_zoos(zoo_list):
        count = 0
        for i in zoo_list :
            count += i.count_animals()
            
        return count
    



        
    
    
   
deer = Deer(age_in_months=1,breed = 'ELK',required_food_in_kgs =5)
lion = Lion(age_in_months=1,breed = 'Simham',required_food_in_kgs =6)
zoo = Zoo()
na = Zoo()
zoo.add_animal(deer)
zoo.add_animal(lion)
print(zoo.count_animals())
lion.hunt(zoo)
print(zoo.count_animals())


na.add_animal(deer)
na.add_animal(lion)
zoo.feed(deer)
lion.grow()
lion.age_in_months
zoo.add_food_to_reserve(1000)
