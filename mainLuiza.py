import Octavian_pb as oct

print(oct.loadTxt("lista.txt")) #eroare

print(oct.generateListFromString("Ana are mere")) #nu il converteste in lista, pune stringul singur intr-o lista

print(oct.uniques([1,4,2,5,6,1,4,2,41]))

oct.writeListToFile([1,4,2,5,6,1,4,2,41],"curs16/list.txt")