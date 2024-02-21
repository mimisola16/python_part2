class Bank:
    minimum_deposit = 25000000
   
    def __init__(self, name,ceo,cfo,cco):
        print("Welcome to "+ name +" Bank")
        print("********************************************")
        self.mgt = {
            'ceo': ceo,
            'cfo':cfo,
            'cco':cco,
        }
    def atm_machine(self,location, amount=1000 ):
        import math
        print("Branch:  "+ location)
        # if and else statement
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
            
        return cash

# mimi_bank1 = Bank("Alabian ",'Alabi','Adebayo','Ivie')
# print(mimi_bank1.atm_machine("Awoloway Ikeja", 17100)) 
# print(mimi_bank1.minimum_deposit)
# print(mimi_bank1.mgt)

# mimi_bank2 = Bank("Mayowa ",'Mayowa','Busayo','Blessing')
# print(mimi_bank2.atm_machine("Lekki Epe", 1200)) 
# print(mimi_bank2.minimum_deposit) 
# print(mimi_bank2.mgt)



def atm_machine( amount=1000):
    import math

    print("Welcome to Mimi Bank ATM , Awolowo way Ikeja")
    print("********************************************")
    # if and else statement
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
          
    return cash
    
# print(atm_machine())
# atm_machine( 1600)