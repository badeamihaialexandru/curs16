# 3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 

caleText='\Users\Andreea\Desktop\curs\Curs16\curs16'

def loadTxt():
    with open(caleText,'r') as file:
        continut=file.read()
        return continut

# dati commit la schimbari in repositoryul local

# 3.2 scrieti o functie generateListFromString() care primeste ca parametru un string si returneaza o lista pe baza acestuia. stringul va avea formatul (string,string,string)
# dati commit la schimbari in repositoryul global

def generateListFromString(string):
 lista=[]
 for numar in range(5):
     lista.append(string)
     return lista
 
# 3.3 scrieti o functie care sa se numeasca uniques() care primeste ca parametru o lista si returneaza o lista cu valori unice 
# dati commit la schimbari in repositoryul global

 def uniques(lista):
    x=set()
    for element in lista:
        x.add(element)
    return x

# 3.4 scrieti o functie numita listToTxt care sa scrie lista unica intr-un fisier txt 

def listToTxt(lista, CaleText):
    with open(caleText,'w') as file:
        for line in lista:
            file.write(f"{str(line)}\n")

# dati commit la schimbari in repositoryul global
# creati pull request