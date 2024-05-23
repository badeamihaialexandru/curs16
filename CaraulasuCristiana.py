#3.1 3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 


def loadTxt(cale):
    with open (cale,'r') as file:
        continut = file.read()
    return continut

cale = "SCRIPTURI_CURS/Curs2.py"
file_content = loadTxt(cale)
print (file_content)