# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest,f_classif

# Importing CSV File
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'Ride_Cancellation/data/Ride_FE.csv')

# Drop NUll Values
df2 = df.dropna()

# Train-Test Split
independent = df2.drop('booking_status',axis=1)
dependent = df2['booking_status']
Xtrain,Xtest,ytrain,ytest = train_test_split(independent,dependent,train_size=0.8,random_state=12)

# Encoding
o_cols = Xtrain.select_dtypes(include=['object','category']).columns.to_list()
for i in o_cols:
    freq = Xtrain[i].value_counts().to_dict()
    Xtrain[i] = Xtrain[i].map(freq)
    Xtest[i] = Xtest[i].map(freq)

# RF
rf = RandomForestClassifier(n_estimators=100,random_state=12)
rf.fit(Xtrain,ytrain)
cols = Xtrain.columns
features = rf.feature_importances_
best_features = sorted(zip(cols,features),key=lambda x : x[1],reverse=True)[:7]
sl,sv = zip(*best_features)

# SelectKBest
skb = SelectKBest(score_func=f_classif,k=7)
skb.fit_transform(Xtrain,ytrain)
all_scores = skb.scores_
top_scores = np.argsort(all_scores)[::-1][:7]
cols2 = Xtrain.columns[top_scores]
scores = all_scores[top_scores]
best_features2 = sorted(zip(cols2,scores),key=lambda x : x[1],reverse=True)
sl2,sv2 = zip(*best_features2)

# Plotting Important Features
fig,axes = plt.subplots(2,1,figsize=(12,8))
sns.barplot(x=sv,y=sl,ax=axes[0])
axes[0].set_title('RF Features Selection',fontweight='bold',fontsize=15)
plt.subplot(2,1,2)
sns.barplot(x=sv2,y=sl2,ax=axes[1])
axes[1].set_title('SelectKBest Feature Importances',fontweight='bold',fontsize=15)
plt.tight_layout()
plt.show()

# Selecting Features
sl2 = sl2[:5]
select_features = list(set(sl)|set(sl2)|{'booking_status'})
selected_features = df[select_features]

# CSV File
selected_features.to_csv('selected_features.csv',index=False)