# simple calculator


def add(x, y):
    return x+y


def mult(x, y):
    return x*y


def sub(x, y):
    return x-y


def div(x, y):
    return x/y

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

ch = input("Enter your ch :")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if ch == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif ch == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

elif ch == '3':
    print(num1, "*", num2, "=", mult(num1, num2))

elif ch == '4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Invalid input")
