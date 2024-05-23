#3.1

def loadtxt(txt):
   with open (txt, 'r')as file:
      list=file.read
      return list

#3.2

def generateListFromString(string):
   list=[]
   for i in string:
      list.append(i)
   return list

#3.3

def uniques(n):
   unik=set()
   for e in n:
      unik.add(e)
   return unik


#3.4

def listToTxt(n):
    with open('list.txt','w') as file:
        unics=uniques(n)
        for i in unics:
            file.write(f'{i}\n')