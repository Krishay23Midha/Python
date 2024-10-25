#Function arguments

def average(a,b):
    print('the average is', (a+b)/2)

average(4,5)
#in this case this is required arguments as the condition is already given.

def average(a = 9, b =1):
    print('the average is', (a+b)/2)
#in this case this is default arguments as the values are already given.

def average(b = 9, a =1):
    print('the average is', (a+b)/2)
#in this case this is keyword arguments as the order of the values doesn't matter.

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
        print('average is :', sum/len(numbers))

    average(5,6,7,8,9)
##in this case this is variable length arguments as we can take a number of values.
