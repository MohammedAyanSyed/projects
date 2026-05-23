# Importing Libraries
import numpy as np
import pandas as pd

# CSV File
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/AI-Traffic-Intelligence-Platform/data/processed/combined_df.csv')

# Null Check
nul_val = df.isnull().sum()

# Duplicate Rows
dup_rows = df.duplicated().sum()
print('Total Duplicate Rows',dup_rows)
df.drop_duplicates(inplace=True)

# Datatype Handling
df['Time'] = pd.to_datetime(df['Time'],format='%Y-%m-%dT%H:%M',errors="coerce")

# Column Standardization
df.columns = (df.columns.str.lower().str.replace('[^a-z0-9]','_',regex=True).str.replace('_+','_',regex=True)
              .str.strip('_'))

# Values Standardization
for i in df.columns:
    df[i] = df[i].astype(str).str.title().str.strip()

# Saving CSV File
df.to_csv('cleaned_dataset.csv')