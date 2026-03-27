# 🤖 Machine Learning Projects Collection

This repository contains a collection of end-to-end Machine Learning projects covering core techniques in:

- 📈 Regression
- 🧠 Classification
- 🔍 Clustering

Each project follows a structured workflow including data preprocessing, exploratory data analysis (EDA), model building, and evaluation.

## 🛠️ Tech Stack 
- Python
- NumPy, Pandas (Data manipulation)
- Matplotlib, Seaborn (Data visualization)
- Scikit-learn (Modeling & evaluation)

# 📂 Projects Overview
##  📈 Regression Projects
- **☁️ Cloud Pricing**
  - Objective: Predict continuous values for cloud usage
  - Model Used: XGBoostRegressor
  - Results:
    - R² Score: 0.9999
    - RMSE: 0.3410
  - Highlights:
    - Transformed categorical variables using encoding techniques  
    - Applied feature scaling to normalize data distribution
    - Improved prediction performance using XGBoost 
- **🧠 Cognitive Load**
  - Objective: Predicting continuous values for Human Cognitive Load
  - Model Used: RidgeRegression
  - Result:
    - R² Score: 0.5924
    - RMSE: 0.4910
  - Highlights:
    - Engineered 4 new features to capture relationships between variables
    - Transformed categorical variables using encoding techniques
    - Applied feature scaling to normalize input features
    - Moderate predictive performance, indicating scope for feature improvement
  

## 🏷️ Classification Projects
- **👾 AI Misuse**
  - Objective : Detecting Anomaly Users
  - Model Used: LightGBMClassifier
  - Result:
    - Accuracy: 0.7171
    - Precision: 0.9859
    - Recall: 0.6694
    - F1 Score: 0.7974
    - ROC-AUC: 0.8255
  - Highlights:
    - Achieved very high precision, minimizing false positives  
    - Observed lower recall, indicating missed positive cases  
    - Balanced model performance with F1 Score and ROC-AUC evaluation 
- **📱Platform Trustworthy**
  - Objective: Detecting Negative Platforms
  - Model Used: SVC (Support Vector Classifier)
  - Result:
    - Accuracy: 0.896
    - Precision:  0.9877
    - Recall: 0.8957
    - F1 Score: 0.9395
    - ROC-AUC: 0.9683
  - Highlights:
    - Achieved high precision while maintaining strong recall  
    - Demonstrated well-balanced performance with high F1 Score  
    - Excellent class separation indicated by ROC-AUC score  
    - Built a reliable and robust classification model


## 🗃️ Cluster Project
- **🔌API Usage**
  - Objective: Grouping Usage of Different APIs
  - Model Used: DBSCAN and K-Means
  - Result:
    - Silhouette Score: 0.1128
  - Highlights:
    - Applied clustering to identify underlying data patterns 
    - Used Elbow Method to determine optimal number of clusters 
    - Observed low cluster separation, indicating overlapping groups   