'''
Created on 21 de sept. de 2016

@author: lagarto
'''
import random
longitud=input("Dime la longitud de la cadena")
secreto= random.randint(10**(int(longitud)-1),(10**(int(longitud))-1))
seguir=True
while seguir:
    respuesta=input("Intenta adivinar la cadena")
    indice=0
    secreto=str(secreto)
    acertadas=0
    for i in respuesta:
        if i==secreto[indice]:
            acertadas+=1
        indice+=1
    print ("Con "+respuesta+" has adivinado "+str(acertadas)+" valores")
    if acertadas==int(longitud):
        seguir=False
        print("Felicidades, has ganado")