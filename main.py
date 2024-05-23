import Octavian_pb as tavi

print(tavi.load.Txt('\Users\Andreea\Desktop\curs\Curs16\curs16\lista.txt'))
print(tavi.generateListFromString('String'))
lista=['Dean','Dean','Andrei','Andrei']
print(tavi.uniques(lista))
lista2=tavi.uniques(lista)
tavi.writeListToFile(lista2,'\Users\Andreea\Desktop\curs\Curs16\curs16\listanoua.txt')
