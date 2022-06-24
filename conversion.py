# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 22:26:04 2022

@author: Luna
"""
"""
Estructura basica, menu del programa
"""

def menu():
    print("Seleccione una opción que tipo de conversión necesita:")
    print("               1.DD a DMS")
    print("               2.DMS a DD")
    opcion=int(input())
    if opcion==1:
        pedir_datos_sexa()
        

def pedir_datos_sexa():
    datsexalat=input('Ingrese latitud en sexagesimal (grados): ')
    datsexalon=input('Ingrese longitud en sexagesimal (grados): ')
    return datsexalat,datsexalon
    
def pedir_datos_deci():
    datdeclat=input('Ingrese latitud en decimales: ')
    datdeclon=input('Ingrese longitud en decimales: ')
    return datdeclat,datdeclon

menu()
