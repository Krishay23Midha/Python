#Dictionaries
#used for mapping or storing something
#Eg- can store employee id's

dic = {
    435 : "Krishay",
    343 : "Harry",
    267 : "michael",
}
print(dic[435])

#or if we write like this then the output will be in the exact same order as of the keys
info = {'name' : 'krishay', 'age' : '20', 'eligible' : 'true'}
print(info)
print(info.keys()) #will give us all the keys one by one
print(info.values()) #will give us all the values one by one

for key in info.keys():
    print(info[key]) #will give us the value of the keys one by one

print(info['name'])
print(info.get('name2')) #will show us none if the key called is not present
