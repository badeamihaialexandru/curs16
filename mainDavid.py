import Octavian_pb as oc

print(oc.loadTxt("lista.txt"))
print(oc.generateListFromString("Salutare tuturor!"))
print(oc.uniques([1,2,3,4,1,2,5,3]))
lista=oc.uniques([1,2,3,4,1,2,5,3])
#oc.writeListToFile(lista,'newoutput.txt')