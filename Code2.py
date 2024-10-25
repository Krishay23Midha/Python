#EXERCISE

distance = int (input("distance: "))
unit = input("(K)m or (M)ls: " )
if unit.upper() =="K":
    converted = distance / 1.6
    print("Distance in mls: " + str(converted))

else:
    converted = distance * 1.6
    print("distance in mls: " + str(converted))