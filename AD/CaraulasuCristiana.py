#3.1 3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 


def loadTxt(cale):
    print("din modul!!!")
    # with open (cale,'r') as file:
    #     continut = file.read()
    # return continut

cale = "SCRIPTURI_CURS/Curs2.py"
file_content = loadTxt(cale)
# print (file_content)

#3.2 scrieti o functie generateListFromString() care primeste ca parametru un string si returneaza o lista pe baza acestuia. 
#stringul va avea formatul (string,string,string)

def generateListFromString(string,separator):
    lista = string.split(separator)
    print("de la cristiana")
    return lista
#print (generateListFromString('1,2,3,4',','))

#3.3 scrieti o functie care sa se numeasca uniques() care primeste ca parametru o lista si returneaza o lista cu valori unice 

def unique():
    lista = ['1','2','2','5']
    unica = set(lista)
    return unica
#print (unique())

#3.4 scrieti o functie numita listToTxt care sa scrie lista unica intr-un fisier txt 

def listToTxt():
    lista = unique()
    with open ("Curs14/curs16/lista_unica.txt",'w') as file:
        unic = file.write(str(lista))
    return unic
#listToTxt()
    