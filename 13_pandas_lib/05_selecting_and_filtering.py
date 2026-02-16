# ================================================
# PANDAS - SELECTING AND FILTERING DATA
# ================================================

import pandas as pd

data = {
    "Name": ["Vivek", "Rahul", "Amit", "Sneha", "Priya", "Arjun", "Kiran", "Neha"],
    "Age": [25, 30, 28, 22, 35, 40, 29, 31],
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 45000, 70000, 65000, 52000, 58000]
}

df = pd.DataFrame(data)
print("\n--- FULL DATAFRAME ---")
print(df)

# =================================================
# 1 COLUMN SELECTION
# =================================================

# Select single column
print("\n--- SINGLE COLUMN (Age) ---")
print(df["Age"])
# df["Age"] returns a Series (1D)

# Select multiple columns
print("\n--- MULTIPLE COLUMNS (Name, Salary) ---")
print(df[["Name", "Salary"]])
# Double brackets return a DataFrame (2D)

# =================================================
# 2 ROW SELECTION - loc (Label Based)
# =================================================

# loc selects rows by index LABEL
print("\n--- ROW WITH INDEX 2 ---")
print(df.loc[2])

# Select multiple rows by index labels
print("\n--- ROWS 1 TO 3 ---")
print(df.loc[1:3])  # inclusive

# Select specific rows and columns
print("\n--- ROWS 1 TO 3, ONLY Name & Salary ---")
print(df.loc[1:3, ["Name", "Salary"]])

# =================================================
# 3 ROW SELECTION - iloc (Position Based)
# =================================================

# iloc selects by numerical position (like array remembering)
print("\n--- ROW AT POSITION 2 ---")
print(df.iloc[2])

# Select rows 1 to 3 (position-based)
print("\n--- ROWS POSITION 1 TO 3 ---")
print(df.iloc[1:4])  # 4 excluded (like normal Python slicing)

# Select rows and columns by position
print("\n--- ROWS 0-2 AND FIRST 2 COLUMNS ---")
print(df.iloc[0:3, 0:2])

# =================================================
# 4 BOOLEAN FILTERING
# =================================================

# Filter employees with Salary > 55000
print("\n--- SALARY > 55000 ---")
high_salary = df[df["Salary"] > 55000]
print(high_salary)
# df["Salary"] > 55000 creates True/False values
# DataFrame keeps rows where condition is True

# Filter employees Age >= 30
print("\n--- AGE >= 30 ---")
print(df[df["Age"] >= 30])

# =================================================
# 5 MULTIPLE CONDITIONS
# =================================================

# Salary > 50000 AND Department == "IT"
print("\n--- IT EMPLOYEES WITH SALARY > 50000 ---")
filtered = df[
    (df["Salary"] > 50000) &
    (df["Department"] == "IT")
]
# Always wrap each condition in parentheses
print(filtered)

# Salary > 60000 OR Age > 35
print("\n--- SALARY > 60000 OR AGE > 35 ---")
print(
    df[
        (df["Salary"] > 60000) |
        (df["Age"] > 35)
    ]
)

# NOT condition (~)
# Employees NOT in HR
print("\n--- NOT HR DEPARTMENT ---")
print(df[~(df["Department"] == "HR")])

# =================================================
# 6 USING loc WITH CONDITIONS (Cleaner Style)
# =================================================

print("\n--- CLEAN FILTER USING loc ---")
print(
    df.loc[
        (df["Salary"] > 50000) &
        (df["Department"] == "Finance"),
        ["Name", "Salary"]
    ]
)

# Format:
# df.loc[ condition , columns_to_display ]