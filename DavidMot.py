#3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 
#dati commit la schimbari in repositoryul local

def loadTxt(cale):
    with open (cale,"r") as file:
        continut=file.readlines
        return(continut)
    
#3.2 scrieti o functie generateListFromString() care primeste ca parametru un string si returneaza o lista pe baza acestuia. stringul va avea formatul (string,string,string)
#dati commit la schimbari in repositoryul global

def generateListFromString():
    string="Salutare tuturor"
    list=[]
    for i in string:
        list.append(i)
    print(list)

#generateListFromString()


#3.3 scrieti o functie care sa se numeasca uniques() care primeste ca parametru o lista si returneaza o lista cu valori unice 
#dati commit la schimbari in repositoryul global


def uniques(list):
    myset=set(list)
    print(myset)

#uniques([1,2,3,4,5,1,3,4])

#3.4 scrieti o functie care sa scrie lista unica intr-un fisier txt 
# dati commit la schimbari in repositoryul global
# creati pull request


def listToTxt(list):
    with open ("curs_16/curs16/outputDavid.txt",'w') as file:
        for elem in list:
            file.write(elem)

