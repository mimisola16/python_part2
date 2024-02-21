# Raise Exception
# number = 10
# if number > 5:
#     raise Exception(f"number should not exceed 5.{number= }")
# print("Number is greater than 5")

# syntax error
# def mysyntax()
#     print("Hello class")
# mysyntax()

# AssertionError
# import sys
# assert ("linux" in sys.platform), "This code runs on linux only"

# try and accept
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as error:
#     print(f'{error}')
#     print('could not open file.log')  
    
# import sys 
# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
# print('Doing something.')
# try:
#  linux_interaction()
#  with open('file.log') as file:
#     read_data = file.read()
# except FileNotFoundError as fnf_error:
#  print(fnf_error)
# except AssertionError as error:
#  print(error)
#  print('Linux linux_interaction() function was not executed')
      
# Else clause
# def myfunc():
#     try:
#     except:
          
# Finally
def linux_interaction():
    try:
        linux_interaction()   
    except RuntimeError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        finally:
            print("cleaning up, irrespective of any exceptions.")
linux_interaction()                            
        