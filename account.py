

# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.


class Account:

    def __init__(self,name,number):
        self.balance = 0
        self.name=name
        self.number=number
        



    def withdrawal(self,amount):
        if amount> self.balance:
            return f"Not enough money"

        elif amount <=0:
            return f"Amount must be greater than 0"    

        else :
            self.balance-=amount
            return f"Hello{self.name}you have withdawan{amount} your new balance is{self.balance}"


    # def amount(self):
    #     return f"{self.deposit} was depossited in my account for launch,but am going to take{self.withdraw} and fuel my car."

# class Account :
#     def __init__(self,name,number,balance):
#         self.name=name
#         self.number=number
#         self.balance=balance


#     def deposit(self,amount):
#         self.balance+=amount
#         return f"hello{self.name} you have deposited{self.amount} your new balance is{self.balance}"   
 
        
