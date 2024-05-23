def loadTxt(path):
    with open(path,'r') as file:
        content=file.read()
        return content


def generateListFromString(string):
    lista=[]
    for nr in range(3):
        lista.append(string)
    return lista


def uniques():
    lista=['Dean','Dean','Andrei','Andrei']
    lista=set(lista)
    return lista


def listaToTxt():
    listaUnica=uniques()
    with open('Curs16/curs16/uniques.txt','w') as file:
        file.write(str(listaUnica))
