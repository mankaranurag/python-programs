# while loop

counter = 1

# 1st check condition => print => counter increment => check condition => repeat
while counter <= 10:
    print(counter * counter)
    counter += 1

print("Done with while Loop")

# for loop
print("Starting For Loop")

# loops through each letters in Mankar Academy
for letter in "Mankar Academy":
    print(letter)
print()

friends = ["omkar", "prajesh", "vikas"]
for friend in friends:
    print(friend)

print()

for index in range(len(friends)):
    print(friends[index])

# [0,10)
for index in range(10):
    print(index)
print()
# [3.10)
for index in range(3, 10):
    print(index)
