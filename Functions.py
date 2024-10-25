#Functions

a = 8
b = 9
gmean1 = (a*b)/(a+b)
print(gmean1)

c = 9
d = 10
gmean2 = (c*d)/(c+d)
print(gmean2)

#instead of writing gmean everytime we can:

def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

#instead of writing greater than everytime
def isGreater(a,b):
    if(a > b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

a = 9
b = 10
if(a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")
calculategmean(a,b)

c = 9
d = 8
if(c>d):
    print("first number is greater")
else:
    print("second number is greater or equal")
calculategmean(c,d)

#instead of writing this whole code we will call it in a function

a = 8
b = 9
isGreater(a,b)
calculategmean(a,b)

#if we are defining a function but plan to write the body of the function we can simply write

def islesser(a,b):
pass