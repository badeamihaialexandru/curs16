def loadTxt(path):
    with open(path,'r') as file:
        content=file.read()
        return content
# print(loadTxt('Curs13/input.txt'))

def generateListFromString(string):
    lista=[]
    for nr in range(3):
        lista.append(string)
    return lista
# print(generateListFromString('Macarena'))

def uniques():
    lista=['Dean','Dean','Andrei','Andrei']
    lista=set(lista)
    return lista
print(uniques())