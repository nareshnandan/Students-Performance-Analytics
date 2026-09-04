import pandas as pd


# Load dataset
df = pd.read_csv("data/students.csv")


# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())


# Dataset shape
print("\nDataset Shape:")
print(df.shape)


# Column names
print("\nColumn Names:")
print(df.columns)


# Data types
print("\nData Types:")
print(df.dtypes)


# Dataset information
print("\nDataset Information:")
df.info()


# Statistical summary
print("\nStatistical Summary:")
print(df.describe())