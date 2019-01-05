import datetime

def cambiarHora(date,h,m,s): #date=hora antigua,h,m,s = nueva hora
    return date + datetime.timedelta(hours=h, minutes=m, seconds=s)
def horaString(date): #date= string de la forma %H:%M:%S
    h,m,s = date.split(":")
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

def hacerTodo(hora,h,m,s,ms = 0): #hora = H:M:S,MS
    tiempo, milisegundo = hora.strip().split(",")
    dateTiempo = horaString(tiempo)
    newTiempo = cambiarHora(dateTiempo, h, m, s)
    return newTiempo.__str__() + "," + milisegundo


#b = datetime.timedelta(hours=2, minutes=4, seconds=45)
#print(cambiarHora(b,0,0,0))
#print(horaString("2:04:25"))
#print(b.__str__())

