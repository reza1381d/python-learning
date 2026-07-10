def show_info(name, age):
    print(name , age)

def square_number(a):
    return a * a

def is_even_number(b):
    return not b % 2

def calculator(a, b, operation):
    if operation == "+" :
        return a + b
    elif operation == "-" :
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "%" :
        return a % b

show_info("reza" , 23)
print(square_number(5))
print(is_even_number(24))
print(calculator(4,6,"*"))