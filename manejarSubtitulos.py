#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re,myTime,glob,fnmatch,os

def modifica(inicio,final,h,m,s,ms):
    newinicio = myTime.hacerTodo(inicio,h,m,s,ms)
    newfinal = myTime.hacerTodo(final,h,m,s,ms)

    return newinicio, newfinal

def abrirArchivo():
    input1 = input("Nombre de subtitulo a buscar:")
    ginput = glob.glob('*.txt')
    finput = fnmatch.translate('*.txt')
    print("Inicio")
    matches = list()
    cont = 0
    for file in os.listdir('.'):
        if re.match(input1 + finput,file):
            matches.append(file)
            print(str(cont) + " - " + file)
            cont+=1
    return matches

def manejarSubtitulo(archivo,h,m,s,ms):
    print("Archivo a modificar : " + archivo)
    print("Horas : " + str(h) + "\n" + "Minutos: " + str(m) + "\n" + "Segundos : " + str(s) + "\n" + "Milisegundos : " + str(ms) + "\n")
    file = open(archivo,'r+',encoding='utf-8')
    file2 = open(archivo + '-remastered.srt','w')
    #ObjArchivo = open('/home/archivo.txt',mode='r', encoding='utf-8')

    for line in file:
        i = re.split(" (-->) ",line)
        if i.__len__() > 2:
            inicio = i[0]
            final = i[2]
            ni,nf = modifica(inicio,final,h,m,s,ms)
            nueva = ni + " --> " + nf + "\n"
            file2.write(nueva)
        else:
            file2.write(line)
    file.close()
    file2.close()
    print("FINALIZADO : " + archivo + '-remastered.srt')

matches = abrirArchivo()
input2 = input("Elija su archivo : ")
archivo = matches[int(input2)]
input3 = input("Escriba el tiempo a modificar(Hora:Minuto:Segundo:Milisegundo) : ")
h,m,s,ms = input3.split(":")
manejarSubtitulo(archivo,int(h),int(m),int(s),int(ms))
