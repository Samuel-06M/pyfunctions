# subtraction function
def subtract_numbers(a, b):
    result = a - b
    return result

difference_result = subtract_numbers(8, 10)

print(difference_result)

# multiplication function
def multiplication(a, b):

    return a * b

result = multiplication(4, 5)
print(result)

# division function
def division(a, b):
    if b ==0:
        raise ValueError("cannot divide by zero")
    return a/b

try:
    result = division(50, 5)
    print(result)
except ValueError as e:
    print(e)


# addition function
def addition(a,b):
    return a + b
result = addition(9, 9)
print(result)