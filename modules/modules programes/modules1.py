"""write a program to generate a random color hex, a random alphabetical string ,random value
between 2 integers,and random multiple of 7 between 0 and 70.
hint: use random.randint()"""

print("1.random colour hex")
import random
print(random.randint(0,0xFFFFFF))
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))

rand=random.randint(0,16777215)
hex_num=str(hex(rand))
hex_num='#'+hex_num[2:]
print(hex_num)

print("2. A random alphabetical String")
import string
import random

# initializing size of string
N = 7

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits,k=N))
# print result
print("The generated random string : " + str(res))



print("another method")
max_length = 255
s = ""
for i in range(random.randint(1, max_length)):
    s += random.choice(string.ascii_letters)
print(s)


print("3.Random value between 2 integrs")
import random
print(random.randint(1,9))
print(random.randint(-7,7))





print("4.Random multiple to 7 between 0 and 70")
import random
print(random.randint(0,10)*7)
