import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
        
        if(self.real_part == str(self.real_part) and (self.imaginary_part == str(self.imaginary_part))):
            raise ValueError('Invalid value for real and imaginary part')
        
        
        elif (self.real_part == str(self.real_part)):
            raise ValueError('Invalid value for real part')
            
        
        elif (self.imaginary_part == str(self.imaginary_part)):
            raise ValueError('Invalid value for imaginary part')
            
            
    def __str__(self):
        return( f"{self.real_part}{self.imaginary_part:+}i")
        
    def conjugate(self):
        return ComplexNumber((self.real_part),-(self.imaginary_part))
            
        
    def __add__(self,other):
        re = self.real_part + other.real_part
        im = self.imaginary_part + other.imaginary_part
        return ComplexNumber(re,im)
        
        
    def __sub__(self,other):
        re = self.real_part - other.real_part
        im = self.imaginary_part - other.imaginary_part
        return ComplexNumber(re,im)
        
        
    def __mul__(self,other):
        re = (self.real_part * other.real_part - self.imaginary_part * other.imaginary_part) 
        im = (self.real_part * other.imaginary_part + self.imaginary_part * other.real_part)
        return ComplexNumber(re,im)
        
        
    def __truediv__(self,other):
        a,b,c,d=self.real_part,self.imaginary_part,other.real_part,other.imaginary_part
        k=(pow(c,2))+(pow(d,2))
        re = ((a*c)+(b*d))/k
        im = ((b*c)-(a*d))/k
        return ComplexNumber (re,im)
        
        
    def __abs__(self):
        re = pow(self.real_part,2) + pow(self.imaginary_part,2)
        return(round(math.sqrt(re),3))
        
        
    def __eq__(self,other):
        
        if(self.real_part == other.real_part and self.imaginary_part == other.imaginary_part):
            return (True)
        else:
            return (False)
    
    
            
            
        
        
