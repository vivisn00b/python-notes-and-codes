# Pandas Series is a one-dimensional labeled array that can hold data of any type (integer, float, string, Python objects, etc.).
# It is similar to a column in an Excel spreadsheet or a database table.
# It supports integer-based and label-based indexing.
# It stores heterogeneous data types.

import pandas as pd
import numpy as np

# Creating a Pandas Series
data = [1, 2, 3, 4]
ser = pd.Series(data)
print(ser)

# Elements of series can be accessed using two ways:
# Position-based Indexing - We use numerical positions similar to lists in Python.
# Label-based Indexing - This method also custom index labels assigned to elements.
# 1. Position-based Indexing
data = np.array(['v','i','v','e','k'])
ser = pd.Series(data)
print(ser[:3])

# 2. Label-based Indexing
data = np.array(['v','i','v','e','k'])
ser = pd.Series(data, index=[10,11,12,13,14])
print(ser[10], ser[11], ser[12])

#  Indexing can also be known as Subset Selection.
#  .iloc[] is used for position-based selection and .loc[] for label-based selection.
# 1. Indexing a Series using .loc[]
df = pd.read_csv("nba.csv")
ser = pd.Series(df['Name'])
data = ser.head(10)
print(data)
print(data.loc[3:9])

# 2. Indexing a Series using .iloc[]
df = pd.read_csv("nba.csv")
ser = pd.Series(df['Name'])
data = ser.head(10)
print(data)
print(data.iloc[3:6])

# Pandas allows performing binary operations on Series, such as addition, subtraction, multiplication and division.
# These operations can be performed using functions like .add() , .sub(), .mul() and .div().
ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
df_sum = ser1.add(ser2)
print(df_sum)

# Conversion operations allow transforming data types within a Series. This can be useful for ensuring consistency in data types.
# In order to perform conversion operation we have various function which help in conversion like .astype(), .tolist() etc
ser = pd.Series([1, 2, 3, 4])
ser = ser.astype(float)
print(ser)

s = pd.Series([1, "hello", 3.14, True, np.nan])
a = s.tolist()
print(a)