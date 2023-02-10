a=int(input("enter the mark of Physics: "))
b=int(input("enter the mark of Chemistry: "))
c=int(input("enter the mark of Biology: "))
d=int(input("enter the mark of Maths: "))
e=int(input("enter the mark of Computer: "))
total=((a+b+c+d+e)*100/500)
print("The total Percentage is ",total)
if(total>=90):
    print("GRADE A")
elif(total>=80):
    print("GRADE B")
elif(total>=70):
    print("GRADE C")
elif(total>=60):
    print("GRADE D")
elif(total>=50):
    print("GRADE E")
else:
    print("FAILED")


