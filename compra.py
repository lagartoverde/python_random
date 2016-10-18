'''
Created on 22 de sept. de 2016

@author: lagarto
'''
print("Elija el producto deseado: \n \n Producto \t \t Codigo \n \n Camisa \t \t 1 \n Cinturon \t \t 2 \n Zapatos \t \t 3 \n Pantalon \t \t 4 \n Calcetines \t \t 5")
seguir=True
total=0
while seguir:
    codigo=input(" \n Introduzca el codigo, presione 0 para finalizar la compra: ")
    if codigo=="0":
        seguir=False
    elif codigo!="0":
        precios={"1":20, "2":10, "3":40, "4":25, "5":2}
        precio=precios[str(codigo)]
        cantidad=input("\n El precio es: "+str(precio)+" Introuzca el numero de unidades:")
        preciotot=float(precio)*int(cantidad)
        total+=preciotot
        print("El total acumulado es: "+str(total))
print("La compra asciende a: "+str(total))
    