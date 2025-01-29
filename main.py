def add(a, b):
    a = int(a)
    b = int(b)
    return a + b
    
def subtract(a,b):
    a = int(a)
    b = int(b)
    return a-b
    
def divide(a,b):
    a = int(a)
    b = int(b)
    return a/b
    
def multiply(a,b):
    a = int(a)
    b = int(b)
    return a*b
    
print("Choose one: add, subtract, multiply, divide")

choices = input()

if choices == "add":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is:", add(num1, num2))
    
if choices == "subtract":
    num1 = input ("1st number")
    num2 = input ("2nd number")
    print("the Answer is", subtract(num1,num2))
    
if choices == "divide":
    num1 =input ("1st number")
    num2 = input ("2nd number")
    print("answer:", divide(num1,num2))

if choices == "multiply":
    num1 = input ("1st number")
    num2 = input ("2nd number")
    print("Answer:", multiply(num1,num2))
    
