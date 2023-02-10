"""write a python script to concatenate two dict to create a new one"""

dict1={"fruit":"banana","color":"red"}
dict2={"age":12,"place":"ktm"}
print("Dictionary 1: ",dict1)
print("Dictionary 2: ",dict2)
dict1.update(dict2)
print("Concateneted Dictionary: ",dict1)

