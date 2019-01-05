import re,myTime
def modifica(inicio,final,h,m,s):
    newinicio = myTime.hacerTodo(inicio,h,m,s)
    newfinal = myTime.hacerTodo(final,h,m,s)
    print(newinicio, newfinal)
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
        ni,nf = modifica(inicio,final,0,0,2)
        nueva = ni + " --> " + nf + "\n"
        lista.append(nueva)
    else:
        lista.append(line)
    print(i)
    c = c + 1

file.close()

for i in lista:
    print(i)
