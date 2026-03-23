"""
=================================================================
ADVANCED PANDAS – APPLY, MAP, TRANSFORM, LAMBDA (DEEP DIVE)
=================================================================

Covers:
1. apply() → row-wise & column-wise
2. applymap() → element-wise
3. map() → Series mapping
4. transform() → same-shape output
5. agg() → aggregation
6. pipe() → clean chaining
7. Performance rules
8. When to use what
"""

import pandas as pd
import numpy as np

print("\n================= APPLY ECOSYSTEM =================")

# ==============================================================
# 1 SAMPLE DATA
# ==============================================================

df = pd.DataFrame({
    "Name": ["Vivek", "Rahul", "Sneha", "Vivek"],
    "Math": [80, 90, 70, 85],
    "Science": [85, 95, 75, 88]
})

print("\nOriginal DataFrame:")
print(df)

# ==============================================================
# 2 apply() – COLUMN-WISE (axis=0 default)
# ==============================================================

print("\nColumn-wise apply (mean):")

print(df[["Math", "Science"]].apply(np.mean))

"""
NOTE:
axis=0 → each column is passed to function
"""

# ==============================================================
# 3 apply() – ROW-WISE (axis=1)
# ==============================================================

print("\nRow-wise apply (Total score):")

df["Total"] = df.apply(
    lambda row: row["Math"] + row["Science"],
    axis=1
)

print(df)

"""
IMPORTANT:
Row-wise apply is slower because each row is converted into a Series.
Avoid when vectorization is possible.
"""

# Better way (vectorized)
df["Total_Vectorized"] = df["Math"] + df["Science"]

# ==============================================================
# 4 apply() ON SERIES
# ==============================================================

print("\nSeries apply (Name length):")

df["Name_Length"] = df["Name"].apply(lambda x: len(x))
print(df)

"""
Series.apply() applies function to each element.
"""

# ==============================================================
# 5 applymap() – ELEMENT-WISE ON DATAFRAME
# ==============================================================

print("\napplymap example (add 5 marks):")

df_bonus = df[["Math", "Science"]].applymap(lambda x: x + 5)
print(df_bonus)

"""
applymap():
- Works only on DataFrame
- Applies function to every element
- Slower than vectorization
"""

# ==============================================================
# 6 map() – FOR SERIES ONLY
# ==============================================================

print("\nmap example (Name replacement):")

name_map = {
    "Vivek": "V",
    "Rahul": "R",
    "Sneha": "S"
}

df["Name_Short"] = df["Name"].map(name_map)
print(df)

"""
map():
- Works only on Series
- Faster than apply for simple mapping
- Can use dictionary, function, or Series
"""

# ==============================================================
# 7 transform() – SAME SHAPE OUTPUT
# ==============================================================

print("\ntransform example (group mean):")

df["Group_Mean"] = df.groupby("Name")["Total"].transform("mean")
print(df)

"""
transform():
- Returns same length as original
- Used for feature engineering
- Very important in data pipelines
"""

# ==============================================================
# 8 agg() – AGGREGATION
# ==============================================================

print("\nagg example:")

print(df.groupby("Name")[["Math", "Science"]].agg(["mean", "max"]))

"""
agg():
- Returns reduced shape
- Used for summarization
"""

# ==============================================================
# 9 pipe() – CLEAN CHAINING
# ==============================================================

print("\npipe example:")

def add_bonus(df):
    df["Bonus"] = df["Total"] * 0.1
    return df

df = df.pipe(add_bonus)
print(df)

"""
pipe():
- Passes DataFrame into custom function
- Makes method chaining clean
"""

# ==============================================================
# 10 PERFORMANCE TEST
# ==============================================================

print("\n================ PERFORMANCE TEST =================")

large_df = pd.DataFrame({
    "A": np.random.randint(1, 100, 1_000_000),
    "B": np.random.randint(1, 100, 1_000_000)
})

# Fast (vectorized)
large_df["Sum_Vectorized"] = large_df["A"] + large_df["B"]

# Slower (apply row-wise)
large_df["Sum_Apply"] = large_df.apply(
    lambda row: row["A"] + row["B"],
    axis=1
)

print("Vectorized is much faster than row-wise apply.")

# ==============================================================
# INTERNAL BEHAVIOR NOTES
# ==============================================================

"""
Why apply(axis=1) is slow?

Because:
1. Each row becomes a pandas Series
2. Python-level loop happens internally
3. Not pure C-level vectorized computation

Vectorization:
- Runs in NumPy
- Much faster
"""

# ==============================================================
# WHEN TO USE WHAT
# ==============================================================

"""
Use vectorization when possible:
    df["A"] + df["B"]

Use map():
    Simple one-column mapping

Use apply():
    Complex row logic

Use transform():
    Group-based feature engineering

Use agg():
    Summaries

Avoid:
    Loops over rows
"""

# ==============================================================
# ORDER OF PREFERENCE
# ==============================================================

'''
1 = Vectorized operations
2 = Built-in pandas functions
3 = map()
4 =  transform()
5 = apply()
6 = Loops (almost never)
'''