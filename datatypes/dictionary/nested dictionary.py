people={1: {"name":"anjali","age":12,"sex":"female"},2:{"name":"vidya","age":23,"sex":"female"}}
print(people)
people.update({"name":"anki"})
print(people)
print(people[1]["name"])#accesing element from 3rd dictionary
print(people[2]["name"])#accesing element from 2nd dictionary
del people[2]["name"]#deleting
print(people)
print(people.get(2))
print(people.values())

"""How to change or add elements in a nested dictionary?"""

people1 = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
people1[3]={}
people1[3]["name"]="a"
people1[3]["age"]=34
people1[3]["sex"]="male"
print(people1[3])