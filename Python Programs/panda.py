import pandas as pd
info = {'one' : pd.Series([1 , 2], index= ['a','b']),
'two' : pd.Series([1 , 2, 3], index=['a', 'b','c'])}
df = pd.DataFrame(info)
print ("The DataFrame:")
print (df)
print ("Delete the first column:" )
del df['one']
print (df)
#using pop function
print ("Delete another column:")
df.pop('two')
print (df)