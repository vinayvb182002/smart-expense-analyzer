
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("sample_expense_data.csv")

# Display basic info
print("Basic Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Total expense
total_expense = df['Amount'].sum()
print(f"\nTotal Expense: ₹{total_expense:.2f}")

# Expense by Category
category_summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("\nExpense by Category:")
print(category_summary)

# Daily Expenses
daily_summary = df.groupby('Date')['Amount'].sum()

# Visualization - Pie Chart by Category
plt.figure(figsize=(8, 6))
category_summary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Expense Distribution by Category")
plt.ylabel('')
plt.tight_layout()
plt.show()

# Visualization - Line Chart of Daily Expenses
plt.figure(figsize=(10, 5))
daily_summary.plot(kind='line', marker='o')
plt.title("Daily Expense Trend")
plt.xlabel("Date")
plt.ylabel("Amount (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()
