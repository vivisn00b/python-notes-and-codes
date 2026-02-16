# ==========================================================
# PANDAS DATA LOADING & SAVING
# ==========================================================

import pandas as pd
import sqlite3

# ==========================================================
# 1 CREATE SAMPLE DATAFRAME (TO SAVE LATER)
# ==========================================================

data = {
    "Name": ["Vivek", "Rahul", "Amit", "Sneha"],
    "Age": [25, 30, 28, 22],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 55000, 45000]
}

df = pd.DataFrame(data)

print("\n========= ORIGINAL DATAFRAME =========")
print(df)

# ==========================================================
# 2 WRITING DATA TO FILES
# ==========================================================

# ---------------------------
# Write to CSV
# ---------------------------
df.to_csv("employees.csv", index=False)
# index=False prevents saving row index as extra column

# ---------------------------
# Write to Excel
# ---------------------------
# Requires: pip install openpyxl
df.to_excel("employees.xlsx", index=False)

# ---------------------------
# Write to JSON
# ---------------------------
df.to_json("employees.json", orient="records", indent=4)
# orient="records" → better structured JSON
# indent=4 → pretty formatting

# ==========================================================
# 3 READING DATA FROM FILES
# ==========================================================

# ---------------------------
# Read CSV
# ---------------------------
df_csv = pd.read_csv("employees.csv")
print("\n========= READ FROM CSV =========")
print(df_csv)
# Important parameters:
# pd.read_csv("file.csv", sep=",", encoding="utf-8")
# sep=";" for semicolon separated
# usecols=["Name", "Age"] to read specific columns

# ---------------------------
# Read Excel
# ---------------------------
df_excel = pd.read_excel("employees.xlsx")
print("\n========= READ FROM EXCEL =========")
print(df_excel)
# If multiple sheets:
# pd.read_excel("file.xlsx", sheet_name="Sheet1")

# ---------------------------
# Read JSON
# ---------------------------
df_json = pd.read_json("employees.json")
print("\n========= READ FROM JSON =========")
print(df_json)

# ==========================================================
# 4 WORKING WITH SQL DATABASE (SQLite Example)
# ==========================================================

# Create SQLite database connection
conn = sqlite3.connect("company.db")

# ---------------------------
# Write DataFrame to SQL
# ---------------------------
df.to_sql("employees", conn, if_exists="replace", index=False)
# if_exists options:
# "fail" → error if table exists
# "replace" → drop table and recreate
# "append" → add rows

# ---------------------------
# Read from SQL
# ---------------------------
query = "SELECT * FROM employees"
df_sql = pd.read_sql(query, conn)
print("\n========= READ FROM SQL =========")
print(df_sql)

# Close connection
conn.close()

# ==========================================================
# 5 ADVANCED & IMPORTANT PARAMETERS
# ==========================================================

# Read only specific columns
df_selected = pd.read_csv("employees.csv", usecols=["Name", "Salary"])
print("\n========= READ SELECTED COLUMNS =========")
print(df_selected)

# Read large file in chunks
print("\n========= READING IN CHUNKS =========")
chunk_iterator = pd.read_csv("employees.csv", chunksize=2)

for chunk in chunk_iterator:
    print("Chunk:")
    print(chunk)

# Specify data types while loading (very important)
df_typed = pd.read_csv(
    "employees.csv",
    dtype={
        "Age": "int64",
        "Salary": "float64"
    }
)

print("\n========= READ WITH SPECIFIED DTYPES =========")
print(df_typed.dtypes)

# Parse dates while loading
df_with_dates = pd.read_csv(
    "employees.csv",
    parse_dates=[]
)

# Example if file had joining_date column:
# parse_dates=["joining_date"]

# ==========================================================
# 6 MEMORY & PERFORMANCE TIPS
# ==========================================================

# Convert object columns to category for optimization
df["Department"] = df["Department"].astype("category")

print("\n========= MEMORY USAGE =========")
print(df.memory_usage())
print("Total Memory:", df.memory_usage().sum())

# ==========================================================
# 7 OTHER COMMON FORMATS
# ==========================================================

# Parquet (Fast & Efficient - Recommended for production)
# Requires: pip install pyarrow

# df.to_parquet("employees.parquet")
# df_parquet = pd.read_parquet("employees.parquet")


# Pickle (Python object serialization)
# df.to_pickle("employees.pkl")
# df_pickle = pd.read_pickle("employees.pkl")