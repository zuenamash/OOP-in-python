
class Student:
  

    def __init__(self,name,age,school,country,first_name,last_name):
        self.name= name
        self.age = age
        self.school = school
        self.country = country
        self.first_name= first_name
        self.last_name = last_name
        

#Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.

    def greeting(self):
        return f"Hello {self.name} from {self.country},welcome to {self.school}"

    def full_name(self) :
         return f"She go by the name {self.first_name} {self.last_name}"

    def year_of_birth(self):
         return f"She was born in {2022-23}"

    def initials(self):
        return f"This is my initials {self.first_name[0]}.{self.last_name[0]}"   



    