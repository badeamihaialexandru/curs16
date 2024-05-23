#3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 
#dati commit la schimbari in repositoryul local

def loadTxt(cale):
    with open (cale,"r") as file:
        return(file)
    
#3.2 scrieti o functie generateListFromString() care primeste ca parametru un string si returneaza o lista pe baza acestuia. stringul va avea formatul (string,string,string)
#dati commit la schimbari in repositoryul global

def generateListFromString():
    string="Salutare tuturor"
    list=[]
    for i in string:
        list.append(i)
    print(list)

generateListFromString()
