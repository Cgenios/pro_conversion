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
        n1=pedir_datos_sexa()
    print(n1,type(n1))
    
#peticion de datos en caso de ser sexagesimal 
def pedir_datos_sexa():
    datsexalat=input('Ingrese latitud en sexagesimal (grados): ')
    datsexalon=input('Ingrese longitud en sexagesimal (grados): ')
    return datsexalat,datsexalon
#peticion de datos en caso de ser decimal    
def pedir_datos_deci():
    datdeclat=input('Ingrese latitud en decimales: ')
    datdeclon=input('Ingrese longitud en decimales: ')
    return datdeclat,datdeclon

#conversion a cadena de numeros ingresados
def coversexa(dat1, dat2):
    xlat=str(dat1)
    xlon=str(dat2)
    return xlat,xlon
    
        

menu()
