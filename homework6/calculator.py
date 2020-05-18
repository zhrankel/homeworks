def concat(a,b):
    return a + b

while True:
    a = input("Enter first number: ")
    try:
        a = int(a)
    except ValueError:
        print("Sorry but enter the NUMBER please! ")
    else:
        break


while True:
    b = input("Enter second number: ")
    try:
        b = int(b)
    except ValueError:
        print("Sorry but enter the NUMBER please! ")
    else:
        break

operand = input("Enter the operand: ")

if operand == '/':
    result = a / b
    print(f"the result of {operand} is: ", result)
elif operand == '*':
    result = a * b
    print(f"the result of {operand} is: ", result)
elif operand == '-':
    result = a - b
    print(f"the result of {operand} is: ", result)
elif operand == '+':
    result = a + b
    print(f"the result of {operand} is: ", result)
