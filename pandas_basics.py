import pandas as pd

# Load dataset
df = pd.read_csv("sample_dataset.csv")

# Basic inspection
print(df.head())        # First 5 rows
print(df.info())        # Column types, nulls
print(df.describe())    # Summary stats

# Accessing columns
print(df['country'].head())

# Indexing examples
print(df.loc[0])        # First row by label
print(df.iloc[0])       # First row by position

# Add a new column (example: score scaled to 100)
df['score_scaled'] = df['score'] * 10
print(df[['country','score','score_scaled']].head())
