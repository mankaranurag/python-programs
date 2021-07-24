from math import *

# comments in python
# single line
'''
This is a multiline comment
'''

character_name = "mani"
character_age = 100.24
character_is_alive = False

print("    /|There one was a spider name  " + character_name + ",")
print("   / |it was " + str(character_age) + " years old")
print("  /  |it really liked the name " + character_name + ",")
print(" /   |")

character_name = "Mike"
print("/____|thank you " + character_name)

# working with strings
print("---------------------------Working with strings")
print("Mankar\n \"Academy\" \n Escape Character \\ ")

phrase = "Mankar Academy"
print(phrase + " is cool phrase")

print("phrase Lower Case ->" + phrase.lower())
print("phrase Is Upper Check  ->" + str(phrase.upper().isupper()))
print("phrase Length ->" + str(len(phrase)))
print("phrase[0] ->" + phrase[0])
print(int(phrase.index("Acad")))
print(phrase.replace("Mankar", "Anurag"))

# working with numbers
print("---------------------------Working with numbers")
print("Add (3 + 4) -> " + str(3 + 4))
print("Subtract (3 - 4) -> " + str(3 - 4))
print("Multiply (3 * 4) -> " + str(3 * 4))
print("Divide (3 / 4) -> " + str(3 / 4))
print("Exponent (3**4) 3^4 = 3*3*3*3 -> " + str(3 ** 4))
print("Modulus (10 % 3) return remainder 10 = 3*3 + 1 -> " + str(10 % 3))
print("(3*4 + 5) -> " + str(3 * 4 + 5))
print("(3* (4 + 5)) -> " + str(3 * (4 + 5)))

print("\n********functions with numbers")
print("abs(-5) -> " + str(abs(-5)))
print("pow(2,4) 2 raised to power 4, 2*2*2*2 -> " + str(pow(2, 4)))
print("max(4,8) -> " + str(max(4, 8)))
print("min(4,8) -> " + str(min(4, 8)))
print("round(3.2) -> " + str(round(3.2)))
print("round(3.5) -> " + str(round(3.5)))
print("round(3.7) -> " + str(round(3.7)))

print("floor(3.7) -> " + str(floor(3.7)))
print("ceil(3.2) -> " + str(ceil(3.2)))
print("sqrt(36) -> " + str(sqrt(36)))

# Getting Input From Users
print("---------------------------Getting Input From Users")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!\n You are " + age)
