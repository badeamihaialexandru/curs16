import csv

def loadTxt(cale):
    with open(cale,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row) 

def generateListFromString(x):
    list=[]
    for i in x:
        list.append(i)
    return list

def uniques(y):
    n=set(y)
    return n

def listToTxt(y):
    with open('lista.txt','w') as file:
        unique_set=uniques(y)
        for item in unique_set:
            file.write(f'{item}\n')