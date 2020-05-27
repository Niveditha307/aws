class Deer:
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        
        if(self.age_in_months >9):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        
    def grow(self):
        self.required_food_in_kgs += 2
        self.age_in_months += 1
        
    def make_sound(self):
        print('Buck Buck')
    
    def breathe(self):
        print('Breathe in air')
        
        
class Lion(Deer):
    
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        
        if(self.age_in_months >9):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        
    def grow(self):
        self.required_food_in_kgs += 4
        self.age_in_months += 1
        
    def make_sound(self):
        print('Roar Roar')
    
    def breathe(self):
        print('Breathe in air')
        
    def hunt(self):
        pass
    
class Shark(Deer) :
    
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        
        if(self.age_in_months >9):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        if(self.required_food_in_kgs ==0 or self.required_food_in_kgs == str(self.required_food_in_kgs)):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.required_food_in_kgs))
        
            
        
    def grow(self):
        self.required_food_in_kgs += 8
        self.age_in_months += 1
        
    def make_sound(self):
        print('Shark Sound')
    
    def breathe(self):
        print('Breathe oxygen from water')
        
    def hunt(self):
        pass
    
class GoldFish(Deer):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        
        if(self.age_in_months >9):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        if(self.required_food_in_kgs ==0 or self.required_food_in_kgs == str(self.required_food_in_kgs)):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.required_food_in_kgs))
        
            
        
    def grow(self):
        self.required_food_in_kgs += 0.2
        self.age_in_months += 1
        
    def make_sound(self):
        print('Hum Hum')
    
    def breathe(self):
        print('Breathe oxygen from water')
        
    def hunt(self):
        pass
    
    
class Snake(Deer):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        
        if(self.age_in_months >9):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        if(self.required_food_in_kgs ==0 or self.required_food_in_kgs == str(self.required_food_in_kgs)):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.required_food_in_kgs))
        
            
        
    def grow(self):
        self.required_food_in_kgs += 0.5
        self.age_in_months += 1
        
    def make_sound(self):
        print('Hiss Hiss')
    
    def breathe(self):
        print('Breathe in air')
        
    def hunt(self):
        pass

    
    
class Zoo :
    
    def __init__(self):
        self.reserved_food_in_kgs = 0
        self.c=0
        self.list_animals = []
        
    def add_food_to_reserve(self,food):
        self.reserved_food_in_kgs = food
        
    def count_animals(self):
        pass
    
    def feed(self,animal):
        if(animal == 'gold_fish'):
            self.reserved_food_in_kgs -= 0.2
        elif(animal == 'deer'):
            self.reserved_food_in_kgs -=2
        elif(animal == 'snake'):
            self.reserved_food_in_kgs -=0.5
        elif(animal == 'shark'):
            self.reserved_food_in_kgs -=8
        elif(animal == 'lion'):
            self.reserved_food_in_kgs -=4
            
    def add_animal(self,obj):
        pass
        
            
        
        
    
    
        