# Find all the users who were active for 3 consecutive days or more.

# https://platform.stratascratch.com/coding/2054-consecutive-days?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
sf_events.head()
df = sf_events.sort_values(['user_id', 'record_date'])

g = df.groupby('user_id')['record_date']

prev_date = g.shift(1)
next_date = g.shift(-1)

result = df.loc[
    ((df['record_date'] - prev_date).dt.days == 1) &
    ((next_date - df['record_date']).dt.days == 1),
    'user_id'
].unique()
