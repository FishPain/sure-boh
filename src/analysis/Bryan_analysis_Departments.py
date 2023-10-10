import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/bryan/PycharmProjects/pythonProject/Dataset.csv")

# Convert 'fraudulent' column to boolean values
df['fraudulent'] = df['fraudulent'].map({'t': True, 'f': False})

# Count fraudulent job postings based on each department and select top 10
top_10_fraudulent_departments = df[df['fraudulent'] == True]['department'].value_counts().nlargest(10)

# Plotting a pie chart for the top 10 departments
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(top_10_fraudulent_departments.values, labels=top_10_fraudulent_departments.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Fraudulent % (Top 10 Departments)')

plt.tight_layout()
plt.show()

