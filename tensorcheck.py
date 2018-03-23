import numpy as np
import pandas as pd
import time
import csv
import urllib2
start_time = time.time()
# Importing the dataset
dataset = pd.read_csv('HIGGS.csv')
X = dataset.iloc[1:1500000:, 2:28].values
y = dataset.iloc[1:1500000:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Part 2 - Now let's make the ANN
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import CSVLogger

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu', input_dim = 26))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Fitting the ANN to the Training set
#csv_logger = CSVLogger('log.csv', append=True, separator=';')
for x in xrange(25):
	#print "Epoch Number:"
	#print x
	classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 1,verbose = 2)
	#with open('dummy.csv','wb') as csvfile:
		#writer = csv.writer(csvfile,delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#writer.writerow(X_train) 
	response =urllib2.urlopen('http://python.org/')
	html = response.read()	
	#time.sleep(0.5)
# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print (cm)
print ("Running time of the application")
print  time.time() - start_time 

