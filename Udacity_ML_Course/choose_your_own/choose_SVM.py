#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


from sklearn import svm
from time import time

#reduce the trianing data
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]


clf = svm.SVC(kernel='rbf', C=100000)
t0 = time()
clf.fit(features_train, labels_train)
#print trianing time
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)

#print prediction  time
print "prediction time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print('Accuracy ' + str(acc))