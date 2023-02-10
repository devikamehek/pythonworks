"""Define a function that accepts roll number and returns whether the student is present or absent."""
def roll_number(num1):
    i=0
    x=[5,34,21,54,78,32,67]
    if num1 in x:
        print("Present")
    else:
        print("Absent")

num1=int(input("Enter the Roll Number: "))
roll_number(num1)
