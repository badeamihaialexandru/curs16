import Octavian_pb as oct

print(oct.loadTxt('Curs16/curs16/lista.txt'))

print(oct.generateListFromString('String'))
lista=['Dean','Dean','Andrei','Andrei']
print(oct.uniques(lista))
lista2=oct.uniques(lista)
oct.writeListToFile(lista2,'Curs16/curs16/listaNoua.txt')