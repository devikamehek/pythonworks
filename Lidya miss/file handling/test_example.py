# f=open("test","r")
# print(f.read())
# for i in f:
#     print(i)
# f.close()

# print(f.read(8))


#readline method read line by line
# print(f.readline())
# print(f.readline())

# we can also read file by for loop
# for i in f:
#     print(i)


"""append"""
# f=open("test","a")
# f.write("python is an oop ")
# f.close()

#
# f=open("test","r")
# for i in f:
#     print(i)
# f.close()

#
# f=open("test","r")
# print(f.read())
# f.close()
# f=open("test","a")
# f.write("phskfgsk")
# f.close()


"""write- overrite the content"""
# f=open("test","w")
# f.write("python django")
# f.close()
# f=open("test","r")
# print(f.read())
# f.close()

"""seek method"""
# f=open("test","r")
# f.seek(4)
# print(f.readline())
# f.close()

"""tell method"""
# f=open("test","r")
# f.readline()
# pos=f.tell()
# f.close()
# print("Position is: ",pos)


"""copy"""
# from shutil import copyfile
# copyfile("test","test1")

"""print as dictionary"""
str1="cat rat mat cat pat rat cat sat cat sat"
lst=str1.split(" ")
print(lst)
d={}
for i in lst:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

