# create a faulty calculator in which 45*3=555, 56+9=77, and 56/6=4
# except these values the calculator returns the exact values

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = input("enter the operator(*,/,+,-): ")
d = "Total: "

if a==45 and b==3 and c=="*" :
    print(d, 555)
if a==56 and b==9 and c=="+" :
    print(d, 77)
if a==56 and b==6 and c=="/" :
    print(d, 4)
elif c=="*" :
    print(d, a*b)
elif c=="+" :
    print(d, a+b)
elif c=="/" :
    print(d, a/b)
elif c=="-" :
    print(d, a-b)
else:
    print("invalid operation")
