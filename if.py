x=range(0,30)
for y in x:
    if y%3==0:
        print(y)

z=range(10,50)
for w in z:
    if w%2==0:
      print(w)
num= 5
if num>0:
    print(num,"is a positive number")
    print("This is always printed")
    #The body of if is executed only if this evaluates to True.
age = 18  
if ((age>= 18) and (age<= 18)):
    print("YOU ARE ALLOWED. WELCOME !")

    var = 'N'
if (var =='N' or var =='y'):
    print("YOU SAID YES")
a = 7
b = 9
c = 3  
if((a<b and a>c) and (a != b and a >= c)):
    print(a, " is the largest")