class Pokemon:
    sound = ''
    def __init__(self,name=None,level = 1):
        self._name = name
        self._level = level
        
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
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
        
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
        self._level += 1
        
class Squirtle(Pokemon,Running,Swimming):
    
    sound ='Squirtle...Squirtle'
    ran = 'Squirtle running...'
    sim = 'Squirtle swimming...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Water attack with {} damage'.format(self._level * 9))
        self._level += 1
        
class Pidgey(Pokemon,Flying):
    
    sound ='Pidgey...Pidgey'
    fli = 'Pidgey flying...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Air attack with {} damage'.format(self._level * 5))
        self._level += 1
        
class Swanna(Pokemon,Flying,Swimming):
    
    sound ='Swanna...Swanna'
    fli = 'Swanna flying...'
    sim = 'Swanna swimming...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        print('Water attack with {} damage'.format(self._level* 9))
        print('Air attack with {} damage'.format(self._level * 5))
        self._level += 1
        
        
class Zapdos(Pokemon,Flying):
    
    sound ='Zap...Zap'
    fli = 'Zapdos flying...'
    
    def __init__(self,name= None,level = 1):
        super().__init__(name,level)
        
    def attack(self):
        
        print('Electric attack with {} damage'.format(self._level * 10))
        print('Air attack with {} damage'.format(self._level * 5))
        self._level += 1



    
    