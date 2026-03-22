# ===============================================================
# DATA TRANSFORMATION & AGGREGATION
# ===============================================================

import pandas as pd

# ===============================================================
# 1 CREATE SAMPLE SALES DATASET
# ===============================================================

# Creating realistic dataset for transformation practice
data = {
    "Date": pd.to_datetime([
        "2024-01-01", "2024-01-15",
        "2024-02-01", "2024-02-10",
        "2024-03-05", "2024-03-20"
    ]),
    "Salesperson": ["Vivek", "Rahul", "Sneha", "Amit", "Vivek", "Rahul"],
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Sales": [10000, 15000, 20000, 12000, 18000, 22000]
}

df = pd.DataFrame(data)
# Extract month from date (very common in analytics)
df["Month"] = df["Date"].dt.month
print("\n================ ORIGINAL DATA ================")
print(df)

# ===============================================================
# 2 SORTING & RANKING
# ===============================================================

# Sort by Sales descending
sorted_df = df.sort_values(by="Sales", ascending=False)
print("\n================ SORTED BY SALES DESC ================")
print(sorted_df)

# Sort by multiple columns (Region ascending, Sales descending)
multi_sorted = df.sort_values(by=["Region", "Sales"], ascending=[True, False])
print("\n================ MULTI COLUMN SORT ================")
print(multi_sorted)

# Sorting DataFrame with Missing Values
data_with_nan = {"Name": ["Alice", "Bob", "Charlie", "David"],"Age": [28, 22, None, 22]}
sorted_df = pd.DataFrame(data_with_nan).sort_values(by="Age", na_position="first")
print("\n============= SORTING WITH MISSING VALUES =============")
print(sorted_df)

# Ranking Sales (dense ranking = no gaps)
df["Sales_Rank"] = df["Sales"].rank(method="dense", ascending=False)
print("\n================ RANKING ================")
print(df)
# rank(method="dense") -> 1,2,2,3
# rank(method="min") -> 1,2,2,4
# rank(method="first") -> based on appearance order

# ===============================================================
# 3 GROUPBY OPERATIONS
# ===============================================================

# Monthly revenue per region (common interview question)
monthly_region = df.groupby(["Month", "Region"])["Sales"].sum()
print("\n================ MONTHLY REVENUE PER REGION ================")
print(monthly_region)

# Multiple aggregations
agg_result = df.groupby("Region")["Sales"].agg(["sum", "mean", "max", "min"])
print("\n================ MULTIPLE AGGREGATIONS ================")
print(agg_result)

# Named aggregations (cleaner & professional)
named_agg = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Sales=("Sales", "mean"),
    Max_Sales=("Sales", "max")
)
print("\n================ NAMED AGGREGATION ================")
print(named_agg)

# transform() keeps original row count
df["Region_Total_Sales"] = df.groupby("Region")["Sales"].transform("sum")
print("\n================ TRANSFORM EXAMPLE ================")
print(df)
# Use transform when you want aggregated values but keep row-level data.

# ===============================================================
# 4 PIVOT TABLES
# ===============================================================

# pivot() reshapes data (fails if duplicates exist)
pivot_df = df.pivot(index="Month", columns="Region", values="Sales")
print("\n================ PIVOT TABLE ================")
print(pivot_df)

# pivot_table() handles duplicates + supports aggregation
pivot_table_df = df.pivot_table(
    index="Month",
    columns="Region",
    values="Sales",
    aggfunc="sum"
)
print("\n================ PIVOT_TABLE (SAFE) ================")
print(pivot_table_df)

# Crosstab (frequency table)
cross = pd.crosstab(df["Month"], df["Region"])
print("\n================ CROSSTAB ================")
print(cross)

# ===============================================================
# 5 MERGING & JOINING (CRITICAL SKILL)
# ===============================================================

# Customer dataset
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Vivek", "Rahul", "Amit", "Sneha"]
})

# Transactions dataset
transactions = pd.DataFrame({
    "CustomerID": [1, 2, 2, 3, 5],
    "Amount": [500, 700, 300, 400, 1000]
})

# INNER JOIN (only matching keys)
inner_join = pd.merge(customers, transactions, on="CustomerID", how="inner")
print("\n================ INNER JOIN ================")
print(inner_join)

# LEFT JOIN (all customers)
left_join = pd.merge(customers, transactions, on="CustomerID", how="left")
print("\n================ LEFT JOIN ================")
print(left_join)

# RIGHT JOIN (all transactions)
right_join = pd.merge(customers, transactions, on="CustomerID", how="right")
print("\n================ RIGHT JOIN ================")
print(right_join)

# OUTER JOIN (everything)
outer_join = pd.merge(customers, transactions, on="CustomerID", how="outer")
print("\n================ OUTER JOIN ================")
print(outer_join)

# Join on multiple keys
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Year": [2023, 2023, 2024],
    "Sales": [100, 200, 300]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Year": [2023, 2024, 2024],
    "Target": [150, 250, 350]
})

multi_key_join = pd.merge(df1, df2, on=["ID", "Year"], how="inner")
print("\n================ MULTI KEY JOIN ================")
print(multi_key_join)

# Debug joins using indicator
debug_join = pd.merge(customers, transactions, on="CustomerID", how="outer", indicator=True)
print("\n================ DEBUG JOIN (INDICATOR) ================")
print(debug_join)

# Set MultiIndex on both DataFrames
df1_indexed = df1.set_index(["ID", "Year"])
df2_indexed = df2.set_index(["ID", "Year"])
print("\nDF1 with MultiIndex:")
print(df1_indexed)
print("\nDF2 with MultiIndex:")
print(df2_indexed)

# Join (by index)
joined = df1_indexed.join(df2_indexed, how="inner")
print("\n================ JOIN (BY INDEX) ================")
print(joined)

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Vivek", "Rahul", "Sneha"]
}).set_index("CustomerID")

transactions = pd.DataFrame({
    "CustomerID": [1, 2, 2, 4],
    "Amount": [500, 700, 300, 900]
}).set_index("CustomerID")

# Join on index
result = customers.join(transactions, how="left")
print(result)

# Optional: Reset index to normal columns
final_result = joined.reset_index()
print("\nFinal Result After Reset Index:")
print(final_result)

# | Feature            | merge()              | join()              |
# | ------------------ | ---------------------| ------------------- |
# | Join on columns    | ✅ Direct            | ❌ Needs index      |
# | Join on index      | ✅ (left_index=True) | ✅ Default          |
# | Default join type  | inner                | left                |
# | SQL-like clarity   | ✅                   | ❌                  |
# | Multi-key join     | Very easy            | Requires MultiIndex |
# | Used in production | ⭐⭐⭐⭐            | ⭐⭐                |

# ===============================================================
# 6 CONCAT (STACKING DATA)
# ===============================================================

# Vertical concat (row stacking)
vertical_concat = pd.concat([df1, df2])
print("\n================ VERTICAL CONCAT ================")
print(vertical_concat)

# Horizontal concat (column stacking)
horizontal_concat = pd.concat([df1, df2], axis=1)
print("\n================ HORIZONTAL CONCAT ================")
print(horizontal_concat)

# ===============================================================
# 7 ADDITIONAL IMPORTANT TRANSFORMATION FUNCTIONS
# ===============================================================

# Drop duplicates
deduplicated = df.drop_duplicates()

# Value counts (frequency)
region_counts = df["Region"].value_counts()
print("\n================ VALUE COUNTS ================")
print(region_counts)

# Apply (custom transformation)
df["Sales_With_Tax"] = df["Sales"].apply(lambda x: x * 1.10)

# Map (category encoding)
region_map = {"North": 1, "South": 2}
df["Region_Code"] = df["Region"].map(region_map)
print("\n================ FINAL DATAFRAME WITH EXTRA TRANSFORMS ================")
print(df)