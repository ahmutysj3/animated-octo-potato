weight = input("Weight: ")
unit = input("(K)gs or (L)bs: ")
if unit.upper() == "K":
    weight = float(weight) * 2.2
    print("Weight in pounds is: " + str(weight) + " pounds")
elif unit.upper() == "L":
    weight = float(weight) / 2.2
    print("Weight in kilos is: " + str(weight) + " kilos")
else: 
    print("You're dumb")
