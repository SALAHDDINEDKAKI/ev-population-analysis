from config import RAW_DATA, CLEANED_DATA
import pandas as pd

# load the raw dataset
df = pd.read_csv(RAW_DATA)
print(f"Raw dataset loaded from {RAW_DATA}")

# Explore the dataset
print(df.shape)
print(df.columns)
print(df.head())

# Check data types & missing values
print(df.info())

print(df.isnull().sum())

# Check for duplicates
print(df.duplicated().sum())

# Drop duplicates if any exist
df = df.drop_duplicates()

# Check unique values in key categorical columns
print(df['Make'].unique())
print(df['Model Year'].unique())

# Clean column names: lowercase, no spaces
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Confirm the new column names
print(df.columns)

# Save the cleaned dataset
df.to_csv(CLEANED_DATA, index=False)
print(f"Cleaned dataset saved to {CLEANED_DATA}")