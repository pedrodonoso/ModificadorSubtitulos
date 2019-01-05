import re,time

def modifica(inicio,final,segundos):
    segundo,milisegundo = inicio.strip().split(",")
    h,m,s = segundo.split(":")
    newsegundo = int(s) + segundos
    lista = []
    lista.append(h)
    lista.append(m)
    lista.append(str(newsegundo))
    newinicio = ":".join(lista) + "," + milisegundo
    
    segundo, milisegundo = final.strip().split(",")
    h, m, s = segundo.split(":")
    newsegundo = int(s) + segundos
    lista = []
    lista.append(h)
    lista.append(m)
    lista.append(str(newsegundo))
    newfinal = ":".join(lista) + "," + milisegundo
    return newinicio, newfinal


file = open('sub.txt','r+')
#ObjArchivo = open('/home/archivo.txt',mode='r', encoding='utf-8')
lista = []
c = 0
while c < 6:
    line = file.readline()
    i = re.split(" (-->) ",line)
    if i.__len__() > 2:
        inicio = i[0]
        final = i[2]
        ni,nf = modifica(inicio,final,2)
        nueva = ni + " --> " + nf + "\n"
        lista.append(nueva)
    else:
        lista.append(line)
    print(i)
    c = c + 1

print(lista)
file.close()
