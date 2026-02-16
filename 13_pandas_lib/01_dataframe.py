# A Pandas DataFrame is a two-dimensional table-like structure in Python where data is arranged in rows and columns.
# It can store different types of data such as numbers, text and dates across its columns. The main parts of a DataFrame are:
# Data: Actual values in the table.
# Rows: Labels that identify each row.
# Columns: Labels that define each data category.

import pandas as pd
import numpy as np

# Creating DataFrame using a List
lst = ['This', 'is', 'a', 'list']
df = pd.DataFrame(lst)
print(df)

# Creating DataFrame from dict of ndarray/lists
# We can create a DataFrame from a dictionary where the keys are column names and the values are lists or arrays.
# All arrays/lists must have the same length.
# If an index is provided, it must match the length of the arrays.
# If no index is provided, Pandas will use a default range index (0, 1, 2, …).
data = {'Name' : ['Vivek', 'Ashwin', 'Krish', 'Jack'],
        'Age' : [20, 30, 40, 50]}
df = pd.DataFrame(data)
print(df)

# Creating DataFrame from list of lists
data = [["Vivek", 25],
        ["Rahul", 30],
        ["Amit", 28]]
df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)

# We can perform basic operations on rows/columns like selecting, deleting, adding and renaming.
# 1. Column selection in Pandas DataFrame
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df[['Name', 'Qualification']])

# 2. Row selection in Pandas DataFrame
data = pd.read_csv("nba.csv", index_col="Name")
#df = pd.read_excel("employees.xlsx")     # to read files from excel
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
#print(data)
print(first)
print(second)

# Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame.
# It allows us to access subsets of data such as:
# Selecting all rows and some columns.
# Selecting some rows and all columns.
# Selecting a specific subset of rows and columns.
# 1. Indexing a Dataframe using indexing operator []
data = pd.read_csv("nba.csv", index_col="Name")
first = data["Age"]
print(first)

# 2. Indexing a DataFrame using .loc[ ]
data = pd.read_csv("nba.csv", index_col="Name")
avery = data.loc["Avery Bradley"]
print(avery)

#3. Indexing a DataFrame using .iloc[ ]
data = pd.read_csv("nba.csv", index_col="Name")
row2 = data.iloc[3]
print(row2)

# Missing Data can occur when no information is available for one or more items or for an entire row/column.
# In Pandas missing data is represented as NaN (Not a Number)
# 1. Checking for Missing Values using isnull() and notnull()

dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score':[30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df = pd.DataFrame(dict)
print(df.isnull())

# 2. Filling Missing Values using fillna(), replace() and interpolate()
# these function replace NaN values with some value of their own
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(dict)
print(df.fillna(0))

# 3. Dropping Missing Values using dropna()
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

df = pd.DataFrame(dict)
print(df)
print(df.dropna())     #drop rows with at least one Nan value (Null value)

# We can iterate over rows and columns to extract values or perform operations on each item.
# 1. Iterating Over Rows
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}
df = pd.DataFrame(dict)
for i, j in df.iterrows():
        print(i, j)
        print()

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for x, y in df.items():
  print(x)
  print(y)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for row in df.itertuples():
  print(row)

# 2. Iterating Over Columns
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}
df = pd.DataFrame(dict)
columns = list (df)

for i in columns:
    #print(df)
    print(df[i][2])