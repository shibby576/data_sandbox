#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()





from sklearn import svm
from time import time

#reduce the trianing data
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]


clf = svm.SVC(kernel='rbf', C=10000)
t0 = time()
clf.fit(features_train, labels_train)
#print trianing time
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)

#get individual predictions
ten = pred[10]
two_six = pred[26]
fifty = pred[50]

#Get number that are predicted to be chris (1)
chris = pred.sum()

#print prediction  time
print "prediction time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print('Accuracy ' + str(acc))

#print individual predictions
print('#10 ' + str(ten) + ' #26 ' + str(two_six) + ' #50 ' + str(fifty))

#print number that are chris
print(chris)
