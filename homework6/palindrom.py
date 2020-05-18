string = (input("Enter the string you whant to check: "))

if string[:] == string[::-1]:
    print(f"The {string} is palindrom!")
else:
    print(f"Sorry, but {string} is not palindrom")