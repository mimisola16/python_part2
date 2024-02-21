# class Human:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.ages = age
#         self.gende = gender
#         print("She is beautiful")

#     def character(self):
#         print( self.name +" is a good girl")
        
#     def age(self):  
#         print(f"i am {self.ages} years old")   
        
#     def gender(self):
#         print("i am a "+ self.gende)  
        
#     def myFunc(self,behaviour):
#         print("She as " + behaviour + " character" )     
        
# Mimi = Human("mariam",21,"female")
# Mimi.character()
# Mimi.age() 
# Mimi.gender() 
# Mimi.myFunc("good") 

# class shark:
#     def __init__(self,swim,feed):
#         self.swim = swim
#         self.feed = feed
#     def mySwimming(self):
#         print("Shark swims faster")
      
#     def feed(self):
#         print("feeds on other fish")    
     
# class Clownfish(shark):
#     def live_with_anemone(self):
#         print(f"The clownfish swims {self.swim} and {self.feed} through it fins")   
     
#     def food(self):
#         print("shark feeds on little " + self.feed)
                 

# fish = Clownfish("faster", "eats" )
# fish.live_with_anemone()
# fish.food()


import module as x
x.greeting("Mariam")