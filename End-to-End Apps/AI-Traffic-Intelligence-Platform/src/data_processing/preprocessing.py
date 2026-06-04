import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'AI-Traffic-Intelligence-Platform/data/processed/traffic_fe.csv',parse_dates=['time'])
df_selected = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                          'AI-Traffic-Intelligence-Platform/data/processed/traffic_selected.csv')

# All Feature Preprocessing
# Splitting
independent = df.drop(['congestion_level','region_index','time'],axis=1)
dependent = df['congestion_level']
Xtrain_fe,Xtest_fe,ytrain_fe,ytest_fe = train_test_split(independent,dependent,train_size=0.8,random_state=33)
cat_cols = Xtrain_fe.select_dtypes(include=['object','category']).columns.to_list()
num_cols = Xtrain_fe.select_dtypes(include=['int','float']).columns.to_list()

# Encoding
for col in cat_cols:
    freq = Xtrain_fe[col].value_counts(normalize=True)
    Xtrain_fe[col] = Xtrain_fe[col].map(freq)
    Xtest_fe[col] = Xtest_fe[col].map(freq)

# Scaling
SS = StandardScaler()
Xtrain_fe[num_cols] = SS.fit_transform(Xtrain_fe[num_cols])
Xtest_fe[num_cols] = SS.transform(Xtest_fe[num_cols])

# Selected Feature Preprocessing
# Splitting
independent_selected = df_selected.drop('congestion_level',axis=1)
dependent_selected = df_selected['congestion_level']
Xtrain_select,Xtest_select,ytrain_select,ytest_select = train_test_split(independent_selected,dependent_selected,train_size=0.9,random_state=33)
cat_cols2 = Xtrain_select.select_dtypes(include=['category','object']).columns.to_list()
num_cols2 = Xtrain_select.select_dtypes(include=['int','float']).columns.to_list()
# Encoding
for col in cat_cols2:
    freq = Xtrain_select[col].value_counts(normalize=True)
    Xtrain_select[col] = Xtrain_select[col].map(freq)
    Xtest_select[col] = Xtest_select[col].map(freq)
# Scaling
Xtrain_select[num_cols2] = SS.fit_transform(Xtrain_select[num_cols2])
Xtest_select[num_cols2] = SS.transform(Xtest_select[num_cols2])