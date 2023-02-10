print("1. global varible using global keyword")
def my_func():
  global x
  x="c++"
  print("hi " + x)
my_func()
print("hiiii " +x)
print("hiiiiiii "+x)


print("2.global variable inside and outside ")
x="car" #global variable
def a():
  x="cycle" #local varible
  print("hii "+ x)
a()
print("hiiiiii "+x)


print("3. Local variable")
def b():
  a="car" #local varible
  print(a)
b()

print("4.global,local and non local variables")

def programming():

  def python1():
    nonlocal name
    name="mrunal"

  def mean_stack():
    global name
    name="ashish"

  def java1():
    name="abhi"

  name="abhishek"

  python1()
  mean_stack()
  print("Coder is: "+name)

programming()
print(name)