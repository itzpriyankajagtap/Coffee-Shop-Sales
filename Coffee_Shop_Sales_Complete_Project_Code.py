# ==========================================
# Coffee Shop Sales Analysis (SAFE VERSION)
# Author: Priyanka Jagtap
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# 1️⃣ Load Dataset
# ------------------------------------------

df = pd.read_csv(r"C:\Users\itzpr\OneDrive\Desktop\Uminified Mentor\Data Analyst & Data Science\Coffe Sales\index.csv")

print("Dataset Loaded Successfully ✅")

# ------------------------------------------
# 2️⃣ Basic Cleaning
# ------------------------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# ------------------------------------------
# 3️⃣ SAFE Date Conversion (No Crash Version)
# ------------------------------------------

# Convert date safely
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Convert datetime safely
if 'datetime' in df.columns:
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

# Remove only rows where datetime failed
df = df[df['datetime'].notna()]

print("After Cleaning Shape:", df.shape)

# ------------------------------------------
# 4️⃣ Feature Engineering
# ------------------------------------------

df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.to_period("M")
df['Day_Name'] = df['date'].dt.day_name()
df['Hour'] = df['datetime'].dt.hour

# ------------------------------------------
# 5️⃣ Summary Info
# ------------------------------------------

print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe())

# ------------------------------------------
# 6️⃣ Revenue by Coffee Type
# ------------------------------------------

if 'coffee_name' in df.columns and 'money' in df.columns:
    coffee_sales = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False)

    plt.figure()
    coffee_sales.plot(kind='bar')
    plt.title("Total Revenue by Coffee Type")
    plt.xlabel("Coffee Type")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.show()

# ------------------------------------------
# 7️⃣ Payment Method Pie Chart
# ------------------------------------------

if 'cash_type' in df.columns:
    payment = df['cash_type'].value_counts()

    plt.figure()
    payment.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Payment Method Distribution")
    plt.ylabel("")
    plt.show()

# ------------------------------------------
# 8️⃣ Monthly Sales Trend
# ------------------------------------------

if 'money' in df.columns:
    monthly_sales = df.groupby('Month')['money'].sum()

    plt.figure()
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.show()

# ------------------------------------------
# 9️⃣ Sales by Hour
# ------------------------------------------

hourly_sales = df.groupby('Hour')['money'].sum()

plt.figure()
hourly_sales.plot(kind='bar')
plt.title("Sales by Hour")
plt.xlabel("Hour")
plt.ylabel("Revenue")
plt.show()

# ------------------------------------------
# 🔟 Histogram
# ------------------------------------------

plt.figure()
df['money'].plot(kind='hist', bins=20)
plt.title("Sales Distribution")
plt.xlabel("Money")
plt.ylabel("Frequency")
plt.show()

print("\n🎉 Analysis Completed Successfully Without Errors!")
