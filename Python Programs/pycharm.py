# importing the pandas library
import pandas as pd
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e','f'])}
info = pd.DataFrame(info)
print(info)
# Add a new column to an existing DataFrame object
print ("Add new column by passing series")
info['three']=pd.Series([20,40,60],index=['a','b','c'])
print (info)
print ("Add new column using existing DataFrame columns")
info['four']=info['one']+info['three']
print (info)
