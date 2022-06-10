# Conditions for withdrawal to be succesiful
# Requested amount must be greater than amount balance


# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.



class Account:

    def __init__(self,name,balance,number):
        self.number=number
        self.name=name
        self.balance=balance
        self.deposits=[]
        self.withdraw=[]

    def deposit(self,amount):
        if amount< 0:
           return f"Hello your deposited amount {amount} this is your new balance {self.balance}"    
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"You have deposited {amount}. Your new balance is {self.balance}"
   
    def withdrawal(self,amount):
        if amount> self.balance:
            return f"Not enough money"

        elif amount <=0:
            return f"No money"    

        else :
            self.withdrawal-=amount
            return f"Hello{self.name}you have withdawan{amount} your new balance is{self.balance}"

      
    def deposits_statement(self):
          print(*self.deposits, sep="\n")  
         
    def withdrawals_statement(self):
        print(*self.withdrawals, sep="\n")      