# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b

# Function for modulus
def modulus(a, b):
    return a % b

# Function for floor division
def floor_division(a, b):
    return a // b

# Function for exponent
def power(a, b):
    return a ** b


# Main Program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")
print("7. Power")

choice = int(input("\nEnter your choice (1-7): "))

if choice == 1:
    print("Result =", add(num1, num2))

elif choice == 2:
    print("Result =", subtract(num1, num2))

elif choice == 3:
    print("Result =", multiply(num1, num2))

elif choice == 4:
    if num2 != 0:
        print("Result =", divide(num1, num2))
    else:
        print("Division by zero is not allowed.")

elif choice == 5:
    print("Result =", modulus(num1, num2))

elif choice == 6:
    print("Result =", floor_division(num1, num2))

elif choice == 7:
    print("Result =", power(num1, num2))

else:
    print("Invalid choice!")