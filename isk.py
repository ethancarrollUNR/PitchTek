import pandas as pd

# Sample DataFrame
data = {'Column1': ['A', 'B', 'C', 'A', 'B'],
        'Column2': ['B', 'A', 'C', 'B', 'A']}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Sort values in each row to disregard the order
sorted_df = df.apply(sorted, axis=1)

# Drop rows with the same values, regardless of order
df_no_duplicates = sorted_df[~sorted_df.duplicated(keep='first')]

# Display the DataFrame without rows with the same values, regardless of order
print("\nDataFrame without rows with the same values, regardless of order:")
print(df_no_duplicates)
