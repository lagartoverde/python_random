'''
Created on 21 de sept. de 2016

@author: lagarto
'''
palabra1=input("Introduce la primera palabra:")
palabra2=input("Introduce la segunda palabra:")
if palabra1[-1]==palabra2[-1] and palabra1[-2]==palabra2[-2] and palabra1[-3]==palabra2[-3]:
    print("Las palabras riman")
elif palabra1[-1]==palabra2[-1] and palabra1[-2]==palabra2[-2]:
    print("Las palabras solo riman un poco")
else:
    print("Las palabras no riman")