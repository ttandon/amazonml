##without feature engineering

from __future__ import division

import csv
import numpy as np
from sklearn import (metrics, cross_validation, linear_model, preprocessing)
from sklearn.ensemble import RandomForestRegressor
import numpy as np

SEED = 25
##extract train data
def load_data(filename, use_labels=True):

	data = np.loadtxt(open("../datasets/" + filename), delimiter=',',
                      usecols=range(1, 9), skiprows=1)
	if use_labels:
		labels = np.loadtxt(open("../datasets/" + filename), delimiter=',', usecols=[0], skiprows=1)
	else:
		labels = np.zeros(data.shape[0])
	return labels, data

def save_results(predictions, filename):
	ofile = filename
	filew = open(ofile, "w")
	filew.write("id,ACTION\n")
	for i, pred in enumerate(predictions):
		filew.write("%d,%f\n" % (i + 1, pred))

print "loading data"
Forest = RandomForestRegressor(n_estimators = 500)
y, X = load_data('train.csv')
y_test, X_test = load_data('test.csv', use_labels=False)
##CV
mean_auc = 0.0
n = 10
for i in range(n):
	X_train, X_cv, y_train, y_cv = cross_validation.train_test_split(
	            X, y, test_size=.20, random_state=i*SEED)
	Forest = Forest.fit(X_train, y_train)
	predictions = Forest.predict(X_cv)
	fpr, tpr, thresholds = metrics.roc_curve(y_cv, predictions)
	roc_auc = metrics.auc(fpr, tpr)
	print "AUC (fold %d/%d): %f" % (i + 1, n, roc_auc)
	mean_auc += roc_auc
print "Mean AUC: %f" % (mean_auc/n)
Forest = Forest.fit(X, y)
predictions = Forest.predict(X_test)
save_results(predictions, "../output/rfpred.csv")