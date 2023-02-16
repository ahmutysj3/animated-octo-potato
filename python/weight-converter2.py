weight = input("Weight: ")
unit = input("(K)gs or (L)bs: ")
if unit.upper() == "K":
    weight = int(weight) * 2.2
    print(str(weight) + " pounds")
elif unit.upper() == "L":
    weight = int(weight) / 2.2
    print(str(weight) + " kilos")
else: 
    print("You're dumb")
    