# a=[{"V":"S001"},{"V":"S002"},{"VI":"SOO1"},{"VI":"S005"},{"VII":"SOO5"},{"V":"SOO9"},{"VIII":"SOO7"}]
# b=[]
# for i in a:
#     b.extend(list(i.values()))
# b=set(b)
# print(b)


"""print unique values in dictionary"""
a=[{"V":"S001"},{"V":"S002"},{"VI":"SOO1"},{"VI":"S005"},{"VII":"SOO5"},{"V":"SOO9"},{"VIII":"SOO7"}]
b=set()
for i in a:
    for value in i.values():
        b.add(value)
print(b)

