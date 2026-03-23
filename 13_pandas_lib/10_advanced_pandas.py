import pandas as pd
import numpy as np

# ==============================================================
# 1 WORKING WITH DATES & TIME
# ==============================================================

print("\n================= DATES & TIME =================")

df = pd.DataFrame({
    "Date": ["2024-01-01", "2024-01-02", "2024-02-01", "2024-03-01"],
    "Sales": [100, 150, 200, 250]
})

# Convert string to datetime
df["Date"] = pd.to_datetime(df["Date"])
print("\nConverted to datetime:")
print(df)

# Extract components
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

print("\nExtracted Year / Month / Day:")
print(df)

# Time difference
df["Days_Diff"] = df["Date"].diff()
print("\nDate Difference:")
print(df)

# Set Date as index for time-based operations
df.set_index("Date", inplace=True)
# Normally, pandas functions create a new modified copy, does NOT change the original DataFrame
# But When You Use inplace=True, the original df is modified directly
# No new DataFrame is returned, the function returns None

# Resampling (monthly aggregation)
monthly_sales = df["Sales"].resample("ME").sum()
# resample() is basically GROUP BY time intervals
# It only works when your index is a DatetimeIndex
print("\nResampled Monthly Sales:")
print(monthly_sales)

# Sample time-series data
data = {
    'date': pd.date_range('2023-01-01', periods=10, freq='D'),
    'sales': [200, 220, 250, 230, 210, 300, 280, 270, 260, 240]
}
df2 = pd.DataFrame(data)
print("\n", "time-series data:","\n", data)
resampled_data = df2.resample('W', on='date').agg({'sales': ['sum', 'mean']})
# specify a datetime column using 'on' when index is not a DatetimeIndex
print("\n", "time-series resampled data:","\n", resampled_data)

# DOWNSAMPLING Example (Daily to Monthly):
monthly_sales = df2.resample("ME", on='date').sum()
# specify a datetime column using 'on' when index is not a DatetimeIndex
print("\n", "Monthly data:","\n", monthly_sales)

# UPSAMPLING Example (Daily to Hourly):
df2 = df2.set_index("date")
# Upsampling from on= selection is not supported, use .set_index() to explicitly set index to datetime-like
hourly_sales = df2.resample("h").ffill()
# upsampling to hourly data and forward filling missing values
# ffill() = “forward fill.” When you upsample, new timestamps are created without data.
# ffill() fills these gaps using the last known value.
# similarly, bfill() (Backward Fill) = fills missing values with the next known value.
# interpolate() = fills missing data using interpolation
print("\n", "Hourly data:","\n", hourly_sales)

# Time-based slicing
print("\nTime-based filtering (Feb 2024):")
print(df.loc["2024-02"])

# ==============================================================
# 2 MULTI-INDEX (Hierarchical Index)
# ==============================================================

print("\n================= MULTIINDEX =================")

data = {
    "Region": ["North", "North", "South", "South"],
    "Month": ["Jan", "Feb", "Jan", "Feb"],
    "Sales": [100, 150, 200, 250]
}

df_multi = pd.DataFrame(data)

# Create MultiIndex
df_multi.set_index(["Region", "Month"], inplace=True)
print("\nMultiIndex DataFrame:")
print(df_multi)

# Access specific level
print("\nAccess North region:")
print(df_multi.loc["North"])

# Reset index
df_reset = df_multi.reset_index()
print("\nAfter reset_index():")
print(df_reset)

# ==============================================================
# 3 WINDOW FUNCTIONS
# ==============================================================

print("\n================= WINDOW FUNCTIONS =================")

df_window = pd.DataFrame({
    "Sales": [100, 200, 300, 400, 500]
})

# Rolling window (moving average of last 2 values)
df_window["Rolling_Mean"] = df_window["Sales"].rolling(window=2).mean()

# Expanding window (cumulative mean)
df_window["Expanding_Mean"] = df_window["Sales"].expanding().mean()

# Cumulative sum
df_window["Cumulative_Sum"] = df_window["Sales"].cumsum()

print(df_window)

# ==============================================================
# 4 PERFORMANCE OPTIMIZATION
# ==============================================================

df_perf = pd.DataFrame({
    "A": np.random.randint(1, 100, 1000000),
    "B": np.random.randint(1, 100, 1000000)
})

# Vectorized operation (FAST)
df_perf["Sum_Vectorized"] = df_perf["A"] + df_perf["B"]

# Avoid this (SLOW)
# df_perf["Sum_Apply"] = df_perf.apply(lambda row: row["A"] + row["B"], axis=1)

# Memory optimization using categorical dtype
df_mem = pd.DataFrame({
    "Category": ["A", "B", "A", "C", "B"] * 10000
})
print("\nMemory before categorical:")
print(df_mem.info())

df_mem["Category"] = df_mem["Category"].astype("category")
print("\nMemory after categorical:")
print(df_mem.info())

# Optimizing memory usage by downcasting data types
print ("Before downcasting: ", df_perf.info(memory_usage="deep"))
df_perf["A"] = pd.to_numeric(df_perf["A"], downcast="integer") # Pandas automatically picks smallest possible integer types among int8, int16, int32, int64

print("After downcast optimization:", df_perf.info(memory_usage="deep"))

# ==============================================================
# CHUNKING LARGE FILES
# ==============================================================

for chunk in pd.read_csv("nba.csv", chunksize=10000):
    print(chunk.head())

# ==============================================================
# EXTRA IMPORTANT CONCEPTS
# ==============================================================

# 1 Vectorized string operations
df_str = pd.DataFrame({"Name": ["vivek", "rahul", "sneha"]})
df_str["Upper"] = df_str["Name"].str.upper()
print("\nString vectorization:")
print(df_str)

# 2 Query (clean filtering syntax)
df_query = pd.DataFrame({
    "Age": [20, 25, 30],
    "Salary": [30000, 50000, 70000]
})
print("\nQuery example:")
print(df_query.query("Age > 22 and Salary > 40000"))

# 3 Assign (clean pipeline style)
df_assign = df_query.assign(
    Bonus=lambda x: x["Salary"] * 0.10
)
print("\nAssign example:")
print(df_assign)