weight = int(input("Weight: "))
unit = input("(K)gs or (L)bs: ")
if unit == "K" or unit == "k":
    weight = weight * 2.2
    print(str(weight) + " pounds")
elif unit == "L" or unit == "l":
    weight = weight / 2.2
    print(str(weight) + " kilos")
else:
    print("nothing")

