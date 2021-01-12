import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import random
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import xgboost
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data=pd.read_csv("indian_liver_patient.csv")
data=data.fillna(method="ffill")
data.Gender=data.Gender.map({"Female":1,"Male":0})
data["Dataset"]=data["Dataset"].map({1:0,2:1})
np.random.shuffle(data.values)
print(data.shape[1])
print(data.columns)


target=data["Dataset"]
source=data.drop(["Dataset"],axis=1)
sm=SMOTE()
sc=StandardScaler()
lr=LogisticRegression()
source=sc.fit_transform(source)
X_train,X_test,y_train,y_test= train_test_split(source,target,test_size=0.01)
X_train, y_train=sm.fit_sample(X_train,y_train)
cv=cross_validate(lr,X_train,y_train,cv=10)
lr.fit(X_train,y_train)
print(cv)
joblib.dump(lr,"model4")



#for cross valid
params={
 "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.1, 0.2, 0.3, 0.4, 0.5 , 0.7 ]
    
}

classifier=xgboost.XGBClassifier()
random_search=RandomizedSearchCV(classifier,param_distributions=params,n_iter=5,scoring='roc_auc',n_jobs=-1,cv=5,verbose=3)

random_search.fit(X_train,y_train)

clf = random_search.best_estimator_