import numpy as np
import pandas as pd

# Importing Dataset
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'Ride_Cancellation/data/ride_cleaned.csv')

df['date'] = pd.to_datetime(df['date'],format='mixed')
df['time'] = pd.to_datetime(df['time'],format='%H:%M:%S')

# Hour
hour = df['time'].dt.hour
df.insert(2,'hour',hour)

# Day
day = df['date'].dt.day
df.insert(1,'day',day)

# Month
month = df['date'].dt.month
df.insert(2,'month',month)

# Day of Week
dow = df['date'].dt.weekday
df.insert(3,'day_of_week',dow)

# Weekend
weekend = (df['date'].dt.weekday >=5).astype(int)
df.insert(4,'weekend',weekend)

# Time Period
b = pd.to_datetime([5,12,15,20,24])
l = ['morning','afternoon','evening','night']
time_period = pd.cut(df['time'],labels=l,bins=b)
df.insert(7,'time_period',time_period)

# Rush Hour
rush = ((df['time'].dt.hour>=14) & (df['time'].dt.hour<=20)).astype(int)
df.insert(8,'rush_hour',rush)

# value per km
val_per_km = df['booking_value']/df['ride_distance']
df.insert(24,'booking_val_per_km',val_per_km)

# High value booking
high_value = df['booking_val_per_km'].map(lambda x : 1 if x>=25 else 0)
df.insert(26,'High_value_booking',high_value)

# long ride
long_ride = df['ride_distance'].map(lambda x : 1 if x > 40 else 0)
df.insert(27,'long_ride',long_ride)


# Dropping Columns
df.drop(['booking_id','customer_id','avg_ctat','avg_vtat','cancelled_rides_by_customer',
         'reason_for_cancelling_by_customer','cancelled_rides_by_driver','driver_cancellation_reason',
         'incomplete_rides','incomplete_rides_reason','driver_ratings','customer_rating'],axis=1,inplace=True)

# Dropping Duplicate Rows
df.drop_duplicates(inplace=True)

# CSV File
df.to_csv('Ride_FE.csv',index=False)