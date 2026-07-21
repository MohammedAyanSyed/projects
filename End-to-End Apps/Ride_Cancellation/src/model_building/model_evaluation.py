# Importing Libraris
import pandas as pd
import joblib
from pathlib import Path
from ..data_preprocessing import Xtest,ytest
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Path
base = Path(__file__).resolve().parent.parent.parent

# Loading Models
RF = joblib.load(base / "artifacts" / "RF_model.pkl")
XGB = joblib.load(base / "artifacts" / "XG_model.pkl")
LGBM = joblib.load(base / "artifacts" / "LGB_model.pkl")

# Model Score of Accuracy, Recall, Precision and F1_score

models = {
    'Random_Forest' : RF,
    'XGBoost' : XGB,
    'LightBGM': LGBM
}

comparison = pd.DataFrame()

for name,model in models.items():
    pred = model.predict(Xtest)
    acc_score = accuracy_score(ytest,pred)
    prec_score = precision_score(ytest,pred,average='weighted')
    rec_score = recall_score(ytest,pred,average='weighted')
    f_score = f1_score(ytest,pred,average='weighted')
    comparison = pd.concat([comparison,pd.DataFrame([{
            'Model':name,
            'accuracy_score':acc_score,
            'precision_score':prec_score,
            'recall_score':rec_score,
            'f1_score':f_score
        }])],ignore_index=True)

# Confusion Matrix of Best Model
pred = XGB.predict(Xtest)
matrix = confusion_matrix(ytest,pred)
sns.heatmap(matrix,annot=True,fmt='.2f')
plt.title('XGBoost Confusion Matrix',fontsize=15,fontweight='bold')
plt.tight_layout()
plt.show()

# Comparison CSV File
comparison.to_csv('comparison.csv',index=False)