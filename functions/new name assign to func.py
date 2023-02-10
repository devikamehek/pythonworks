"""Assign a different name to function and call it through the new name"""

def fruits(name,price):
    print(name,price)

#call it using the original name
fruits("apple",34)

#assign new name
fruits_Rate=fruits

#call using new name
fruits_Rate("orange",43)

