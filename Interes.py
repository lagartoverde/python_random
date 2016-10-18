'''
Created on 21 de sept. de 2016

@author: lagarto
'''
dolares=input("Introduzca una cantidad de dolares: ")
interes=input("Introduzca una tasa de interes: ")
anos=input("Introduzca un numero de anos: ")
total=float(dolares)*((1+float(interes)/100)**float(anos))
print("Obtendras "+str(total)+" dolares.")