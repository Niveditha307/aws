class Pokemon:
    sound = ''
    def __init__(self,name=None,level = 1):
        self._name = name
        self._level = level
        self._master = None
        
        if((self._name) == '' or (self._name == None)):
            raise ValueError('name cannot be empty')
        if(self._level <= 0):
            raise ValueError('level should be > 0')
            
    @property 
    def name(self):
        return self._name
    @property 
    def level (self):
        return self._level
        
    @property 
    def master(self):
        if(self._master == None):
            print('No Master')
        else :
            return self._master
        
    @classmethod
    def make_sound(cls):
        if(len(cls.sound)!=0):
            print(cls.sound)
        else :
            raise ValueError('no sound ')
        
        
    def __str__(self):
        return f'{self.name} - Level {self.level}'
        
        
class Running :
    ran =""
    @classmethod
    def run(cls):
        print(cls.ran)
        
class Flying :
    fli = ""
    @classmethod
    def fly(cls):
        print(cls.fli)
        
class Swimming :
    sim = ""
    
    @classmethod
    def swim(cls):
        print(cls.sim)
        
    
        
        
class Pikachu(Pokemon,Running):
    
    sound ='Pika Pika'
    ran = 'Pikachu running...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Electric attack with {} damage'.format(self._level * 10))
        
class Squirtle(Pokemon,Running,Swimming):
    
    sound ='Squirtle...Squirtle'
    ran = 'Squirtle running...'
    sim = 'Squirtle swimming...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Water attack with {} damage'.format(self._level * 9))
        
class Pidgey(Pokemon,Flying):
    
    sound ='Pidgey...Pidgey'
    fli = 'Pidgey flying...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Air attack with {} damage'.format(self._level * 5))
        
class Swanna(Pokemon,Flying,Swimming):
    
    sound ='Swanna...Swanna'
    fli = 'Swanna flying...'
    sim = 'Swanna swimming...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Water attack with {} damage'.format(self._level* 9))
        print('Air attack with {} damage'.format(self._level * 5))
        
        
class Zapdos(Pokemon,Flying):
    
    sound ='Zap...Zap'
    fli = 'Zapdos flying...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        
        print('Electric attack with {} damage'.format(self._level * 10))
        print('Air attack with {} damage'.format(self._level * 5))


class Island :
    
    list_islands = []
    
    def __init__(self,name = None,max_no_of_pokemon = 0,total_food_available_in_kgs = 0):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        Island.list_islands.append(self)
        
    
    @property 
    def name(self):
        return self._name
    
    @property 
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property 
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property 
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f'{self.name} - {self.pokemon_left_to_catch} pokemon - {self.total_food_available_in_kgs} food'
        
    
    def add_pokemon(self,pokemon):
        self.pokemon = pokemon
        if(self._pokemon_left_to_catch == self._max_no_of_pokemon):
            print('Island at its max pokemon capacity')
        else:
            self._pokemon_left_to_catch += 1
    
    @classmethod
    def get_all_islands(cls):
        return Island.list_islands
        
    
    
            
class Trainer:
    
    def __init__(self,name = None):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        self._current_island = None
        self.list_catch = [] 
        
        
    @property 
    def name(self):
        return self._name
    
    @property 
    def experience(self):
        return self._experience
        
    @property 
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    @property 
    def food_in_bag(self):
        return self._food_in_bag
        
        
    @property 
    def current_island(self):
        #return self._current_island
        if(self._current_island != None):
                return self._current_island
        else:
            print('You are not on any island')
                
        
        
        
    def move_to_island(self,island):
        #self.island = island
        self._current_island = island
            
           
    def collect_food(self):
        if(self._current_island!= None):
            if(self._current_island._total_food_available_in_kgs > self._max_food_in_bag):
                if(self.food_in_bag < self._max_food_in_bag):
                    self._food_in_bag += self._max_food_in_bag
                    self._current_island._total_food_available_in_kgs -= self._food_in_bag
                else:
                    self._food_in_bag = self._max_food_in_bag
            else:
                self._food_in_bag += self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs = 0
                
        else :
            print('Move to an island to collect food')
            
    
    def catch(self,pokemon):
        self.pokemon = pokemon
        #pokemon._master = self
        if(self._experience >= 100 * self.pokemon._level):
            print('You caught {}'.format(self.pokemon.name))
            self._experience += self.pokemon._level * 20
            self.list_catch.append(self.pokemon)
            pokemon._master = self
        else:
            print('You need more experience to catch {}'.format(self.pokemon.name))
            
    def get_my_pokemon(self):
        return (self.list_catch)
            
        
        
    