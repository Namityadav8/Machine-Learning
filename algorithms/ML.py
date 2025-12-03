import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('C:/Users/Namit Yadav/Downloads/final_chosen_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# 1. Gender Distribution (Bar)
# -----------------------------
plt.figure(figsize=(7,4))
df['Gender'].value_counts().plot(kind='bar', color=['skyblue', 'orange'])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# --------------------------------------
# 2. Product Category Distribution (Bar)
# --------------------------------------
plt.figure(figsize=(7,4))
df['Product Category'].value_counts().plot(kind='bar', color=['green', 'red', 'purple', 'blue'])
plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# -------------------------
# 3. Age Distribution (Hist)
# -------------------------
plt.figure(figsize=(7,4))
plt.hist(df['Age'], bins=10, color='teal')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# --------------------------------
# 4. Total Amount Distribution (Hist)
# --------------------------------
plt.figure(figsize=(7,4))
plt.hist(df['Total Amount'], bins=10, color='magenta')
plt.title("Total Amount Distribution")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------
# 5. Quantity vs Price Scatter Plot
# -----------------------------------
plt.figure(figsize=(7,4))
plt.scatter(df['Quantity'], df['Price per Unit'], color='red')
plt.title("Quantity vs Price per Unit")
plt.xlabel("Quantity")
plt.ylabel("Price per Unit")
plt.show()

# ------------------------------
# 6. Monthly Sales Trend (Line)
# ------------------------------
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total Amount'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# ------------------------------
# 7. Category-wise Total Sales (Pie Chart)
# ------------------------------
plt.figure(figsize=(7,7))
category_sales = df.groupby('Product Category')['Total Amount'].sum()
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', colors=['gold', 'lightblue', 'pink', 'lightgreen'])
plt.title("Product Category-wise Sales Contribution")
plt.show()
