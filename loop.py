# while loop 
# x = 0
# while x <= 5:
#     print(x)
#     x +=1
# the break statement
# x = 0
# while x <= 10:
#     print(x)
#     if x == 5:
#         break
#     x +=1
# continue statement
# x = 0
# while x <= 10:
#      print(x)
#      if x == 5:
#         continue
    

# for loop   
# fruits = ["apple","banana","orange","mango"]
# for fruit in fruits:
#     if fruit == "orange":
#         continue
#     print(fruit)
# name = "mariam"
# for letter in name:
#     print(letter)

# range function
# for num in range(2,6):
#     print(num)
# else:
#     print("finished")    

# nexted loop
# adj = ["red","big","tasty"]

# fruits = ['apple','banana','cherry']

# for x in adj:
#         for y in fruits:
#                 print(x,y)


# loop through a dictionary
# thisdict ={
#     "brand": "Ford",
#     "model": "mustang",
#     "year": 1964
# }
# for key in thisdict:
#     print(thisdict[key])
# for key ,value in thisdict.items():
#     print(key,value)

'''
1. Create a multiplication table program using while loop, this will be done in such a way that when a 
user supplies any number the multiplication table of that number will be created
'''


multiplicator = int(input('Enter your multiplication number'))
start = int(input("Enter the number you will like  to start "))
answer = 0
stop = int(input("enter the number you want to stop"))
while start < stop:
    start = start + 1
    answer = multiplicator * start
    print(f'{multiplicator} x {start} = {answer}')

