import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder
os.makedirs("images", exist_ok=True)

# Load data
df = pd.read_csv("data/churn_data.csv")

# Convert columns
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Plot 1: Churn Distribution
plt.figure()
df['Churn'].value_counts().plot(kind='bar')
plt.title("Churn Distribution")
plt.savefig("images/churn_distribution.png")

# Plot 2: Monthly Charges vs Churn
plt.figure()
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("images/monthly_charges.png")

# Plot 3: Tenure vs Churn
plt.figure()
sns.histplot(data=df, x='tenure', hue='Churn', bins=30)
plt.title("Tenure vs Churn")
plt.savefig("images/tenure.png")

print("Plots created successfully")
