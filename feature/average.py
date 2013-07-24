import csv

cr = csv.reader(open("../output/logisticpred.csv","rb"))
logarray = []
counter = 0
for row in cr:
	if counter != 0:
		logarray.append(float(row[1]))
	counter = counter + 1

cr2 = csv.reader(open("../output/rfpred.csv","rb"))
rfarray = []
counter = 0
for row in cr2:
	if counter != 0:
		rfarray.append(float(row[1]))
	counter = counter + 1
print len(logarray)
print len(rfarray)
averagearr = []
index = 0
for lval in logarray:
	rval = rfarray[index]
	average = (rval + lval)/2.0
	averagearr.append(average)
	index = index + 1


num = 1
ofile ="../output/avgpred.csv"
filew = open(ofile, "w")
filew.write("id,ACTION\n")
for avg in averagearr:
	print avg
	filew.write(str(num) + "," + str(avg) + "\n")
	num = num + 1


