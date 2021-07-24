# if else

is_male = False
is_tall = True
if is_male and is_tall:
    print("The person is tall male ")
elif is_male and not is_tall:
    print("The person is male and not Tall")
elif not is_male and is_tall:
    print("The person is not male but tall")
else:
    print("the person is not tall and not male")


# or , and , not  operators

# comparison operators

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(4, 300, 5))
