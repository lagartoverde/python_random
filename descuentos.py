'''
Created on 21 de sept. de 2016

@author: lagarto
'''
import random
respuesta=0
while respuesta!=1:
    compra=input("Introuzca la cantidad total de la compra: ")
    if float(compra)>=100:
        print("Su gasto iguala o supera los $100.00 y por tanto participa en la promocion. \n \t Color \t \t Descuento \n \n \t Bola Blanca \t No tiene \n \t Bola Roja \t 10 por ciento \n \t Bola Azul \t 20 por ciento \n \t Bola Verde \t 25 por ciento \n \t Bola Amarilla \t 50 por ciento ")
        bola=random.randint(1,5)
        if bola==1:
            print("Atleatoriamente usted obtuvo una bola blanca \n Lo sentimos usted no ha obtenido ningun descuento")
        elif bola==2:
                print("Atleatoriamente usted obtuvo una bola roja \n Felicidades, ha ganado un 10 por ciento de descuento \n Su nuevo total a pagar es: "+str(float(compra)*0.9))
        elif bola==3:
            print("Atleatoriamente usted obtuvo una bola azul \n Felicidades, ha ganado un 20 por ciento de descuento \n Su nuevo total a pagar es: "+str(float(compra)*0.8))
        elif bola==4:
            print("Atleatoriamente usted obtuvo una bola verde \n Felicidades, ha ganado un 25 por ciento de descuento \n Su nuevo total a pagar es: "+str(float(compra)*0.75))
        elif bola==5:
            print("Atleatoriamente usted obtuvo una bola amarilla \n Felicidades, ha ganado un 50 por ciento de descuento \n Su nuevo total a pagar es: "+str(float(compra)*0.5))
        respuesta=int(input("Si desea salir presione 1 o de lo contrario presione otro numero: "))