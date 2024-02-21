# def start():
#     print("Hello World")
# start()
# passing a prams
# def student_profile(fname,lname,age):
#     print(f'{fname} {lname} is {age} years old')
# student_profile('Afolabi','Mariam',16)
# default value
# def student_profile(fname, age,lname ='Ajayi'):
#     print(f'{fname} {lname} is {age} years old')
# student_profile('Afolabi',16)


# def add_number(num2,num1):
#     print(num1 + num2)

# add_number(4, 5)   

# def User_detail(name):
#     print(f'Welcome {name}' )
# User_detail("MARIAM")    
# def User_detail(name,state,Country):
#     print(f' {name} is from {state}and she lives in {Country}' )
# User_detail("Mariam","Osun-state ", 'Nigeria')    

# return value
def my_func(num):
    return 5 * num
# print(my_func(5))

def sum_num(num1,num2):
    total = num1 + num2
    # print(total)
sum_num(2,4)    

def greeting(name):
    global surname
    surname = 'Afolabi'
    print(f'Welcome,{surname} {name}')
greeting('mariam')    
