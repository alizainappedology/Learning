print("Welcome To Simple Calculator")
print("Select an operator\n 1)ADD - 2)Subtract - 3)Multiplication - 4)Division")

operator = int(input(""))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if operator == 1:
    print(num1 + num2)
    
elif operator == 2:
    print(num1 - num2)
    
elif operator == 3:
    print(num1 * num2)
    
elif operator == 4:
    print(num1 / num2)
    