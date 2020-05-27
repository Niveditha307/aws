
class Deer:
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
        if(self._age_in_months >9):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        
        if(self._required_food_in_kgs <=0):
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
        
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @property
    def breed(self):
        return self._breed
    
        
        
        
    
        
    def grow(self):
        self._required_food_in_kgs += 2
        self._age_in_months += 1
    
    @classmethod    
    def make_sound(cls):
        print('Buck Buck')
        
    @classmethod
    def breathe(cls):
        print('Breathe in air')
        
        
class Lion(Deer):
    
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        self._required_food_in_kgs += 4
        self._age_in_months += 1
        
    @classmethod   
    def make_sound(cls):
        print('Roar Roar')
    
    @classmethod
    def breathe(cls):
        print('Breathe in air')
        
    def hunt(self,zoo):
        self.c=0
        self.zoo = zoo
        for i in zoo.count_all:
            if(isinstance(i,Deer)):
                self.c +=1
                Zoo.count_all.remove(i)
                Zoo.count_single -=1
        if(self.c==0):
            print('No deers to hunt')
            
        
    
class Shark(Deer) :
    
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
            
        
    def grow(self):
        self._required_food_in_kgs += 8
        self._age_in_months += 1
    
    @classmethod    
    def make_sound(cls):
        print('Shark Sound')
    
    @classmethod
    def breathe(cls):
        print('Breathe oxygen from water')
        
    def hunt(self):
        c=0
        for i in Zoo.count_all:
            if(isinstance(i,GoldFish)):
                c=c+1
                Zoo.count_all.remove(i)
        if(c==0):
            print('No gold_fish to hunt')
        
    
class GoldFish(Deer):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
            
        
    def grow(self):
        self._required_food_in_kgs += 0.2
        self._age_in_months += 1
        
    @classmethod    
    def make_sound(cls):
        print('Hum Hum')
    
    @classmethod
    def breathe(self):
        print('Breathe oxygen from water')
        
    def hunt(self):
        pass
    
    
class Snake(Deer):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
            
        
    def grow(self):
        self._required_food_in_kgs += 0.5
        self._age_in_months += 1
        
    @classmethod    
    def make_sound(cls):
        print('Hiss Hiss')
    
    
    @classmethod
    def breathe(self):
        print('Breathe in air')
        
    def hunt(self):
        c=0
        for i in Zoo.count_all:
            if(isinstance(i,Deer)):
                c=c+1
                Zoo.count_all.remove(i)
        if(c==0):
            print('No gold_fish to hunt')
        
    

class Zoo:
    count_all = []
    
    def __init__(self):
        self.reserved_food_in_kgs = 0
        
        
    def add_food_to_reserve(self,food):
        self.reserved_food_in_kgs = food
        
    def add_animal(self,obj):
        self.obj = obj
        self.list_animals.append(self.obj)
        self.count_all.append(self.obj)
     
     
    
    def feed(self,animal):
        #self.animal_obj = animal
        if(self.reserved_food_in_kgs !=0):
            self.reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
        else:
            self.reserved_food_in_kgs =0
            
    
    def count_animals(self):
        return(len(self.count_single))
            
    
    @classmethod   
    def count_animals_in_all_zoos(cls):
        return(len(cls.count_all))
    
    def count_animals_in_given_zoos(self,list_item):
        self.list_item = list_item
    



    
    
            
            
'''           
zoo = Zoo()
gold_fish = GoldFish(age_in_months = 1,breed = 'Nemo',required_food_in_kgs = 0.5)
deer = Deer(age_in_months = 1,breed = 'ELK',required_food_in_kgs = 4)
zoo.add_animal(gold_fish)
zoo.add_animal(deer)
zoo.count_animals()
zoo.count_animals_in_all_zoos()
zoo.add_food_to_reserve(1000)
zoo.feed(gold_fish)
zoo.feed(deer)

national = Zoo()
gold_fish = GoldFish(age_in_months = 1,breed = 'Nemo',required_food_in_kgs = 0.5)
deer = Deer(age_in_months = 1,breed = 'ELK',required_food_in_kgs = 4)
national.add_animal(gold_fish)
national.add_animal(deer)
national.count_animals()
national.count_animals_in_all_zoos()'''







        
            
        
        
    
    
        