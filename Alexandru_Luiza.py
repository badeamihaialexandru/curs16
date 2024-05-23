# 3.1 scrieti o functie loadTxt() care primeste ca parametru calea unui fisier si incarca continutul acestuia in memorie 
# dati commit la schimbari in repositoryul local

def loadTxt(caletxt):
    with open(caletxt,'r') as file:
        fisier=file.readlines()
        return fisier