
class Dog:
    c=0
    x = dict()
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.x[self.name]=self.age
        Dog.c += 1
        
        print(Dog.x)
    def des(self):
        return f"{self.name}  {self.age}"
        
    

def get_gratest_number(*args):
    return max(args)
m=0
x=['tommy','zimmy','puppy']
y=[6,7,8]
arr = dict()
for k in range(len(x)):
    z=Dog(x[k],y[k])
    p=Dog.des(z)
    arr[x[k]]=y[k]
    
print (sorted(arr.items(),key=lambda l:l[1],reverse=True))


 


