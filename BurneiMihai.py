def loadTxt(cale):
    with open(cale,'r') as file:
        content = file.read()
    return content

continut = loadTxt('Curs14/logger.txt')
print(continut)


def generateListFromString(string):
    lista=[]
    for element in range(3):
        lista.append(string)
    return lista


def uniques(lista):
    unic=set()
    for element in lista:
        unic.add(element)
    return unic


def listToTxt(lista, cale):
    lista_unice=list(set(lista))
    with open(cale,'w') as file:
        for i in lista_unice:
            file.write(i)
