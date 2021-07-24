try:
    number = int(input("Enter a number : "))
    print(number)
    number = 10 / number
except ZeroDivisionError as err:
    print("Divided by zero -> " + str(err))
except ValueError as err:
    print("Invalid Input -> " + str(err))
