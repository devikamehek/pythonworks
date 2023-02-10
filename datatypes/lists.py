list1=[1,2,3,4,5,"apple",7.8]
print(list1)
print(list1[3])
print(list1[2:5])

a=['welcome',[1,3,5,7],'hi']
print(a)
print(a[0])
print(a[0][6])
print(a[1][2])
print(a[2][1])
a.append('a')
print(a)

my_list=[1,2,3,4,"welcome"]
my_list1=[1,23,"hi"]
my_list.append('hi')
print(my_list)
my_list.remove("welcome")
print(my_list)
my_list.insert(4,'jon')
print(my_list)
my_list.extend(my_list1)
print(my_list)
my_list.index(1,4)
print(my_list)
my_list.index(3)
print(my_list)

a=[3,4,"hi","a","b"]
b=a.copy()
print("b is",b)
a.pop()
print(a)

lst=[1,2,['bb','aa'],6]
lst[2].insert(0,'cc')
print(lst)

lst=[1,2,["car","a"]]
new_lst=lst.copy()
print(new_lst)

lst=[1,2,3,5]
lst.index(2)
print(lst)