# Libraries
import numpy as np
import pandas as pd

# CSV File
df = pd.read_csv('https://raw.githubusercontent.com//MohammedAyanSyed//projects//refs//'
                  'heads//main//End-to-End%20Apps//Airbnb_User_Destination//data//train_users_2.csv')
shape = df.shape

# Null Check
nul_val = df.isnull().sum()

# Duplicate Check
dup_rows = df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Datatype Handling
df['date_account_created'] = pd.to_datetime(df['date_account_created'],format='mixed',errors='coerce')
df['timestamp_first_active'] = pd.to_datetime(df['timestamp_first_active'].astype(str),format='%Y%m%d%H%M%S')
df['date_first_booking'] = pd.to_datetime(df['date_first_booking'],format='mixed',errors='coerce')

# Columns Standardizing
df.columns = (df.columns.str.lower().str.replace('[^a-z0-9]','_',regex=True).str.strip())

# Values Standardizing
cols = df.select_dtypes(include=['object','category']).columns.to_list()
for col in cols:
    df[col] = df[col].astype(str).str.title().str.strip()

# Saving CSV File
df.to_csv('Cleaned.csv',index=False)
