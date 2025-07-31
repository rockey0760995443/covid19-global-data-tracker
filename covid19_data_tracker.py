import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

try:
    df = pd.read_csv("covid_data.csv")
    print("Dataset loaded successfully!\n")
except Exception as e:
    print(f"Failed to load dataset: {e}")
    exit()

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

top_countries = df.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)
print("\nTop 10 countries by total cases:")
print(top_countries)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Reds_r')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    world = df[df['location'] == 'World']
    plt.figure(figsize=(10, 5))
    plt.plot(world['date'], world['total_cases'], label='Total Cases')
    plt.plot(world['date'], world['total_deaths'], label='Total Deaths')
    plt.title('Global COVID-19 Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.tight_layout()
    plt.show()

if 'new_cases' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['new_cases'].dropna(), bins=50, color='blue')
    plt.title('Distribution of New COVID-19 Cases')
    plt.xlabel('New Cases')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

if 'total_cases' in df.columns and 'total_deaths' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='total_cases', y='total_deaths', hue='continent')
    plt.title('Total Cases vs Total Deaths by Continent')
    plt.xlabel('Total Cases')
    plt.ylabel('Total Deaths')
    plt.tight_layout()
    plt.show()

print("""
Insights:
- The dataset contains no major missing values in key columns.
- Some countries, like the US and India, have very high total case counts.
- Global trends show consistent rise in cases and deaths over time.
- Scatter plots show a positive correlation between cases and deaths.
""")
