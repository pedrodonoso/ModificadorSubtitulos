import re,myTime,glob,fnmatch,os

def modifica(inicio,final,h,m,s,ms):
    newinicio = myTime.hacerTodo(inicio,h,m,s,ms)
    newfinal = myTime.hacerTodo(final,h,m,s,ms)

    return newinicio, newfinal

input1 = input("Nombre de subtitulo a buscar:")
reinput = glob.glob('*.txt')
#print(reinput)
s = fnmatch.translate('*.txt')
print("Inicio")
matches = list()
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, s):
        print("Fn - " + file)
    elif re.match(input1 + s,file):
        matches.append(file)
        print("Match - " + file)
    else:
        print("No - " + file)
print("Final")

cont = 0
for file in matches:
    print(str(cont) + " : " + file)
    cont += 1

input2 = input()
print(matches[int(input2)])
file = open(matches[int(input2)],'r+')
file2 = open('sub-remastered.txt','w')
#ObjArchivo = open('/home/archivo.txt',mode='r', encoding='utf-8')
lista = []
c = 0
for line in file:
    i = re.split(" (-->) ",line)
    if i.__len__() > 2:
        inicio = i[0]
        final = i[2]
        ni,nf = modifica(inicio,final,0,0,0,10)
        nueva = ni + " --> " + nf + "\n"
        lista.append(nueva)
        file2.write(nueva)
    else:
        lista.append(line)
        file2.write(line)
    c = c + 1

file.close()
file2.close()
