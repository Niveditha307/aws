'''
s = 'Banana'
x=0
y=0
for i in range(0,len(s)):
    p = ""
    
    for j in range(i+1):
        c=0
        t=0
        p = p+ s[j]
        for k in range(len(p)):
            if(p[k] =='a'or p[k]=='e' or p[k]=='i' or p[k]=='o' or p[k] == 'u'):
                c=c+1
            else:
                t=t+1
    x=x+c
    y=y+t
        
    print()
    
print(x,y)
'''


s = "banana";list_vowel = ['a','i','o','e','u']
rambo,nivi = 0,0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i] in list_vowel: 
            rambo = rambo+1
        else:
            nivi = nivi +1
            
if rambo < nivi:
    print('nivi won the match')
else:
    print('rambo')