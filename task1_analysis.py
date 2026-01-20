import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the 'Outputs' folder exists
os.makedirs('Outputs', exist_ok=True)

# 1. Load the Data
# Note: Adjust the encoding if you get an error (common with this dataset)
try:
    df = pd.read_csv('Dataset/superstore_sales.csv', encoding='windows-1252')
except FileNotFoundError:
    print("Error: Please make sure 'superstore_sales.csv' is inside the 'Dataset' folder.")
    exit()

# 2. Basic Data Cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.sort_values('Order Date', inplace=True)

print("Data Loaded Successfully!")
print(f"Total Records: {len(df)}")

# --- ANALYSIS 1: Sales Trends Over Time ---
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color='b')
plt.title('Monthly Sales Trend')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.savefig('Outputs/1_sales_trend.png') # Saving for your report
print("Saved: Outputs/1_sales_trend.png")

# --- ANALYSIS 2: Top 10 Products by Sales ---
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 8))
sns.barplot(y=top_products.index, x=top_products.values, palette='viridis')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Total Sales ($)')
plt.savefig('Outputs/2_top_products.png')
print("Saved: Outputs/2_top_products.png")

# --- ANALYSIS 3: Profit by Region ---
region_profit = df.groupby('Region')['Profit'].sum()

plt.figure(figsize=(8, 8))
region_profit.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='Pastel1')
plt.title('Profit Distribution by Region')
plt.ylabel('') # Hide y-label for pie chart
plt.savefig('Outputs/3_region_profit.png')
print("Saved: Outputs/3_region_profit.png")

print("\nAnalysis Complete! Check the 'Outputs' folder for your charts.")