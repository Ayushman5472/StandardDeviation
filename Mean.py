import csv
import math

with open('data1.csv') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
Marks = []

for i in range(len(fileData)):
    tempVar = fileData[i][1]
    #storing the 1st coloumn in a temp variable
    Marks.append(float(tempVar))

n = len(Marks)
total = 0
for marks in Marks:
    total = total+marks

mean1 = total/n
print(mean1)

with open('data2.csv') as f:
    reader = csv.reader(f)
    fileData2 = list(reader)

fileData2.pop(0)
Marks2 = []

for i in range(len(fileData2)):
    tempVar2 = fileData2[i][1]
    Marks2.append(float(tempVar2))

l = len(Marks2)
total2 = 0
for marks in Marks2:
    total2 = total2+marks

mean2 = total2/l
print(mean2)


standardDev1 = []
for n in fileData:
    tempVar = int(n)
    #tempVar = tempVar**2
    standardDev1.append(tempVar)
    

sum1 = 0
for a in standardDev1:
    sum1 = sum1 + a

result1 = sum1/(n-1)
StandardDeviation1 = math.sqrt(result1)
print(StandardDeviation1)
