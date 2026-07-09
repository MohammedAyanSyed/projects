# Importing Libraries
from preprocessing import Xtrain_select,Xtest_select,ytrain_select,ytest_select
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import optuna
import joblib

# Training and Testing Data
Xtrain = Xtrain_select
Xtest = Xtest_select
ytrain = ytrain_select
ytest = ytest_select

# Optuna Hyperparameter Tuning
def tuning(trail):
    es = trail.suggest_int('n_estimators',250,400)
    md = trail.suggest_int('max_depth',12,25)
    mss = trail.suggest_float('min_samples_split',0.0001,0.009)
    msl = trail.suggest_int('min_samples_leaf',1,10)
    mf = trail.suggest_float('max_features',0.5,1)
    RF = RandomForestRegressor(n_estimators=es,max_depth=md,min_samples_split=mss,min_samples_leaf=msl,max_features=mf,random_state=33)
    score = cross_val_score(estimator=RF,X=Xtrain,y=ytrain,cv=5,scoring='r2').mean()
    return score

# Optuna Best Parameter
study = optuna.create_study(direction='maximize',sampler=optuna.samplers.TPESampler())
study.optimize(tuning,n_trials=5)

# Model Building
model = RandomForestRegressor(**study.best_params,random_state=33).fit(Xtrain,ytrain)

# Saving Model
joblib.dump(model, '../../artifacts/model.pkl')
