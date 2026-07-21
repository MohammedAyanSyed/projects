# Importing Libraries
from ..data_preprocessing import Xtrain,ytrain
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import optuna
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import json
import joblib

# RF hyperparameter tuning
def objective_random_forest(trial):
    ne = trial.suggest_int('n_estimators',100,130)
    md = trial.suggest_int('max_depth',8,20)
    mss = trial.suggest_float('min_samples_split',0.3,0.7)
    msl = trial.suggest_int('min_samples_leaf',6,12)
    model = RandomForestClassifier(n_estimators=ne,max_depth=md,min_samples_split=mss,min_samples_leaf=msl,
                                   random_state=12)
    score = cross_val_score(model,Xtrain,ytrain,cv=5,scoring='roc_auc_ovr').mean()
    return score

study = optuna.create_study(direction='maximize',sampler=optuna.samplers.TPESampler())
study.optimize(objective_random_forest,n_trials=4)

# XGBoost hyperparameter tuning
def objective_xgboost(trial):
    ne = trial.suggest_int('n_estimators',100,140)
    md = trial.suggest_int('max_depth',8,20)
    ss = trial.suggest_float('subsample',0.3,0.7)
    cst = trial.suggest_float('colsample_bytree',0.6,0.8)
    lr = trial.suggest_float('learning_rate',0.01,0.1)
    rl = trial.suggest_float('reg_lambda',1.0,4.0)
    model = XGBClassifier(n_estimators=ne,max_depth=md,subsample=ss,colsample_bytree=cst,
                          learning_rate=lr,reg_lambda=rl,random_state=12)
    score = cross_val_score(model,Xtrain,ytrain,cv=5,scoring='roc_auc_ovr').mean()
    return score

study2 = optuna.create_study(direction='maximize',sampler=optuna.samplers.TPESampler())
study2.optimize(objective_xgboost,n_trials=10)

# LightBGM hyperparameter tuning
def objective_lightbgm(trial):
    ne = trial.suggest_int('n_estimators',100,160)
    md = trial.suggest_int('max_depth',8,20)
    ss = trial.suggest_float('subsample',0.3,0.7)
    cst = trial.suggest_float('colsample_bytree',0.6,0.8)
    mcs = trial.suggest_int('min_child_samples',150,500)
    lr = trial.suggest_float('learning_rate',0.01,0.1)
    rl = trial.suggest_float('reg_lambda',1.0,4.0)
    nl = trial.suggest_int('num_leaves',15,30)

    model = LGBMClassifier(n_estimators=ne,max_depth=md,subsample=ss,colsample_bytree=cst,min_child_samples=mcs,
                           learning_rate=lr,reg_lambda=rl,num_leaves=nl,random_state=12)
    score = cross_val_score(model,Xtrain,ytrain,cv=5,scoring='roc_auc_ovr').mean()
    return score

study3 = optuna.create_study(direction='maximize',sampler=optuna.samplers.TPESampler())
study3.optimize(objective_lightbgm,n_trials=10)

# Models Training
RF_model = RandomForestClassifier(**study.best_params)
RF_model.fit(Xtrain,ytrain)

XG_model = XGBClassifier(**study2.best_params)
XG_model.fit(Xtrain,ytrain)

LGB_model = LGBMClassifier(**study3.best_params)
LGB_model.fit(Xtrain,ytrain)

# Saving Models
joblib.dump(RF_model,'RF_model.pkl')
joblib.dump(XG_model,'XG_model.pkl')
joblib.dump(LGB_model,'LGB_model.pkl')

# JSON Files
values = {
    'Random Forest' : study.best_params,
    'XGBoost' : study2.best_params,
    'LightGBM' :  study3.best_params
}

with open('best_params.json','w') as f:
    json.dump(values,f,indent=3)