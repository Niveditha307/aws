print('you need to form a word with below letters')
print(" 'a' 'c' 'r' 'e' 'o' 's' ")
li = ['rose','car','race']
score = 0
c=0
print(score)
for i in range(len(li)):
        s = input('enter a word : ')
        if s in li:
            c=1
            if(len(s) == 3):
                score += 2
            else :
                score += 3
        else :
            score -= 1
            i=i-1
            print("sorry wrong word entered")
            print('your score decreases 1')
    
print('your score is {}'.format(score))
            
            
            
    
        

    