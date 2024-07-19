import pandas as pd

# Load data from csv file
df = pd.read_csv('data.csv')

# Check if 'sales_6_month' column exists in the dataframe
if 'sales_6_month' in df.columns:
    # Drop 'sales_6_month' column
    df = df.drop('sales_6_month', axis=1)
else:
    print("'sales_6_month' column does not exist in the dataframe.")

# Fill NaN values
df = df.fillna(method='ffill')

# Save the cleaned dataframe to a new csv file
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head(5))