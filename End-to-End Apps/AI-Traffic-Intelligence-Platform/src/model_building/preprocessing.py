# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# CSV File
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'AI-Traffic-Intelligence-Platform/data/processed/traffic_fe.csv',parse_dates=['time'])
df_selected = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                          'AI-Traffic-Intelligence-Platform/data/processed/traffic_selected.csv')
# Splitting CSV All Features :
independent = df.drop(['congestion_level','region_label','time'],axis=1)
dependent = df['congestion_level']

# Splitting CSV Selected Features :
independent_2 = df_selected.drop('congestion_level',axis=1)
dependent_2 = df_selected['congestion_level']

# Preprocessing
def preprocessed(x,y):
    Xtrain,Xtest,ytrain,ytest = train_test_split(x,y,train_size=0.9,random_state=33)
    num_cols = Xtrain.select_dtypes(include=['int','float']).columns.to_list()
    cat_cols = Xtrain.select_dtypes(include=['object','category']).columns.to_list()

    # Encoding
    for col in cat_cols:
        freq = Xtrain[col].value_counts(normalize=True)
        Xtrain[col] = Xtrain[col].map(freq)
        Xtest[col] = Xtest[col].map(freq)

    # Scaling
    SS = StandardScaler()
    Xtrain[num_cols] = SS.fit_transform(Xtrain[num_cols])
    Xtest[num_cols] = SS.transform(Xtest[num_cols])

    return Xtrain,Xtest,ytrain,ytest

# Preprocessed Splits
Xtrain_fe,Xtest_fe,ytrain_fe,ytest_fe = preprocessed(independent,dependent)
Xtrain_select,Xtest_select,ytrain_select,ytest_select = preprocessed(independent_2,dependent_2)