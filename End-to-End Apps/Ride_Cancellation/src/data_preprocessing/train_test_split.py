import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'Ride_Cancellation/data/Ride_FE.csv')

independent = df.drop('booking_status',axis=1)
dependent = df['booking_status']

Xtrain,Xtest,ytrain,ytest = train_test_split(independent,dependent,train_size=0.8,random_state=12)