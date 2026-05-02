import pandas as pd

df = pd.read_csv("cleaned_dataset.csv")

# Top 10 happiest countries
print(df[['country','score']].sort_values(by='score', ascending=False).head(10))

# Average happiness score by region
region_avg = df.groupby('region')['score'].mean().reset_index()
print(region_avg)

# Correlation between GDP and happiness score
print(df[['gdp_per_capita','score']].corr())

# Countries with highest generosity
print(df[['country','generosity']].sort_values(by='generosity', ascending=False).head(10))

# Example visualization (optional)
import matplotlib.pyplot as plt

region_avg.plot(x='region', y='score', kind='bar', figsize=(10,5), title="Average Happiness Score by Region")
plt.show()
