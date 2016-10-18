'''
Created on 22 de sept. de 2016

@author: lagarto
'''
def suma_acumulada(lista):
    indice1=0
    indice2=0
    listafinal=[]
    
    suma=0
    for x in lista:
        if indice2<=indice1:
            suma+=x
            indice2+=1
        listafinal.insert(indice1, suma)
        indice1+=1
    return listafinal


print(suma_acumulada([1,2,3]))

def tamano_lista(lista):
    tamano=0
    for i in lista:
        tamano+=1
    return tamano

def elimina(lista):
    tamano=tamano_lista(lista)
    listanueva=[]
    indice=0
    for i in lista:
        if indice!=0 and indice!=(tamano-1):
            listanueva.append(i)
        indice+=1
    return listanueva



def ordenada(lista):
    indice=0
    ordenado=True
    for i in lista:
        if indice!=0:
            if lista[indice]<lista[(indice-1)]:
                ordenado=False
        indice+=1
    return ordenado



def duplicado(lista):
    tamano=tamano_lista(lista)
    duplicados=False
    resultado=0
    for i in lista:
        for x in lista:
            if x==i:
                resultado+=1
    if resultado>tamano:
        duplicados=True
    return duplicados



def elimina_duplicados(lista):
    indice1=0
    indice2=0
    duplicado=False
    listanueva=[]
    for i in lista:
        duplicado=False
        indice2=0
        for x in lista:
            if x==i and indice1!=indice2:
                duplicado=True
            indice2+=1
        if not duplicado:
            listanueva.append(i)
        indice1+=1
    return listanueva


        
def archivo():
    archivo=open("texto.txt","r")
    lista=[]
    for linea in archivo.readlines():
        lista.append(linea)
    return lista
                 

def inversa(cadena):
    invertida=""
    long=len(cadena)
    while long>=1:
        invertida+=cadena[long-1]
        long=long-1
    return invertida

def es_palindromo(cadena):
    return cadena==inversa(cadena)
 
def palindromos(lista):
    for i in lista:
        if es_palindromo(i):
            print (i)

palindromos(["radar","ana","loco","oro","pepe","salas"])                 
              


        
