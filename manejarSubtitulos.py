import re
archivo = input("Escribe el nombre del archivo Subtitulo: ")
file = open(archivo + ".txt",'r')
for line in file:
    print("match :")

    m = re.match(r"(\w+) (\w+)",line)
    m.group(0)
    
    print("linea :")
    print(line)

file.close()
