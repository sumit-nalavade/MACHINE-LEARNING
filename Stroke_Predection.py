# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vwd8bShZC-wNdujww_FN1iZvx25jasWX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("/content/Brain Stroke.csv")

print(dataset.shape)
print("")
print(dataset.info())
print("")
print(dataset.describe())
print("")
dataset.head(5)

from sklearn.preprocessing import LabelEncoder
lbl = LabelEncoder()
dataset["gender"] = lbl.fit_transform(dataset["gender"])
dataset["ever_married"] = lbl.fit_transform(dataset["ever_married"])
dataset["work_type"] = lbl.fit_transform(dataset["work_type"])
dataset["Residence_type"] = lbl.fit_transform(dataset["Residence_type"])
dataset["smoking_status"] = lbl.fit_transform(dataset["smoking_status"])

print(dataset.shape)
dataset.head(5)

from collections import Counter
print(Counter(dataset["stroke"]))
sns.heatmap(data = dataset.corr(),cmap = "Blues")

dataset.isnull().sum()

"""#Logistic Regression Algorithm

"""

x = dataset.iloc[ : , :-1]
y = dataset.iloc[ : , -1]

print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=7)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print("")

print(accuracy_score(y_test,y_pred)*100)
print("")

print(confusion_matrix(y_test,y_pred))
print("")

"""# Logistic Regression with Normalization Techqnique


"""

x = dataset.iloc[ : , :-1]
y = dataset.iloc[ : , -1]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=7)

from sklearn.preprocessing import normalize
x_train = normalize(x_train)
x_test = normalize(x_test)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print("")

print(accuracy_score(y_test,y_pred)*100)
print("")

print(confusion_matrix(y_test,y_pred))
print("")

"""# Logistic Regression with Standard Scaler Techqnique"""

x =  dataset.iloc[ : , :-1]
y = dataset.iloc[ : ,-1]

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 77)
scaler = StandardScaler()
model = LogisticRegression()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print("")

print(accuracy_score(y_pred,y_test)*100)
print("")

print(confusion_matrix(y_pred,y_test))
print("")

print(x_train.shape)
print(y_pred.shape)
print("rows = ",x_train.shape + y_pred.shape)
print("")

"""#KNN Algorithm"""

x = dataset.iloc[ : , :-1]
y = dataset.iloc[ : ,-1]

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=70)
knn = KNeighborsClassifier(n_neighbors=9)

knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)
print("")

print(accuracy_score(y_pred,y_test)*100)
print("")

print(confusion_matrix(y_pred,y_test))
print("")

"""#KNN Algorithm with Standardization"""

x = dataset.iloc[ : , :-1]
y = dataset.iloc[ : ,-1]

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 70)
knn = KNeighborsClassifier(n_neighbors=9)
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)
print("")

print(accuracy_score(y_pred,y_test)*100)
print("")

print(confusion_matrix(y_pred,y_test))
print("")

"""#Logistic Regression with Oversampling"""

x = dataset.iloc[ : , :-1]
y = dataset.iloc[ : ,-1]

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE


model = LogisticRegression()
smote = SMOTE(sampling_strategy='auto', k_neighbors=5, random_state=42)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=33)

X_resampled, y_resampled = smote.fit_resample(x_train, y_train)

model.fit(X_resampled,y_resampled)

y_pred = model.predict(x_test)
print("")

print(accuracy_score(y_pred,y_test)*100)
print("")

print(confusion_matrix(y_pred,y_test))
print("")

"""# Logistic Regression with standardization and oversampling"""

x = dataset.iloc[ : , :-1]
y = dataset.iloc[ : ,-1]

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler


model = LogisticRegression()
smote = SMOTE(sampling_strategy='auto', k_neighbors=5, random_state=42)
scaler = StandardScaler()

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=33)

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

X_resampled, y_resampled = smote.fit_resample(x_train, y_train)

model.fit(X_resampled,y_resampled)

y_pred = model.predict(x_test)
print("")

print(accuracy_score(y_pred,y_test)*100)
print("")

print(confusion_matrix(y_pred,y_test))
print("")