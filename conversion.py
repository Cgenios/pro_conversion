# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 22:26:04 2022

@author: Luna
"""
"""
Estructura basica, menu del programa
"""
#menu y contenedores básicos
def menu():
    print("Seleccione una opción que tipo de conversión necesita:")
    print("               1.DD a DMS")
    print("               2.DMS a DD")
    opcion=int(input())
    if opcion==1:
        #coversexa()
        pedir_datos_sexa()
    elif opcion==2:
        pedir_datos_deci()
    
    
#peticion de datos en caso de ser sexagesimal 
def pedir_datos_sexa():
    datsexalat=input('Ingrese latitud en sexagesimal (grados): ')
    datsexalon=input('Ingrese longitud en sexagesimal (grados): ')
    grados=covern(datsexalat,datsexalon)
    return 0


#peticion de datos en caso de ser decimal    
def pedir_datos_deci():
    datdeclat=input('Ingrese latitud en decimales: ')
    datdeclon=input('Ingrese longitud en decimales: ')
    deci=covern(datdeclat,datdeclon)
    coverdas(deci)
    return 0


#conversion a cadena de numeros ingresados
def covern(dat1, dat2):
    xlat=str(dat1)
    xlon=str(dat2)
    return xlat,xlon

#conversion de decimales a grados sexagesimales
def coverdas(data):
    #Asignacion de variables a argumentos
    lat=data[0] #Division para la conversion de la tupla
    lon=data[1] #División para la conversion de la tupla
    conlat=lat.split(sep='.') #Se utiliza un separador en python
    conlon=lon.split(sep='.') #Se utiliza un separador en python en estos casos el punto
    
    #print(conlat[0],conlon)
    #Tratamiento con latitud en decimales a sexagecimales
    conlat[1]=float("0."+conlat[1])*60
    #print(conlat[1])
    res=str(conlat[1]).split(sep='.')
    seg=float("0."+res[1])*60
    print("Los grados latitud: "+conlat[0]+"°"+" "+res[0]+"' "+str(seg)+"''")
    
    #Tratamiento de datos en longitud
    conlon[1]=float("0."+conlon[1])*60
    #print(conlat[1])
    res1=str(conlon[1]).split(sep='.')
    seg1=float("0."+res1[1])*60
    print("Los grados longitud: "+conlon[0]+"°"+" "+res1[0]+"' "+str(seg1)+"''")

menu()
