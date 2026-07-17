# Importing Libraries
import numpy as np
import pandas as pd

# Importing Dataset
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads'
                 '/main/End-to-End%20Apps/Ride_Cancellation/data/ride_bookings.csv')

# Null Check
null_check = df.isnull().sum()

# Fill Null Values for EDA
df.fillna({'Cancelled Rides by Customer':0,
           'Reason for cancelling by Customer':'No Customer Cancellation',
           'Cancelled Rides by Driver':0,
           'Driver Cancellation Reason':'No Driver Cancellation',
           'Incomplete Rides':0,'Incomplete Rides Reason':'Ride is Completed or Cancelled',
           'Payment Method':'No Payment'},inplace=True)

# Duplicate Rows
duplicate = df.duplicated().sum()

# Standardizing Columns
df.columns = (df.columns.str.lower().str.replace('[^0-9a-z]','_',regex=True))

# Standardizing Values
o_cols = df.select_dtypes(include=['object','category']).columns.to_list()
for i in o_cols:
    df[i] = df[i].astype(str).str.title().str.replace(' ','_').str.strip('"')

# Saving CSV File
df.to_csv('ride_cleaned.csv',index=False)