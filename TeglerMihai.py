import csv

def loadTxt(cale):
    with open(cale,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
    
loadTxt('loadTxt.csv')

def generateListFromString(x):
    list=[]
    for i in x:
        list.append(i)
    return list

print(generateListFromString('Mihai are mere'))

