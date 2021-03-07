# Creating an additions function that returns a value
def addition( a, b ):
    return a + b

# Creating an subtractions function that returns a value
def subtraction( a, b ):
    return a - b

# Creating an multiplication function that returns a value
def multiply( a, b ):
    return a * b

# Creating an subtractions function that returns a value
def divide( a, b ):
    if b > 0:
        return a/b
    else:
        return 0

# Creating an mod function that returns a value
def mod( a, b ):
    if b > 0:
        return a // b
    else:
        return 0

# Creating a remainder function that returns a value
def remainder( a, b ):
    if b > 0:
        return a % b
    else:
        return 0


# Main Program
a = float( input("Enter a number: "))
b = float( input("Enter another number: "))

print( a, "+", b, "=", addition(a, b))
print( a, "-", b, "=", subtraction(a, b))
print( a, "*", b, "=", multiply(a, b))
print( a, "/", b, "=", divide(a, b))
print( a, "modulus", b, "=", mod(a, b))
print( a, "remainder", b, "=", remainder(a, b))