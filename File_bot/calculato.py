num1 = float(input("please inter the first number: "))
mod = input("please enter the mod: ")
num2 = float(input("please enter the second number: "))

if mod == '+':
    x = num1+num2
    print(x)
elif mod == '-':
    x = num1 - num2
    print(x)
elif mod == '*':
    x = num1 * num2
    print(x)
elif mod == '/':
    x = num1 / num2
    print(x)
else:
    print("invaleld")