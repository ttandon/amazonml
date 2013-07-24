import csv

cr = csv.reader(open("../datasets/train.csv","rb"))
train = []
test = []
solution = []
linecounter = 0
for row in cr:
	if linecounter != 0 and linecounter >= 10662:
		train.append(row)
	elif linecounter != 0 and linecounter < 10662:
		copy = row
		solution.append(copy.pop(0))
		test.append(copy)
	linecounter = linecounter + 1
##write splitted training data to csv file
ofile ="../datasets/trainsplit.csv"
filew = open(ofile, "w")
filew.write("ACTION,RESOURCE,MGR_ID,ROLE_ROLLUP_1,ROLE_ROLLUP_2,ROLE_DEPTNAME,ROLE_TITLE,ROLE_FAMILY_DESC,ROLE_FAMILY,ROLE_CODE\n")
for row in train:
	counter = 0
	for item in row:
		filew.write(item)
		if counter < 9: filew.write(",") 
		counter = counter + 1
	filew.write("\n")

##writing the splitted test file to csv file
ofile = "../datasets/testsplit.csv"
filex = open(ofile, "w")
filex.write("ID,RESOURCE,MGR_ID,ROLE_ROLLUP_1,ROLE_ROLLUP_2,ROLE_DEPTNAME,ROLE_TITLE,ROLE_FAMILY_DESC,ROLE_FAMILY,ROLE_CODE\n")
mycount = 1
for row in test:
	counter = 1
	filex.write(str(mycount) + ",")
	for item in row:
		filex.write(item)
		if counter<9: filex.write(",")
		counter = counter + 1
	mycount = mycount + 1
	filex.write("\n")


##write answers to separate file
ofile = "../output/answers.csv"
filey = open(ofile, "w")
for row in solution:
	filey.write(row[0] + "\n")

