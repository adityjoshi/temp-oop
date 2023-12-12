import re

# Example of using regex to find all digits in a string
input_string = "There are 3 apples and 5 oranges in the basket."

# Using regex to find all digits
digits = re.findall(r'\d', input_string)

# Printing the result
print("Digits found:", digits)
