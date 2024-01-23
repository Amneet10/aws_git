def add_two_numbers(num1, num2,num3):
    return num1 + num2 + num3

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function to add the numbers
result = add_two_numbers(num1, num2,num3)

# Display the result
print(f"The sum of {num1} , {num2}and {num3} is: {result}")

