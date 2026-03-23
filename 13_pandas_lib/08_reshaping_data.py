import pandas as pd

# =========================================================
# 1 CREATE WIDE FORMAT DATA
# =========================================================

df_wide = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Jan": [100, 150, 200],
    "Feb": [200, 250, 300],
    "Mar": [300, 350, 400]
})
print("\n================ WIDE FORMAT ================")
print(df_wide)

# =========================================================
# 2 MELT (Wide → Long)
# =========================================================

df_long = pd.melt(
    df_wide,
    id_vars="Name",            # columns to keep fixed
    var_name="Month",          # new column name for former headers
    value_name="Sales"         # new column name for values
)
print("\n================ MELTED (LONG FORMAT) ================")
print(df_long)
# When to use melt?
# - Converting Excel-style wide data to analysis-ready long format
# - Required for plotting libraries
# - Required for ML feature engineering

# =========================================================
# 3 PIVOT (Long -> Wide)
# =========================================================

df_pivot = df_long.pivot(
    index="Name",
    columns="Month",
    values="Sales"
)
print("\n================ PIVOT (WIDE FORMAT) ================")
print(df_pivot)
# pivot() fails if duplicate combinations exist

# =========================================================
# 4 PIVOT_TABLE (Safe Version)
# =========================================================

# Create duplicate example
df_long_dup = df_long.copy()
df_long_dup.loc[len(df_long_dup)] = ["A", "Jan", 100]
print("\n", "TABLE WITH DUPLICATE COMBINATION:", "\n", df_long_dup)
df_pivot_table = df_long_dup.pivot_table(
    index="Name",
    columns="Month",
    values="Sales",
    aggfunc="sum"  # handles duplicates
)
print("\n================ PIVOT_TABLE (SAFE) ================")
print(df_pivot_table)

# =========================================================
# 5 STACK (Wide -> Long using index)
# =========================================================

df_stack = df_pivot.stack()
print("\n================ STACKED ================")
print(df_stack)
# stack() pushes column levels into row index
# Result is MultiIndex

# =========================================================
# 6 UNSTACK (Long -> Wide using index)
# =========================================================

df_unstack = df_stack.unstack()
print("\n================ UNSTACKED ================")
print(df_unstack)

# =========================================================
# 7 MULTI-INDEX EXAMPLE (Advanced Understanding)
# =========================================================

multi_df = df_long.set_index(["Name", "Month"])
# In case of duplicates:
# multi_df = df_long_dup.groupby(["Name", "Month"]).sum()
# print(multi_df.unstack())

print("\n================ MULTI-INDEX DATA ================")
print(multi_df)

print("\n--- UNSTACK MONTH ---")
print(multi_df.unstack())

print("\n--- STACK BACK ---")
print(multi_df.unstack().stack())

# =========================================================
# 8 ADDITIONAL IMPORTANT RESHAPING METHODS
# =========================================================

# explode() – Expand list values into rows
df_explode = pd.DataFrame({
    "Name": ["A", "B"],
    "Hobbies": [["Cricket", "Chess"], ["Music"]]
})

print("\n================ BEFORE EXPLODE ================")
print(df_explode)

print("\n================ AFTER EXPLODE ================")
print(df_explode.explode("Hobbies"))

# wide_to_long (structured reshape)
df_structured = pd.DataFrame({
    "ID": [1, 2],
    "Sales_2023": [100, 200],
    "Sales_2024": [150, 250]
})

df_long_structured = pd.wide_to_long(
    df_structured,
    stubnames="Sales",
    i="ID",
    j="Year",
    sep="_"
)
print("\n================ WIDE_TO_LONG ================")
print(df_long_structured)