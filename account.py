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

from datetime import datetime
# now=datetime.datetime.now()

class Account:
    def __init__(self,full_name, number):
        self.full_name =full_name
        self.number =number
        self.account_balance=0
        self.deposits=[] #Add a new attribute to the class Account called deposits which by default is an empty list.
        self.withdraws=[]  #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.transaction=100
        self.words={}
        self.loan_balance=0
        self.statement=[]
    def deposit(self,amount):
      
        if amount <=0:
             print(f"Deposit must be positive amount")
        else:
            self.account_balance+=amount   
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have deposited"
            }
            self.deposits.append(amount)
            self.statement.append(transaction) 
            print(f"Hello {self.full_name}, your new balance is {self.account_balance} and your deposits are {self.deposits}and your statement is {self.statement}")
    
        return self.words            

    def withdraw(self,amount) :
        if amount+self.transaction_fee > self.loan_balance:
            print(f"Hello {self.full_name}, your balance is {self.account_balance} you can't withdraw {amount}")    
        elif amount <=0:
            print(f"Withdrawal amount must be greater than 0")
        else:    
            self.account_balance-=amount+self.transaction_fee
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have withdrawn "
            }
            self.withdraws.append(amount)
            self.statement.append(transaction)
            print(f"Hello {self.full_name}, your new balance is {self.account_balance} and the withdrawals are {self.statement}")
    def deposit_statements(self):
         for deposit in self.statement:
             print(deposit)
          
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)

    def current_balance(self):
        return self.account_balance

    def full_Statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x/%X")
            print(f"{date}:   {Narration}   {amount}")

    def borrow(self,amount):    
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03 
       
        if amount<=100:
            return "Sorry we can't give you this loan, your loan must be more than 100 "
        elif self.loan_balance>0:
            return f"Dear customer you still have a loan of {self.loan_balance}"
        elif item<10:
            return f"Your deposits must be atleast 10"

        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.loan_balance}"

        else:
            self.loan_balance+=amount
            return f"Dear customer {self.full_name} your loan of ksh{amount} has been granted successfully"

    def loan_repay(self,amount): 
        if amount<self.loan_balance:
            paying = self.loan_balance-amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan_balance
            self.loan_balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.account_balance}"  
   
    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.account_balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.loan_balance-=amount
            instance_account.loan_balance += amount
            return f"you have transfered {amount} to {instance_account} account with the name {instance_account.full_name} and your new balance is {self.account_balance}"
            


    # def borrow(self,deposit,loan_balance):
    #     if (len(deposit))>=10:
    #         return f"Yes you can proceed"
    #     elif loan_balance > 100:
    #         return f"proceed"
    #     elif loan_balance<=1/3(account_balance):


#3     Add a new method  full_statement which combines both deposits and 
# withdrawals into one list ordered by date and using a for loop prints
#  each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000
#5 Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.



    
    
