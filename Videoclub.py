'''
Created on 22 de sept. de 2016

@author: lagarto
'''

print(" Categoria \t \t Precio \t Codigo \t Recargo/Dia de atraso \n \n Favoritos \t \t $2.50 \t \t 1 \t \t $0.50 \n Nuevos \t \t $3.00 \t \t 2 \t \t $0.75 \n Estrenos \t \t $3.50 \t \t 3 \t \t $1.00 \n Super Estrenos \t $4.00 \t \t 4 \t \t $1.50 ")
codigo=input("\n Introduzca el codigo de la categoria de la pelicula: ")
retraso=input("Introduzca el numero de dias de atraso en la devolucion: ")
multa={"1":0.5, "2":0.75, "3":1, "4":1.5}
precio=multa[str(codigo)]
pelicula={"1":2.5, "2":3, "3":3.5, "4":4}
preciopeli=pelicula[str(codigo)]
preciotot=(precio*int(retraso))+preciopeli
print("\n El total a pagar es : "+str(preciotot)+" dolares")