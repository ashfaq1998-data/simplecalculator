import math
print("Welcome to Simple Calculator")

def addition():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x+y
    print("The addition of ", x, " + ", y, "=", z)

def subraction():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x-y
    print("The subraction of ", x, " - ", y, "=", z)

def multiply():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x*y
    print("The multiplication of ", x, " * ", y, "=", z)

def division():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    if y == 0:
        print("The division of ", x, " / ", y, "=", "None")

    else:
        z = x/y
        print("The division of ", x, " / ", y, "=", z)

def remainder():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x%y
    print("The modulus of ", x, " % ", y, "=", z)

def power():
    x = float(input("Enter the base number: "))
    y = float(input("Enter the power number: "))
    z = pow(x,y)
    print("The power of ", x, " to the base ",y, "=",z)

def squareroot():
    x = float(input("Enter the number: "))
    z = math.sqrt(x)
    print("The square root value of ", x, " is " ,"=",z)


while True:
    print("Please enter your choice")
    print("1. Addtion + ")
    print("2. Subraction - ")
    print("3. Multiplication * ")
    print("4. Division /")
    print("5. Modulus % ")
    print("6. Power ^ ")
    print("7. Square root @")
    print("8. Evaluate expression **")
    print("9. Reset % ")
    print("10. Exit # ")

    ans = input("Please enter your choice in operator symbol: ")

    if ans == '#':
        print("See you next time Bye!!!!!")
        break

    elif ans == '+':
        addition()

    elif ans == '-':
        subraction()

    elif ans == '*':
        multiply()

    elif ans == '/':
        division()

    elif ans == '%':
        remainder()

    elif ans == '^':
        power()

    elif ans == '@':
        squareroot()

    elif ans == '**':
        x = input("Please enter the expression ")
        z = eval(x)
        print("The value for the expression is ", z)

    elif ans == '%':
        continue
