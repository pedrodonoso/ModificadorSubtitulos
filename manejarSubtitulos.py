import re,myTime

def modifica(inicio,final,h,m,s,ms):
    newinicio = myTime.hacerTodo(inicio,h,m,s,ms)
    newfinal = myTime.hacerTodo(final,h,m,s,ms)

    return newinicio, newfinal

file = open('sub.txt','r+')
file2 = open('sub-remastered.txt','w')
#ObjArchivo = open('/home/archivo.txt',mode='r', encoding='utf-8')
lista = []
c = 0
while c < 60:
    line = file.readline()
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
