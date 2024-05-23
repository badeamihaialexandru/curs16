# 3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 
# dati commit la schimbari in repositoryul local

def loadTxt(caletxt):
    with open(caletxt,'r') as file:
        fisier=file.readlines()
        return fisier
    
# 3.2 scrieti o functie generateListFromString() care primeste ca parametru un string si returneaza o lista pe baza acestuia. stringul va avea formatul (string,string,string)
# dati commit la schimbari in repositoryul global
def generateListFromString(string,separator):
    lista=string.split(separator)
    return lista

# 3.3 scrieti o functie care sa se numeasca uniques() care primeste ca parametru o lista si returneaza o lista cu valori unice 
# dati commit la schimbari in repositoryul global
def uniques(lista):
    unic=set()
    for element in lista:
        unic.add(element)
    return unic

# 3.4 scrieti o functie care sa scrie lista unica intr-un fisier txt 
# dati commit la schimbari in repositoryul global
# creati pull request
def listToTxt(lista,caletxt):
    with open(caletxt,'w') as file:
        for line in lista:
            file.write(f"{str(line)}\n")
