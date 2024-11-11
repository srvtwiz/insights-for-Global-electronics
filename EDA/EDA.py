import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sales=pd.read_csv('data/Sales.csv',)
products=pd.read_csv('data/Products.csv')
customers=pd.read_csv('data/Customers.csv' ,encoding='ISO-8859-1')
stores=pd.read_csv('data/Stores.csv')
exchanges_rates=pd.read_csv('data/Exchange_Rates.csv')
final_df=pd.read_csv('final.csv')


# Display first few rows of each dataset
print("customers:\n", customers.head())
print("products:\n", products.head())
print("sales:\n", sales.head())
print("stores:\n", stores.head())
print("exchanges_rates:\n", exchanges_rates.head())

# Convert 'Birthday' to datetime and calculate Age
customers['Birthday'] = pd.to_datetime(customers['Birthday'], errors='coerce')
customers['Age'] = (pd.Timestamp('today') - customers['Birthday']).dt.days // 365

# Plot gender distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=customers, x='Gender')
plt.title('Gender Distribution')
plt.show()

# Plot age distribution
plt.figure(figsize=(10, 6))
sns.histplot(customers['Age'].dropna(), kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# Top 10 cities by number of customers
plt.figure(figsize=(10, 6))
customers['City'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Cities by Number of Customers')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.show()

# Calculate Profit Margin for each product
products['Profit_Margin'] = final_df['Unit Price USD'] - final_df['Unit Cost USD']

# Plot most popular products
popular_products = sales.groupby('ProductKey')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=popular_products.index, y=popular_products.values)
plt.title('Top 10 Most Popular Products')
plt.xlabel('Product Key')
plt.ylabel('Quantity Sold')
plt.show()

# Profit margin distribution
plt.figure(figsize=(10, 6))
sns.histplot(products['Profit_Margin'], bins=20, kde=True)
plt.title('Profit Margin Distribution')
plt.xlabel('Profit Margin (USD)')
plt.show()
