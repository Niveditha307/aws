

class Pole :
    def __init__(self,question= None,options1 = None,options2 = None,answer = None):
        self.question = question
        self.options1 = options1
        self.options2 = options2
        self.answer = answer
        print(self.question)
        
    def correct_answer(self,ans=None):
        self.ans = ans
        if(self.ans == self.answer):
            print("Correct answer")
        else :
            raise ValueError("amswer is not correct")
        
    
p =Pole("What is ineritance","1,deriving properties from parent","2.deriving properties from child","deriving properties from parent") 

p.correct_answer("deriving properties from parent")
        
