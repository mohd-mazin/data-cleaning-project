import pandas as pd

df = pd.read_csv("sample_dataset.csv")

# Check for missing values
print(df.isnull().sum())

# Fill missing GDP values with mean (example)
df['gdp_per_capita'] = df['gdp_per_capita'].fillna(df['gdp_per_capita'].mean())

# Drop duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Example: strip whitespace from country names
df['country'] = df['country'].str.strip()

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
