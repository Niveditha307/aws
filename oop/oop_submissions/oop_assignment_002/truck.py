
from car import Car
class Truck(Car):
    
    sound='Honk Honk'
    def __init__(self,color='red',max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
        self._max_cargo_weight = max_cargo_weight
        self._cargo_weight = 0
        
        if(self._max_cargo_weight<0):
            raise ValueError('Invalid value for cargo_weight')
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property 
    def cargo_weight(self):
        return self._cargo_weight
        
    
        
    def load(self,cgo_weight):
        self.cgo_weight=cgo_weight
        if(self.cgo_weight<0):
            raise ValueError('Invalid value for cargo_weight')
        else:
        
            if self._current_speed > 0 :
                print('Cannot load cargo during motion')
            else:
                if(self._cargo_weight + cgo_weight > self._max_cargo_weight):
                    print('Cannot load cargo more than max limit: {}'.format(self.max_cargo_weight))
                else:
                    self._cargo_weight += cgo_weight

    
    def unload(self,cgo_weight):     
        self.cgo_weight=cgo_weight
        
        if(self.cgo_weight<0):
            raise ValueError('Invalid value for cargo_weight')
            
        else:
            
            if(self._current_speed > 0):
                print('Cannot unload cargo during motion')
            else:
                self._cargo_weight -= cgo_weight
    


        










'''class Truck:
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        self._color= color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0
        
        if(self._max_speed < 0):
            raise ValueError('Invalid value for max_speed')    
        if(self._acceleration < 0):
            raise ValueError('Invalid value for acceleration')
        if(self._tyre_friction<0):
            raise ValueError('Invalid value for tyre_friction')
        if(self._max_cargo_weight<0):
            raise ValueError('Invalid value for cargo_weight')
        
        
        
        self._current_speed=0
        self._is_engine_started=False
        
    @property 
    def is_engine_started(self):
        return self._is_engine_started
        
    @property 
    def max_speed(self):
        return self._max_speed
        
    @property 
    def acceleration(self):
        return self._acceleration
        
    @property 
    def tyre_friction(self):
        return self._tyre_friction
   
    @property 
    def color(self):
        return self._color
        
    @property 
    def current_speed(self):
        return self._current_speed
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    @property
    def cargo_weight(self):
        return self._cargo_weight
        
    
    
        
    
    
           
    
   
    def start_engine(self):
        self._is_engine_started=True
        
    def accelerate(self):
        if(self._is_engine_started==True):
            if(self._current_speed + self._acceleration <= self._max_speed):
                self._current_speed+=self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            print('Start the engine to accelerate')
    
    def apply_brakes(self):
        if(self._is_engine_started):
            if(self._current_speed < self._tyre_friction):
                self._current_speed=0
            else:
                self._current_speed = self._acceleration - self._tyre_friction
                
            
    def sound_horn(self):
        if(self._is_engine_started == True):
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
            
    def stop_engine(self):
        if self._is_engine_started == True:
            self._is_engine_started = False
            
            
    def load(self,cgo_weight):
        
        self.cgo_weight=cgo_weight
        if(self.cgo_weight<0):
            raise ValueError('Invalid value for cargo_weight')
        else:
        
            if self._current_speed > 0 :
                print('Cannot load cargo during motion')
            else:
                if(self._cargo_weight + cgo_weight > self._max_cargo_weight):
                    print('Cannot load cargo more than max limit: {}'.format(self.max_cargo_weight))
                else:
                    self._cargo_weight += cgo_weight

            
 
        self.cgo_weight=cgo_weight
        
        if(self.cgo_weight<0):
            raise ValueError('Invalid value for cargo_weight')
            
        else:
            
            if(self._current_speed > 0):
                print('Cannot unload cargo during motion')
            else:
                self._cargo_weight -= cgo_weight'''
    
            
        
    
    



        