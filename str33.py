# Write a Python program to print the following floating numbers with no decimal places.

x = -3.1415926
y = 12.9999
print('Original Number: ', x)
print("Formatted Number: "+"{:+.0f}".format(x))
print("Original Number: ", y)
print("Formatted Number: "+"{:+.0f}".format (y))