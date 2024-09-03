import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the data
df = pd.read_csv("dasma_concensus.csv")

# Ensure all population columns are numeric
cols = ['Population_2000', 'Population_2010', 'Population_2015', 'Population_2020']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# Filtering dataframes based on population thresholds
greater_than_10000_df = df[(df['Population_2000'] >= 10000) & 
                           (df['Population_2010'] >= 10000) & 
                           (df['Population_2015'] >= 10000) & 
                           (df['Population_2020'] >= 10000)]

less_than_10000_df = df[(df['Population_2000'] < 10000) & 
                        (df['Population_2010'] < 10000) & 
                        (df['Population_2015'] < 10000) & 
                        (df['Population_2020'] < 10000)]

# Plotting for Population >= 10,000
plt.figure(figsize=(10, 12))
sns.scatterplot(x='Population_2000', y='Name', data=greater_than_10000_df, label='Population 2000', color='red')
sns.scatterplot(x='Population_2010', y='Name', data=greater_than_10000_df, label='Population 2010', color='blue')
sns.scatterplot(x='Population_2015', y='Name', data=greater_than_10000_df, label='Population 2015', color='green')
sns.scatterplot(x='Population_2020', y='Name', data=greater_than_10000_df, label='Population 2020', color='purple')
plt.title('Scatter Plot of Population for Areas with Population >= 10,000')
plt.xlabel('Population')
plt.ylabel('Barangay')
plt.legend(title='Year')
plt.show()

# Plotting for Population < 10,000
plt.figure(figsize=(10, 12))
sns.scatterplot(x='Population_2000', y='Name', data=less_than_10000_df, label='Population 2000', color='red')
sns.scatterplot(x='Population_2010', y='Name', data=less_than_10000_df, label='Population 2010', color='blue')
sns.scatterplot(x='Population_2015', y='Name', data=less_than_10000_df, label='Population 2015', color='green')
sns.scatterplot(x='Population_2020', y='Name', data=less_than_10000_df, label='Population 2020', color='purple')
plt.title('Scatter Plot of Population for Areas with Population < 10,000')
plt.xlabel('Population')
plt.ylabel('Barangay')
plt.legend(title='Year')
plt.show()