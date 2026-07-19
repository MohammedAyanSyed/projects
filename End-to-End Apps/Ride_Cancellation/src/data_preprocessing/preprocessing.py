# Importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder

# CSV File
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'Ride_Cancellation/data/selected_features.csv')

# Train-Test Split
independent = df.drop('booking_status',axis=1)
dependent = df['booking_status']
w,x,y,z = train_test_split(independent,dependent,train_size=0.8,random_state=12)

# Preprocessing
def preprocessing(a,b,c,d):
    o_cols = a.select_dtypes(include=['object','category']).columns.to_list()
    n_cols = a.select_dtypes(include=['int','float']).columns.to_list()
    ss = StandardScaler()
    le = LabelEncoder()
    # Encoding
    for i in o_cols:
        freq = a[i].value_counts().to_dict()
        a[i] = a[i].map(freq)
        b[i] = b[i].map(freq)
    c = le.fit_transform(c)
    d = le.transform(d)
    # Scaling
    a[n_cols] = ss.fit_transform(a[n_cols])
    b[n_cols] = ss.transform(b[n_cols])
    return a,b,c,d

Xtrain,Xtest,ytrain,ytest = preprocessing(w,x,y,z)