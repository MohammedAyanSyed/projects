# Importing Libraries
from pathlib import Path
import joblib
import pandas as pd
from ..data_preprocessing import Xtrain,Xtest,ytrain,ytest
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# Path
base = Path(__file__).resolve().parent.parent.parent

# Importing Models
RF = joblib.load(base / "artifacts" / "RF_model.pkl")
XGB = joblib.load(base / "artifacts" / "XG_model.pkl")
LGBM = joblib.load(base / "artifacts" / "LGB_model.pkl")

# Logistic Ensemble Model
stack = StackingClassifier(estimators=[('rf',RF),('xgb',XGB),('lgbm',LGBM)],
                           final_estimator=LogisticRegression())
stack.fit(Xtrain,ytrain)

# Model Evaluation
pred = stack.predict(Xtest)
score = accuracy_score(ytest,pred)
pre_score = precision_score(ytest,pred,average='weighted')
re_score = recall_score(ytest,pred,average='weighted')
f_score = f1_score(ytest,pred,average='weighted')

# Result CSV File
result = pd.DataFrame([{
    'model': 'Logistic Ensemble Model',
    'accuracy score' : score,
    'precision score' : pre_score,
    'recall score' : re_score,
    'f1_score' : f_score
}])
result.to_csv('ensemble_results.csv',index=False)

# Saving Model
joblib.dump(stack,'ensemble_model.pkl')