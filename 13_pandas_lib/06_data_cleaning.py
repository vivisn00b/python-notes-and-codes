# ============================================================
# PANDAS DATA CLEANING
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# 1 CREATE A MESSY DATASET (Simulating Real-World Data)
# ============================================================

data = {
    " Name ": [" Vivek ", "Rahul", "Amit ", "Sneha", "Priya", None, "Arjun", "Kiran", "Neha", "Rahul"],
    "Age": [25, 30, None, 22, -35, 40, 29, None, 31, 30],
    "Department ": ["IT", "HR ", "Finance", "IT", "finance", "HR", None, "IT", "Finance", "HR "],
    "Salary": [50000, 60000, 55000, None, 70000, 65000, 52000, 52000, None, 60000],
    "Joining_Date": ["2020-01-15", "2019/07/10", "2021-03-22", "invalid_date",
                     "2018-11-30", "2017-09-25", "2020-12-01",
                     None, "2021-06-09", "2019/07/10"]
}

df = pd.DataFrame(data)

print("\n================ ORIGINAL DATA ================")
print(df)

# ============================================================
# 2 CLEAN COLUMN NAMES
# ============================================================

# Remove extra spaces and standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\n================ CLEANED COLUMN NAMES ================")
print(df.columns)

# ============================================================
# 3 CLEAN STRING COLUMNS
# ============================================================

# Remove extra spaces in string columns
df["name"] = df["name"].str.strip()

# Standardize department names (lowercase)
df["department"] = df["department"].str.strip().str.lower()

print("\n================ CLEANED STRING VALUES ================")
print(df)

# ============================================================
# 4 HANDLE MISSING VALUES
# ============================================================

print("\n================ MISSING VALUES COUNT ================")
print(df.isnull().sum())

# ---- Fill missing Age with median ----
df["age"] = df["age"].fillna(df["age"].median())

# ---- Fill missing Salary with mean ----
df["salary"] = df["salary"].fillna(df["salary"].mean())

# ---- Fill missing Department with 'unknown' ----
df["department"] = df["department"].fillna("unknown")

# ---- Drop rows where Name is missing ----
df = df.dropna(subset=["name"])

print("\n================ AFTER HANDLING MISSING VALUES ================")
print(df)

# ============================================================
# 5 FIX INVALID DATA (Business Logic Cleaning)
# ============================================================

# Fix negative age values
df.loc[df["age"] < 0, "age"] = df["age"].median()

print("\n================ AFTER FIXING NEGATIVE AGE ================")
print(df)

# ============================================================
# 6 DATA TYPE CONVERSION
# ============================================================

# Convert age to integer
df["age"] = df["age"].astype(int)

# Convert salary to float (good practice)
df["salary"] = df["salary"].astype(float)

# Convert joining_date to datetime
df["joining_date"] = pd.to_datetime(df["joining_date"], errors="coerce")
# errors parameter options:
# "raise" -> default -> throw error
# "ignore" -> leave as-is
# "coerce" -> convert invalid values to NaT

df_csv = pd.read_csv("nba.csv")
ser = pd.Series(df_csv['Number']).head(10)
print("\n", "Series", "\n", ser)

print("\n================ DATA TYPES AFTER CONVERSION ================")
print(df.dtypes)
print(pd.to_numeric(ser, downcast="signed", errors="coerce"))
# errors : {‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
# ->  If ‘raise’, then invalid parsing will raise an exception
# ->  If ‘coerce’, then invalid parsing will be set as NaN
# ->  If ‘ignore’, then invalid parsing will return the input
# downcast : [default None]  If not None, and if the data has been successfully cast to a numerical dtype downcast that resulting data to the smallest numerical dtype possible according to the following rules:
# ->  ‘integer’ or ‘signed’: smallest signed int dtype (min.: np.int8)
# ->  ‘unsigned’: smallest unsigned int dtype (min.: np.uint8)
# ->  ‘float’: smallest float dtype (min.: np.float32)

# ============================================================
# 7 HANDLE INVALID DATES
# ============================================================

# Count invalid dates (NaT values)
print("\n================ INVALID DATES COUNT ================")
print(df["joining_date"].isnull().sum())

# Option: drop rows with invalid dates
df = df.dropna(subset=["joining_date"])

print("\n================ AFTER REMOVING INVALID DATES ================")
print(df)

# ============================================================
# 8 REMOVE DUPLICATES
# ============================================================

print("\n================ DUPLICATE COUNT ================")
print(df.duplicated().sum())
df = df.drop_duplicates()

print("\n================ AFTER REMOVING DUPLICATES ================")
print(df)

# ============================================================
# 9 STANDARDIZE CATEGORY VALUES
# ============================================================

# Replace inconsistent finance naming
df["department"] = df["department"].replace({
    "finance": "Finance",
    "it": "IT",
    "hr": "HR"
})

print("\n================ AFTER STANDARDIZING DEPARTMENT ================")
print(df)

# ============================================================
# 10 CREATE NEW FEATURES
# ============================================================

# Extract joining year
df["joining_year"] = df["joining_date"].dt.year

# Create salary category
df["salary_category"] = np.where(
    df["salary"] > 60000,
    "High",
    "Normal"
)

print("\n================ FINAL CLEAN DATASET ================")
print(df)

# ============================================================
# 11 FINAL DATA VALIDATION CHECK
# ============================================================

print("\n================ FINAL INFO ================")
df.info()

print("\n================ FINAL SUMMARY ================")
print(df.describe(include="all"))