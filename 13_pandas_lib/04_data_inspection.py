# ============================================
# PANDAS DATA INSPECTION
# ============================================

import pandas as pd

# --------------------------------------------
# 1 Create Sample Dataset (Simulating Real CSV)
# --------------------------------------------

data = {
    "Name": ["Vivek", "Rahul", "Amit", "Sneha", "Priya", "Arjun", "Kiran", "Neha", "Rohan", "Meera"],
    "Age": [25, 30, 28, 22, 35, 40, 29, 31, 27, 26],
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 45000, 70000, 65000, 52000, 58000, 49000, 53000],
    "Joining_Date": [
        "2020-01-15", "2019-07-10", "2021-03-22", "2022-05-18", "2018-11-30",
        "2017-09-25", "2020-12-01", "2019-04-17", "2021-06-09", "2022-02-14"
    ]
}

df = pd.DataFrame(data)

# Convert Joining_Date to proper datetime format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

# --------------------------------------------
# 2 Basic Inspection Methods
# --------------------------------------------

# View first 5 rows (default)
print("\n--- HEAD (first 5 rows) ---")
print(df.head())

# View last 5 rows
print("\n--- TAIL (last 5 rows) ---")
print(df.tail())

# View specific number of rows
print("\n--- FIRST 3 ROWS ---")
print(df.head(3))

# --------------------------------------------
# 3 Shape & Structure
# --------------------------------------------

# Shape gives (rows, columns)
print("\n--- SHAPE ---")
print(df.shape)

# Number of rows
print("\n--- NUMBER OF ROWS ---")
print(len(df))

# Column names
print("\n--- COLUMN NAMES ---")
print(df.columns)

# Index information
print("\n--- INDEX INFO ---")
print(df.index)

# Data types of each column
print("\n--- DATA TYPES ---")
print(df.dtypes)

# --------------------------------------------
# 4 Detailed Information (Very Important)
# --------------------------------------------

# Shows:
# - total rows
# - column names
# - non-null values
# - data types
# - memory usage
print("\n--- INFO() ---")
df.info()

# --------------------------------------------
# 5 Statistical Summary
# --------------------------------------------

# Describe numeric columns
print("\n--- DESCRIBE (NUMERIC) ---")
print(df.describe())

# Describe ALL columns including categorical
print("\n--- DESCRIBE (ALL COLUMNS) ---")
print(df.describe(include="all"))

# --------------------------------------------
# 6 Checking Missing Values
# --------------------------------------------

# Check missing values per column
print("\n--- MISSING VALUES COUNT ---")
print(df.isnull().sum())

# Check if any missing values exist
print("\n--- ANY MISSING VALUES? ---")
print(df.isnull().values.any())

# --------------------------------------------
# 7 Unique & Value Counts (Very Useful)
# --------------------------------------------

# Unique values in a column
print("\n--- UNIQUE DEPARTMENTS ---")
print(df["Department"].unique())

# Count unique values
print("\n--- NUMBER OF UNIQUE DEPARTMENTS ---")
print(df["Department"].nunique())

# Value counts (frequency)
print("\n--- DEPARTMENT COUNTS ---")
print(df["Department"].value_counts())

# --------------------------------------------
# 8 Sorting Data
# --------------------------------------------

# Sort by Salary ascending
print("\n--- SORT BY SALARY ASC ---")
print(df.sort_values("Salary"))

# Sort by Salary descending
print("\n--- SORT BY SALARY DESC ---")
print(df.sort_values("Salary", ascending=False))

# --------------------------------------------
# 9 Basic Filtering (Inspection Purpose)
# --------------------------------------------

# Employees with Salary > 55000
print("\n--- SALARY > 55000 ---")
print(df[df["Salary"] > 55000])

# Employees in IT department
print("\n--- IT DEPARTMENT ---")
print(df[df["Department"] == "IT"])

# --------------------------------------------
# 10 Extracting Date Information
# --------------------------------------------

# Extract year of joining
df["Joining_Month"] = df["Joining_Date"].dt.month
df["Joining_Year"] = df["Joining_Date"].dt.year
print("\n--- DATA WITH JOINING YEAR ---")
print(df)

# --------------------------------------------
# 11 Memory Usage (Important for Large Data)
# --------------------------------------------

print("\n--- MEMORY USAGE ---")
print(df.memory_usage())
print("\n--- TOTAL MEMORY USAGE (bytes) ---")
print(df.memory_usage().sum())

# --------------------------------------------
# 12 Random Sampling (Very Useful for Large Data; Randomly selects rows)
# --------------------------------------------

print("\n--- RANDOM SAMPLE (3 rows) ---")
print(df.sample(3))

# --------------------------------------------
# 13 Checking Duplicates
# --------------------------------------------

# Returns boolean Series
# True -> row is duplicate
# False -> unique
print("\n--- DUPLICATE ROWS COUNT ---")
print(df.duplicated().sum())