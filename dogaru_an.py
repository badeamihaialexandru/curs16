#3.1
def loadTxt(file_path):
    with open(file_path, 'r') as file:
            content = file.read()
    return content

file_path = "fisier.txt"
content = loadTxt(file_path)
if content:
    print(content)

#3.2
def lista_string(string):
    
    string = string.replace('(', '').replace(')', '').replace(' ', '')

    parts = string.split(',')
    return parts

input_string = "(string, string, string)"
lista = lista_string(input_string)
print(lista)