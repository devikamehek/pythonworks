import random
print(dir(random))
print(random.random())
print(random.randint(1,100))
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.choice("environment"))

num=[1,2,3,4,5,6]
shuf=random.shuffle(num)
print(num)