# Importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
import joblib

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

    freq_encoding = {}
    # Encoding
    for i in o_cols:
        freq = a[i].value_counts().to_dict()
        a[i] = a[i].map(freq)
        b[i] = b[i].map(freq)
        freq_encoding[i] = freq
    c = le.fit_transform(c)
    d = le.transform(d)
    # Scaling
    a[n_cols] = ss.fit_transform(a[n_cols])
    b[n_cols] = ss.transform(b[n_cols])

    return a,b,c,d,freq_encoding,le,ss

Xtrain,Xtest,ytrain,ytest,fe,le,ss = preprocessing(w,x,y,z)

# Saving Encoding Model
joblib.dump(fe,'frequency_encoding.pkl')

# Label Encoder Model
joblib.dump(le,'l_encoder.pkl')

# Scaling Model
joblib.dump(ss,'scaling.pkl')

# Saving Columns order
joblib.dump(Xtrain.columns.to_list(),'training_columns.pkl')