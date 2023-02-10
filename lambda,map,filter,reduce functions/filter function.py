"""The filter() function returns an iterator were the items are
filtered through a function to test if the item is accepted or not."""
"""syntax: filter(function, iterable)"""

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)