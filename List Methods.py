#LIST METHODS

numbers = ['1', '2', '3', '4', '5']
#if we want to insert something somewhere in the list
numbers.insert(0,6) #first the index number, then the element we want to add
print(numbers)

#if we want to add something in the end in the list
numbers.append(6)
print(numbers)

#if we want to remove something in the list
numbers.remove('3')
print(numbers)

#if we want to clear everything in the list
numbers.clear()
print(numbers)

#if we want to find something in the list , will be a boolean expression
print('1' in numbers)

#if we want to check that how many elements are there in the list
print(len(numbers))