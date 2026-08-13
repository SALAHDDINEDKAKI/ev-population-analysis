from config import CLEANED_DATA
from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply dark theme with orange accent color for all plots in this script
plt.style.use('dark_background')
plt.rcParams['text.color'] = '#FF4500'
plt.rcParams['axes.labelcolor'] = '#FF4500'
plt.rcParams['xtick.color'] = '#FF4500'
plt.rcParams['ytick.color'] = '#FF4500'
plt.rcParams['axes.titlecolor'] = '#FF4500'

# Load the cleaned dataset
df = pd.read_csv(CLEANED_DATA)

# Count vehicles per model year
year_counts = df['model_year'].value_counts().sort_index()
print(year_counts)

# Plot the trend
plt.figure(figsize=(10, 5))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o')
plt.title("EV Registrations by Model Year")
plt.xlabel("Model Year")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.show()

# Electric range distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['electric_range'], bins=30, kde=True)
plt.title("Distribution of Electric Range")
plt.xlabel("Electric Range (miles)")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.show()

# EV type breakdown - fully electric (BEV) vs plug-in hybrid (PHEV)
plt.figure(figsize=(8, 5))
sns.countplot(data=df, y='electric_vehicle_type', order=df['electric_vehicle_type'].value_counts().index)
plt.title("BEV vs PHEV Count")
plt.xlabel("Number of Vehicles")
plt.ylabel("Vehicle Type")
plt.tight_layout()
plt.show()

# Top counties/cities by EV registrations
top_counties = df['county'].value_counts().head(10)
print(top_counties)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_counties.values, y=top_counties.index)
plt.title("Top 10 Counties by EV Registrations")
plt.xlabel("Number of Vehicles")
plt.ylabel("County")
plt.tight_layout()
plt.show()

# Correlation between model year and electric range
valid_data = df[['model_year', 'electric_range']].dropna()
corr, p_value = pearsonr(valid_data['model_year'], valid_data['electric_range'])
print(f"Correlation coefficient: {corr:.2f}")
print(f"P-value: {p_value:.4f}")

# Average electric range by year, split by vehicle type
avg_range_by_type = df.groupby(['model_year', 'electric_vehicle_type'])['electric_range'].mean()
print(avg_range_by_type)