

# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.


class Account:

    def __init__(self,deposit,withdraw,name,balance):
        self.deposit=deposit
        self.withdraw=withdraw
        self.name=name
        self.balance=balance

    def amount(self):
        return f"{self.deposit} was deposited in my account for launch,but am going to take{self.withdraw} and fuel my car."