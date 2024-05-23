def loadTxt(cale):
    with open(cale,'r') as file:
        content = file.read()
    return content

continut = loadTxt('Curs14/logger.txt')
print(continut)


#    


def uniques(lista):
    unic=set()
    for element in lista:
        unic.add(element)
    return unic


    