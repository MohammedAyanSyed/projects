# Importing Libraries
import numpy as np
import pandas as pd

# Importing Dataset
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps'
                 '/AI-Traffic-Intelligence-Platform/data/processed/cleaned_dataset.csv',parse_dates=['time'])

# Hour
hour = df['time'].dt.hour
df.insert(4,'hour',hour)

# Day
day = df['time'].dt.day_name()
df.insert(5,'day',day)

# Month
month = df['time'].dt.month_name()
df.insert(6,'month',month)

# Weekend
weekend = (df['time'].dt.weekday >= 5).astype(int)
df.insert(7,'weekend',weekend)

# Rush Hours
flag = ((df['time'].dt.hour>=7) & (df['time'].dt.hour<=19)).astype(int)
df.insert(8,'rush_hours',flag)

# Time Period
cutoff = [0,6,12,17,21,24]
labels = ['late night','morning','afternoon','evening','night']
period = pd.cut(df['time'].dt.hour,bins=cutoff,labels=labels,right=False,include_lowest=True)
df.insert(9,'time_period',period)

# Speed Category
speed = [0,25,50,80,float('inf')]
speed_cat = ['low','medium','fast','high']
s_category = pd.cut(df['speed_kmh'],bins=speed,labels=speed_cat,right=False,include_lowest=True)
df.insert(11,'speed_category',s_category)

# Travel Time Category
travel_time = [0,8,15,float('inf')]
travel_category = ['fast','moderate','heavy']
t_t_category = pd.cut(df['travel_time_per_10_km_min'],bins=travel_time,labels=travel_category)
df.insert(15,'travel_time_category',t_t_category)

# CSV file
df.to_csv('traffic_fe.csv',index=False)