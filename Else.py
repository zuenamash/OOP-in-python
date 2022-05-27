x=range(10,20)
for y in x:
    if y%3==0:
       print(f"{y} Is an odd number")
    else:
           print(f"{y} Is an even number")

           i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")

num=3
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

#     A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
print="Enter salary"
salary=input("Two thousand")
print="Year of service"
yearofservice=input("three")
if yearofservice >5:
    print("Get bonuses")
else:
    print("No Bonuses")