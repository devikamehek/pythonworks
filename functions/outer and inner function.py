"""calculate an inner function to calculate the addition in the following way
* create an outer function that accept two parameters a and b
* create an inner function inside an outer function that will calculate the addition of a and b
* at last an outer function will add 5 into addition and return it"""

# def calculator(a,b):
#     def addition():
#         c=a+b
#         return c
#     return addition()+5
# print("Total: ",calculator(4,4))


# def calculator(a,b):
#     def addition():
#         c=a+b
#         return c
#     return addition()+5
#
#
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# print("adding 5 to the sum")
# print("Total: ",calculator(a,b))

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add

func=test(4)
print(func(8))
