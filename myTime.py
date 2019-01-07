import datetime

def transformarNumero(numero,cant): #cant = 3 => 001 ,cant = 2 => 01
    largo= str(numero).__len__()
    nuevo = str(numero)
    while largo < cant:
        nuevo = "0" + nuevo
        largo = nuevo.__len__()
    return(nuevo)

def mSecondtoSecond(ms):
    if ms < 1000:
        return(0,ms)
    else:
        nms = ms % 1000
        nsecond = int(ms/1000)
    return(nsecond,nms)

def cambiarHora(date,h,m,s): #date=hora antigua,h,m,s = nueva hora
    return date + datetime.timedelta(hours=h, minutes=m, seconds=s)

def horaString(date): #date= string de la forma %H:%M:%S
    h,m,s = date.split(":")
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

def hacerTodo(hora,h,m,s,ms = 0): #hora = H:M:S,MS
    tiempo, milisegundo = hora.strip().split(",")
    ms = ms + int(milisegundo)
    second,msecond = mSecondtoSecond(int(ms))
    dateTiempo = horaString(tiempo)
    newTiempo = cambiarHora(dateTiempo, h, m, s + second)
    h,m,s = newTiempo.__str__().split(":")
    nuevoTiempo = transformarNumero(h,2) + ":" + m + ":" + s 
    return nuevoTiempo + "," + transformarNumero(msecond,3)


#b = datetime.timedelta(hours=2, minutes=4, seconds=45)
#print(cambiarHora(b,0,0,0))
#print(horaString("2:04:25"))
#print(b.__str__())

