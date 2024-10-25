#Dictionary methods
#like lists and sets

ep1 = {122 : 56, 234 : 68, 345 : 49, 432 : 69}
ep2 = {231 : 76, 342 : 90}
ep1.update(ep2)
print(ep1)

ep1.pop(122)
print(ep1)

ep1.popitem()
print(ep1)

ep1.clear()
print(ep1)

del ep1[122]
print(ep2)
