list_example = ["omkar", 2, 2.334, False, ["aaa", 'bb']]
friends = ["omkar", "vikas", "prajesh", "oscar", "toby"]

print("printing list :                      " + str(friends))
# from front index position starts at 0
# from back index position starts at -1
print("printing value in list from front : friends[1] -> " + friends[1])
print("printing value in list from back : friends[-1] -> " + friends[-1])

print("printing values in list starting from position 1 : friends[1:] -> " + str(friends[1:]))
print("printing values in list from 1 to 3m this would be like [1,3) : friends[1:3] -> " + str(friends[1:3]))

friends[1] = "Mike"
print("changing a element in list friends[1] = \"Mike\". Printing friends[1] -> " + friends[1])

print("\n***** List Functions")
lucky_numbers = [4, 6, 7, 23, 4443, 234, 345]

print("friends list -> ", str(friends))
print("lucky_numbers list -> ", str(lucky_numbers))

friends.extend(lucky_numbers)
print("Extend Function (appends 2 lists) : friends.extend(lucky_numbers), printing friends list -> ", str(friends))

friends.append("Anurag")
print("Append Function (appends the value) : friends.append(\"Anurag\"), printing friends list -> ", str(friends))

friends.insert(1, "JohnD******")
print(
    "Insert Function (inserts the value at the index) : friends.insert(1, \"JohnD******\"), printing friends list -> ",
    str(friends))

friends.remove("JohnD******")
print("Remove Function (removes the value) : friends.remove(\"JohnD******\"), printing friends list -> ", str(friends))

popped = friends.pop()
print("Pop Func-tion (removes the value at position -1) : friends.pop(), printing friends list -> ", str(friends),
      " , Popped Value is ->  ", popped)

print("Index Function (returns the index of  the value) : friends.index(\"oscar\"), printing index -> ",
      friends.index("oscar"))

friends.clear()
print("Clear Function (removes all the values) : friends.clear(), printing friends list -> ", str(friends))

lucky_numbers.sort()
print("\nSort Function (sorts the list) : lucky_numbers.sort(), printing lucky_numbers list -> ", str(lucky_numbers))

lucky_numbers.reverse()
print("Reverse Function (reverses the list) : lucky_numbers.reverse(), printing lucky_numbers list -> ",
      str(lucky_numbers))

lucky_numbers2 = lucky_numbers.copy()
print("Copy Function (creates a copy the list) : lucky_numbers.copy(), printing lucky_numbers2 list -> ",
      str(lucky_numbers2))

# similar functinons include
# friends.count("omkar") -> returns the count  of number of elements of omkar
# friends.sort() -> sorts the list in alphbetical order
