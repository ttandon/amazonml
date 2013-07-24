from sklearn.metrics import metrics

file = open("../output/splitpred1.csv")
numarray = []
while 1:
	line = file.readline()
	if not line:
		break
	numarray.append(float(line))
file = open("../output/answers.csv")
answerarray = []
while 1:
	line = file.readline()
	if not line:
		break
	answerarray.append(float(line))
fpr, tpr, thresholds = metrics.roc_curve(answerarray, numarray, pos_label=1)
auc = metrics.auc(fpr,tpr)
print auc