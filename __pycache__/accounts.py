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
    def __init__(self,full_name, number):
        self.full_name =full_name
        self.number =number
        self.account_balance=0
        self.deposits=[] #Add a new attribute to the class Account called deposits which by default is an empty list.
        self.withdraws=[]  #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.transaction=100
    def deposit(self,amount):
        if amount<=0:
            return f"must be greater than 0"
        else:
            self.account_balance+=amount
            self.deposits.append({amount})
            return f"Confirmed, you have deposited {amount}. Your new balance is {self.account_balance}"
        # self.amount=1000
        # self.amount=1500
        # self.amount=7500
    def withdraw(self,amount) :
        # self.withdrawal_info = {"date": datetime,"amount":amount,"narration": self.deposit or self.withdraws}
        if amount> self.account_balance:
            return f"Insuffiecient funds"
        elif amount<=0:
            return f"must be greater than 0"
        else:
             self.account_balance -= amount + self.transaction
             self.withdraws.append({amount})
        return f"You've withdrawn {amount} your new balance is {self.account_balance}"
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)
    def current_balance(self):
        return self.account_balance
