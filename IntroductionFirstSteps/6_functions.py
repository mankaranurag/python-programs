# collection of code
# allow you to organize your code

# function that says hi to the user
# name of a function in lowercase and separated by underscore
def say_hi_to_user(name, age):
    print("Hello " + name + " from function. You are " + str(age))


print("Top")
say_hi_to_user("Anurag", 10)
say_hi_to_user("John", 30)
print("Bottom")


# return statement
def cube(num):
    return num * num * num


print(cube(3))
print(cube(4))
