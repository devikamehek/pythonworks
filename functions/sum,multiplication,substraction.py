"""Define a function that accepts 2 values and return its sum, subtraction and multiplication."""

def addition(num1,num2):
    return num1 + num2

def substraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

print("Enter the two numbers: ")
num1=int(input())
num2=int(input())

add=addition(num1,num2)
sub=substraction(num1,num2)
mul=multiplication(num1,num2)

print("Addition of 2 numbers: ",add)
print("Substraction of 2 numbers: ",sub)
print("Multiplication of 2 numbers: ",mul)


#
# """ This function calculating additon of two numbers. """
# def addition_two_numbers(num1, num2):
#     '''Calculating the sum of two numbers'''
#     return num1 + num2
#
#
# """ This function calculating subtraction of two numbers. """
# def subtraction_two_numbers(num1, num2):
#     """ Calculating the subtraction of two numbers """
#     return num1 - num2
#
#
# """ This function calculating multiplication of two numbers.  """
# def multiplication_two_numbers(num1, num2):
#     """ Calculating the multiplication of two numbers """
#     return num1*num2
#
#
# """ This function calculating division of two numbers. """
# def division_two_numbers(num1, num2):
#     """ Calculating the division of two numbers """
#     return float(num1)/float(num2)
#
#
# """ Get the input of two variables """
# print("Enter the Two Numbers:")
# num1 = int(input())
# num2 = int(input())
# """ Call Function addition_two_numbers, subtraction_two_numbers,
#      multiplication_two_numbers, and division_two_numbers with two Parameters """
# add = addition_two_numbers(num1, num2)
# sub = subtraction_two_numbers(num1, num2)
# multi = multiplication_two_numbers(num1, num2)
# division = division_two_numbers(num1, num2)
# """ Display sum, Subtraction, Multiplication, and Division of two numbers"""
# print("Addition of two Numbers is: ", add)
# print("Subtraction of two Numbers is: ", sub)
# print("Multiplication of two Numbers is: ", multi)
# print("Division of two Numbers is: ", division)