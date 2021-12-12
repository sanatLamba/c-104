import csv

with open("height-weight.csv", newline="") as f :
    fileReader = csv.reader(f)
    fileData = list(fileReader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    number = fileData[i][1]  
    newData.append(float(number))

numberOfItems = len(newData)
total = 0

for i in newData :
    total = total+i

mean = total/numberOfItems

print("Mean is:"+str(mean))