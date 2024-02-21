'''
write a pyhton program that takes the temperature of the weather
from the user and tells the user if the weather will be hot,cold or hot

hint 
hot =>  >35 and above
cold => < 20 below
'''
# weather = int(input("Enter your temperature"))
# if weather >= 35:
#     print("The weather is going to be hot today") 
# elif weather <= 20:
#     print("The weather is cold today")
# else:
#     print("the weather is warm today")     

'''
write a python program that takes the weather degree in celcuis and converts it to  fahrenheit

hint
f = (c * 9/5) + 32
'''     
# celcuis = int(input("Enter the degree celcuis"))
# fahrenheit= celcuis * 9/5 + 32 
# print(fahrenheit)

'''
write a python program that converts naira to dollars
hint  : N1,400 => $1
'''
# amount = int(input("Enter your amount in naira"))
# dollar_conversion = amount // 1400
# print(f'{amount} naira is equivalent to ${dollar_conversion}')

'''
write a python program that calculate the area of a circle
hint : A = PI * R square


write a python program to print true if the two numbers given by the user are the same
the
'''
# num1 = 5
# num2 = 5
# if num1 == num2:
#     print(True)
# elif num1 + num2 == 5:
#     print(True)
# elif num1 - num2 == 5:
#     print(True)
# else:
#     print(False)            

# Radius = int(input("Enter your radius value"))
# Pi = 3.142
# Area_of_circle = Pi * Radius

'''
create a list called students and add te following students:
Adebayo,Janet,Blessing,Habeeb,Moses,Alabi. carry out the following operations
1. remove all the names that start with A
2. add the names of all the student in the present python class
3.get the length of the list
4. delete the list
'''
# students=["Adebayo","Janet","Blessing","Habeeb","Moses","Alabi"]
# students.remove('Adebayo')
# students.remove('Alabi')
# print(students)
# No 2
# students.insert(0,'Mariam')
# students.insert(4,'Lawrence')
# students.insert(3,'Temi')
# students.insert(2,'Bouncer')
# students.extend()
# print(students)
# No 3
# print(len(students))
# No 4
# del students
# print(students)

#  create an immutable collection of five colors
# colors= tuple(('Red','Blue','Black','Pink','Green'))
# print(colors)

# create a set method of subject and perform the follwoing
# 1.check if mathematics and english is present in the set
# 2.remove chemistry from the set
# 3. clear out the set

# subject={'English','Mathematics','Chemistry','Biology'}
# print("English" in subject)
# print("Mathematics" in subject)

# no 2
# subject.remove("Chemistry")
# print(subject)
# # no 3
# subject.clear()
# print(subject)

# n0 4
# Employee={
#     "First name": 'Williams',
#     'Last name':'James',
#     'Age': 34,
#     'Work': 'Alabian solution',
#     'Sign in ': '8:30am',
#     'Sign out': "5:00pm",
#     'Monthly salary':500.000,
#     'Job':"Full stack developer",
#     'Proficient':['python,Javascript,Php,Java'],
#     'Vacations':'3 times a year'
# }

# score = int(input('Enter your score'))
# if score >= 70 and score  <= 100:
#     print("Score = Excellence")
# elif score >= 60 and score <= 69:
#     print('Very good')
# elif score >= 50 and score <= 59:
#     print('this is good')  
# elif  score >= 44 and score <= 49:
#     print("Fair grades")   
# elif score >= 35 and   score <= 43:
#     print("This is pass")  
# elif score > 0 and score <= 34:
#     print("fail") 
# else:
#     print("Invalid grade")              


# 
# apc= []
# labour= []
# pdp =[]
# # print("supply name for APC candidates")
# apc.append(input("First name"))
# apc.append(input("Middle name"))
# apc.append(input("Last  name"))
# apc.append(input("Political  party"))

# # print("supply name for labour party candidate ")
# labour.append(input("First name"))
# labour.append(input("Middle name"))
# labour.append(input("Last  name"))
# labour.append(input("Political  party"))

# print("supply name for PDP party candidate ")
# pdp.append(input("First name"))
# pdp.append(input("Middle name"))
# pdp.append(input("Last  name"))
# pdp.append(input("Political  party"))

# print(apc, labour ,pdp)

# grade = float(input("Enter your score"))
# if grade >= 70 and grade <= 100:
#     print("A")
# elif grade >= 60 and grade <= 69:
#     print("B")    
# elif grade >= 50 and grade <= 59:
#     print("C")   
# elif grade >= 45 and grade  <= 49:
#     print("D")
# elif grade >= 40 and grade <= 44:
#     print("E")  
# elif grade >= 0 and grade <= 39:
#     print("F") 
# else:
#     print("Invalid grade")         

# 
# naira = 21750
# modulus =naira % 1000
# print(modulus)

modulus =int(input("enter the modulus"))  
naira = int(input("Enter your amount"))
print(modulus, naira  )
answer= modulus % naira
print(answer)
