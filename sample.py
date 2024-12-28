def factorial(n):
  if n<=1:
    return 1
  else:
    return n* factorial(n-1)
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial{number}}")
