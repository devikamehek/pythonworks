import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)


print("version")
import pandas as pd
print(pd.__version__)


print("series")
import pandas as pd
a=[1,2,3,5,6]
myvar=pd.Series(a)
print(myvar)