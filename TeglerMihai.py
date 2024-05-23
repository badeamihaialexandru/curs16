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

def uniques(y):
    n=set(y)
    return n

list=[1,2,3,1,2,6,1,10,0,2,3,1,1,2,15,201,10,20,3]
print(uniques(list))


def listToTxt(y):
    with open('lista.txt','w') as file:
        unique_set=uniques(y)
        for item in unique_set:
            file.write(f'{item}\n')

listToTxt(list)