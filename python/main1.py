# age=int(input())
# if 12<age<18:
#     growth_stage="Teen"
#     print("Growth_stage: "+ growth_stage)
# print(str(age) + " years of old")

# number=int(input())
# if number%2:
#     print("odd")
    
# else:
#     print("even")


#age=float(input())

# if 12<age<18:
#     growth_stage="Teen"
#     print("Growth_stage: "+ growth_stage)
# elif 18<=age<21:
#     print("Growth_stage: young")
# elif age>=21:
#     print("Growth_stage: adult")
# else:
#     print("Growth_stage: child")

# print(str(age) + " years of old")
# print(type(age))

# n=int(input())
# i=1
# while i<n:
#     if i<n:
#         print("condition :" + str(i),end=" ")
#     i=i+1
# print(i,end="")
    

# n,i=int(input()),1
# output="1"
# while i<n:
#     i+=1
#     if i%5==0:
#         continue
#     print(output +=" " + str(i))

# def add(a,b):
#     return a+b
    
# a=add(3,5)
# print(a)

# def greet(name="world",greeting="Hello"):
#     print(greeting + " " + name + "!")

    
# a=greet
# a()
# a("Developers",greeting="hey")
# a("hey")


# def get_operator(operator):
#     if operator=='ADD':
#         return 'add'
#     if operator=='MULTIPLY':
# op=get_operator('ADD')
# print(op(2,4))


# add=lambda x,y:x+y
# c=add(2,3)
# print(c)





# a=lambda x,y:x+y
# print(a(2,3))

# double=lambda x:2*x
# print(double(6))

# half=lambda x:x/2
# print(half(6))

# print((lambda x,y,z=3:x+y+z)(1,y=2))
    
    
    
# Built In functions
# sorted()
# sorted(a,reverse=True)
# sorted('authentiation')

# words=['i','was','wondering','about','this']
# sorted(words,key=len,reverse=True)

# sorted['A9','B6','D8','C4','X0','Y2'] key=lambda x:int(x[-1])



# ages=[('john',42),('julie',35),('Rob',23),('john',12)]
# ages_map=dict(ages)
# print(ages_map)
# t=ages_map.get('julie')
# print(t)
# ages_map['john']=35
# ages_map['Teja']=26



# print(ages_map.keys())
# print(ages_map.values())
# print(list(ages_map.keys()))
# print(list(ages_map.values()))
# print(ages_map.items())


# for k,v in ages_map.items():
#     print(k,v)
    
    
# def more_kwargs(a,**kwargs):
#     print(a)
#     print(kwargs)
# more_kwargs(1,b=10,c=9,d=5,number=0)
# more_kwargs(1)


# def greet(name="World",greeting="helo"):
#     print(greeting+""+name+"!")
# data={"name":"Hey","greeting":"python"}
# greet(**data)

# from collections import Counter
# ages=[22,23,24,24,24]
# value_count=Counter(ages)
# print(value_count.most_common())

# if __name__ == "__main__":
#     import sys
#     print(sys.argv)

Acessing internet with python
