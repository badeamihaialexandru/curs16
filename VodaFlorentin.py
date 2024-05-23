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

