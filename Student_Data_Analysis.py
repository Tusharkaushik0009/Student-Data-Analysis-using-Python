import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Aman', 'Riya', 'Raj', 'Simran', None],
    'Marks': [85, 90, np.nan, 75, 88],
    'Age': [20, 21, 19, np.nan, 22]
}

df = pd.DataFrame(data)

# Display initial data
print("Original Data:\n", df)

# Handling missing values
df['Name'].fillna("Unknown", inplace=True)
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)

# Data transformation
df['Grade'] = df['Marks'].apply(lambda x: 'A' if x > 85 else 'B')

# Summary statistics
print("\nCleaned Data:\n", df)
print("\nSummary Statistics:\n", df.describe())

# Insights
avg_marks = df['Marks'].mean()
print("\nAverage Marks:", avg_marks)