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

