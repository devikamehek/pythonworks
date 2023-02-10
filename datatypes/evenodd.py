i=1
n=[]
n=int(input("enter the limit:"))
even=[]
odd=[]
while(i<=n):
    if(i%2==0):
        #print("even is",i)
        even.append(i)
    else:
        odd.append(i)
    i=i+1
print("even list is",even)
print("odd list is",odd)







