# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 08:39:09 2018

@author: nithi
"""
##Importing the libraries###
import numpy as np
import pandas as pd
import time
start_time = time.time()
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#from matplotlib.colors import ListedColormap

### importing dataset####
dataset = pd.read_excel("iris.xlsx")
X = dataset.iloc[:,0:4]
y= dataset.iloc[:,4]
#### Train test split######
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

####Feature scaling#####
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#### Fitting to the model and predicting the result####
classifier = SVC()
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

### Confusion Matrix####
cm = confusion_matrix(y_test, y_pred)
print cm
print ("Running time of the application")
print  time.time() - start_time
