#!/usr/bin/env python3


def admin_login(username, password):
    password = '9999'
    username == 'Felooh'
    if username == 'Felooh' and  password == '9999':
        print(admin_login("Access granted"))
    else:
        print("Access denided")

print(admin_login("oyaa", "1234"))
    # your code here
    
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return ("It's brisk out there!")
    elif temperature > 40 and temperature < 65:
        return ("It's a little chilly out there!")
    elif temperature > 85:
        return ("It's too dang hot out there!")
    else:
        return ("It's perfect out there!")
print(hows_the_weather(88))


## I beleive I am wrong
def fizzbuzz(num):
    if num == 1:
        return "Fizz"
    elif num == 5:
        return "Buzz"
    elif num == 3 or num ==5:
        return "FizzBuzz"
    else:
        return num
    
print(fizzbuzz(23))

     # your code here
    

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Invalid operator."
print(calculator("*", 2, 3))
