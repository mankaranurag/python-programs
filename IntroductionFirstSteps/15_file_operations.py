# w -> write permissions
# a -> only append, no modification
# r -> read file permissions
# r+ -> read and write

employee_file = open("15_employees.txt", "r")

print("Check if file is readable : employee_file.readable() -> " + str(employee_file.readable()))
if employee_file.readable():
    print("File Output All at once -> ")
    print(employee_file.read())

employee_file.close()

employee_file = open("15_employees.txt", "r")
print()
if employee_file.readable():
    print("reading line by line -> ")
    print("line 1 : " + employee_file.readline().replace("\n", ""))
    print("line 2 : " + employee_file.readline().replace("\n", ""))

employee_file.close()

employee_file = open("15_employees.txt", "r")
print()
if employee_file.readable():
    print("reading lines -> ")
    print("lines : " + str(employee_file.readlines()))

employee_file.close()

# appending to a file
employee_file = open("15_employees.txt", "a")
print()
if employee_file.writable():
    employee_file.write("\nKelly - Customer Services")
employee_file.close()

# writing to a new file
employee_file = open("15_employees_1.txt", "w")
print()
if employee_file.writable():
    employee_file.write("\nKelly - Customer Services")
employee_file.close()
