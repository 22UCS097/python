age=25

if age<13:
    print("child")
elif age<20:
    print("teenager")
elif age<60:
     print("adult")
else :
    print("senior")

# Q.2


temp=input("enter age ")
age=int(temp)
day="wed"

price=12 if age>=18 else 8

if day=="wed":
    price-=2

print("ticket price fro you is $", price)

# Q.3

score=93

if score>=101:
    print("validate score")
    exit()

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")   
elif score>=60:
    print("C")
else:
    print("P")        




