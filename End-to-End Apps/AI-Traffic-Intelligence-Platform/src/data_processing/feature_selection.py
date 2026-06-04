# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.ensemble import RandomForestRegressor

# Importing CSV
df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/'
                 'AI-Traffic-Intelligence-Platform/data/processed/traffic_fe.csv')

# Splitting
independent = df.drop(['region_index','congestion_level'],axis=1)
dependent = df['congestion_level']
Xtrain,Xtest,ytrain,ytest = train_test_split(independent,dependent,train_size=0.8,random_state=33)

# Encoding
for i in Xtrain.select_dtypes(['category','object']).columns.to_list():
    freq = Xtrain[i].value_counts(normalize=True)
    Xtrain[i] = Xtrain[i].map(freq)
    Xtest[i] = Xtest[i].map(freq)

# RF Feature Selection
model = RandomForestRegressor(n_estimators=100,max_depth=6,min_samples_split=8,min_samples_leaf=7,max_features=8,n_jobs=-1,random_state=33)
model.fit(Xtrain,ytrain)
best_features = model.feature_importances_
cols = independent.columns
sorty = sorted(zip(cols,best_features),key=lambda x:x[1],reverse=True)[:7]
sl,sv = zip(*sorty)

# SelectKBest Feature Selection
selector = SelectKBest(score_func=f_regression,k=7)
best_train = selector.fit_transform(Xtrain,ytrain)
all_scores = selector.scores_
top_scores = np.argsort(all_scores)[::-1][:7]
selected_features = Xtrain.columns[top_scores]
scores = all_scores[top_scores]
sorty2 = sorted(zip(selected_features,scores),key=lambda x:x[1],reverse=True)
sl2,sv2 = zip(*sorty2)

# plotting important features
fig , axes = plt.subplots(2,1,figsize=(12,8))
sns.barplot(x=sv,y=sl,ax=axes[0])
for i in axes[0].patches:
    width = i.get_width()
    if width > 0 :
        axes[0].text(width,i.get_y()+i.get_height()/2,round(width,2),ha='left',va='center',weight='bold')
axes[0].set_title('RF Feature Selection',fontweight='bold',fontsize=15)
plt.subplot(2,1,2)
sns.barplot(x=sv2,y=sl2,ax=axes[1])
for i in axes[1].patches:
    width = i.get_width()
    if width > 0 :
        axes[1].text(width,i.get_y()+i.get_height()/2,round(width),ha='left',va='center',weight='bold')
axes[1].set_title('SelectKBest Feature Selection', fontweight='bold', fontsize=15)
plt.tight_layout()
plt.show()

# Selecting Features
selected = list(set(sl)|set(sl2)|{'congestion_level'})
selected_df = df[selected]

# Saving CSV File
selected_df.to_csv('traffic_selected.csv',index=False)