l=[]
def create():
    n = int(input("Enter the number numbers to add: "))
    print("Enter " + str(n) + " elements to the list")
    for i in range(1,n+1):
        l.append(int(input()))
    print("List is: ",l)

def search():
    ele=int(input("Enter the element to search: "))
    if ele in l:
        print("Found")
    else:
        print("Not Found")

def removed():
    rem=int(input("Enter the  item to get removed: "))
    if rem in l:
        l.remove(rem)
        print("New list is: ",l)
    else:
        print("Element is not found in the list")

def replace():
    replace_ele=int(input("Enter the item to replace: "))
    new_ele=int(input("Enter the new element to add: "))
    for i in range(len(l)):
        if replace_ele in l:
            l.remove(replace_ele)
            print("Removed list: ",l)
            l.append(new_ele)
            print("New element added list: ",l)


# while True:
#     opt=int(input(" 1.create\n 2.search\n 3.remove\n 4.replace\n Enter your Choice: "))
#     if opt==1:
#         create()
#     elif opt==2:
#         search()
#     elif opt==3:
#         removed()
#     elif opt==4:
#         replace()
#     else:
#         break
