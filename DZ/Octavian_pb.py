def loadTxt(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def generateListFromString(string):
    print("de la octavian!!!")
    return string.split(',')

def uniques(input_list):
    return list(set(input_list))

def writeListToFile(output_list, filepath):
    with open(filepath, 'w') as file:
        for item in output_list:
            file.write(f"{item}\n")
