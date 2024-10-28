class person:
    name = "krishay"
    occupation = "AI"
    age = "20"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()

a.name = "chinmay"
a.occupation = "accountant"
a.age = "22"

b.name = "rahul"
b.occupation = "HR"
b.age = "23"
print(a.name, a.occupation, a.age)  #if we remove the part from a.name then it'll print the upper part, otherwise it'll print what we have specified

a.info()
b.info()
c.info() #if we don't print anything about c then it'll automatically print the default values for it

