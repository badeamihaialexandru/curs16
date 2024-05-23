def loadTxt(path):
    with open(path,'r') as file:
        content=file.read()
        return content
print(loadTxt('Curs13/input.txt'))