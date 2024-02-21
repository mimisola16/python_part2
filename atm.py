import math

print("Welcome to Mimi Bank ATM , Awolowo way Ikeja")
print("********************************************")
# if and else statement
amount = int(input("Enter your amount"))
cash= {
    '1000': 0,
    '500': 0,
    '200': 0,
    '100': 0,
    '50': 0
}
# for cash in cash

cash['1000']= math.floor(amount / 1000)

remainder= amount % 1000
if remainder != 0:
 cash['500']= math.floor(remainder / 500)
 
remainder= amount % 500 
if remainder != 0:
    cash['200']= math.floor(remainder / 200) 

remainder= amount % 200 
if remainder != 0:
    cash['100']= math.floor(remainder / 100) 
    
remainder= amount % 100 
if remainder != 0:
    cash['50']= math.floor(remainder / 50)    
    
     
print("Collect your cash")
print(cash)
 
 
    
    

        