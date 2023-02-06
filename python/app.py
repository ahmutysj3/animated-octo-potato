name = input("What is your name? ")
print("Hello " + name.upper())
age = int(input("How old are you " + name + "? "))
print("I am also " + str(age) + " years old")
print("Give me two numbers and I will add them up for you")
num1 = float(input("NUMBER 1: "))
num2 = float(input("NUMBER 2: "))
total = num1 + num2
print("The answer is " + str(total))
animal = "lion"
print("Name an animal and if it is the one I am thinking then I will tell you")
animal2 = input("ANIMAL: ")
print(animal2.lower() in animal)
