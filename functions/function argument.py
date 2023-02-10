print("1. arguments passing")
def func(name):  # name is parameter
    print("Hi ",name)
func("mrunal")  # mrunal arguments/values


# print("2. calculate sum of two variables in functions")
# def sum(a,b):
#     return(a+b)
#
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# print("sum is: ",sum(a,b))

print("3. arbitrary arguments")
def sample(*name):
    print("Hi ",name)

sample("mrunal","ashish")
sample("devika","athira")

print("4. keyword arguments")
def my_func(child3,child2,child1):
    print("The youngest child is: ",child3)
    print("The first child is: ",child1)
my_func(child1="ashish",child2="mrunalsen",child3="abhi")

print("5.default parameter value")
def country(place="maradu"):
    print("Iam from "+ place)
country("india")
country("paroor")
country()

print("6. passing a list as an argument")
def func(food):
    for x in food:
        print(x)

fruits=["apple","banana","orange","pineapple"]
func(fruits)

print("7.return values")
def my_function(x):
    return 5 * x
print(my_function(4))
print(my_function(5))

print("8. positional arguments")
def my_function(msg1,msg2,msg3):
    print(msg1 +" "+msg2+" "+msg3)
my_function("hi","hi","hi")



print("9. arbitrary arguments")
def my_func(*names):
    print("hi", names ,",how are you")
my_func("jack","anjali")
my_func("mrunal")





