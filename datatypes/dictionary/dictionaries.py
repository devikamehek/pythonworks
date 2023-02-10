n={
    "name":"devika",
    "age":25,
    "address":"muttath house",
    "course":"python django"
}
print(n)


"""accessing elements in dictionary"""
print("ACCESING ELEMENTS IN DICTIONARY")
dict1={"name":"a","age":23,"course":"python"}
print(dict1)
print(type(dict1))
print(dict1["name"])
print(dict1["course"])
x=dict1.get("name")#get method
print(x)
print(dict1.keys())#accesing keys
print(dict1.values())#accesing values
print(dict1.items())#we will get as tuples

print("changing values")
dict2={"fruit":"apple","colour":"red","rate":15}
dict2["colour"]="green"
print(dict2)
dict2.update({"colour":"grey"})#updat method also used to change values
print(dict2)
dict2["type"]="malayalam"#adding extra element
print(dict2)
dict2.update({"colour":"g","rate":34})#updating multiple elements
print(dict2)
dict2.update({"money":74})#update method used to add values
print(dict2)
dict2.update({"money":45,"fruit1":"orange"})#update multiple elemets
print(dict2)
dict2.pop("fruit1")#pop method used to remove the key:value pair
print(dict2)
dict2.popitem()#removes the last keyvalue pair
print(dict2)
del dict2["colour"]#deleting the keyvalue pair
print(dict2)


print("new dictionary")
x={"colour":"red","car":"swift","number":34}
print(x)
x.update({"place":"ekm"})
print(x)
x.clear()
print(x)
