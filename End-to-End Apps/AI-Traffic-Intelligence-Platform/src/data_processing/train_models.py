# Importing Libraries
import pandas as pd
from preprocessing import Xtrain_fe,Xtest_fe,ytrain_fe,ytest_fe,Xtrain_select,Xtest_select,ytrain_select,ytest_select
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score,root_mean_squared_error

# Different Model Scores
def model_building(Xtrain,Xtest,ytrain,ytest):
    results = []
    models = [LinearRegression(),RandomForestRegressor(random_state=33),XGBRegressor(random_state=33)]
    for model in models:
        model.fit(Xtrain,ytrain)
        pred = model.predict(Xtest)
        score = r2_score(ytest,pred)
        rmse = root_mean_squared_error(ytest,pred)
        results.append(
            {
                'Model' : type(model).__name__,
                'R2' : score,
                'RMSE':rmse
            }
        )
    return results

# Model for both all features data and selected features data
scores_1 = model_building(Xtrain_fe,Xtest_fe,ytrain_fe,ytest_fe)
scores_2 = model_building(Xtrain_select,Xtest_select,ytrain_select,ytest_select)

# Model Score CSV File
all_scores = scores_1 + scores_2
comparison = pd.DataFrame(all_scores)
comparison.to_csv('comparison.csv',index=False)