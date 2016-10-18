'''
Created on 20 de sept. de 2016

@author: lagarto
'''

def  max(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
    else:
        print ("son iguales")
        return

def max_de_tres(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    elif num3>num1 and num3>num2:
        return num3
    else:
        print("Son iguales")
        return
    
def len(cadena):
    longitud=0
    for i in cadena:
        longitud+=1
    return longitud

def vocal(caracter):
    return caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u"

def sum(lista):
    total=0
    for i in lista:
        total+=i
    return total 
  
def multip(lista):
    total=1
    for i in lista:
        total*=i
    return total

def inversa(cadena):
    invertida=""
    long=len(cadena)
    while long>=1:
        invertida+=cadena[long-1]
        long=long-1
    return invertida

def es_palindromo(cadena):
    return cadena==inversa(cadena)
    
def superposicion(lista1, lista2):
    for e1 in lista1:
        for e2 in lista2:
            if e1==e2:
                return True
    return False        
def n_caracteres(num, car):
    resultado=""
    while num>=1:
        resultado+=car
        num-=1
    return resultado

def procedimiento(lista):
    for i in lista:
        print(n_caracteres(i,"*"))

def max_in_list(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def mas_larga(lista):
    larga=""
    for i in lista:
        if len(i)>len(larga):
            larga=i
    return larga

def filtrar_palabras(lista, n):
    for i in lista:
        if len(i)>n:
            print(i)

def mayusculas():
    cadena=input("Ingresa una cadena de texto:")
    mayuscula=0
    for i in cadena:
        if i!=i.lower():
            mayuscula+=1
    return mayuscula 

def aDecimal(binario):
    decimal=0
    binario= str(binario)
    exponente=len(binario)-1
    for i in binario:
        decimal+=(int(i)*2**(exponente))
        exponente-=1
    return decimal

def curso():
    ano=input("Introduce el ano en curso:")
    nombre1=input("Introduce el nombre de la primera persona:")
    nombre2=input("Introduce el nombre de la segunda persona:")
    nombre3=input("Introduce el nombre de la tercera persona:")
    nacimiento1=input("Introduce el ano de nacimiento de la primera persona") 
    nacimiento2=input("Introduce el ano de nacimiento de la segunda persona") 
    nacimiento3=input("Introduce el ano de nacimiento de la tercera persona")
    print(nombre1+" va a cumplir "+str(int(ano)-int(nacimiento1))+" anos este curso")
    print(nombre2+" va a cumplir "+str(int(ano)-int(nacimiento2))+" anos este curso") 
    print(nombre3+" va a cumplir "+str(int(ano)-int(nacimiento3))+" anos este curso")
    return

def mayores_a(lista,num):
    for i in lista:
        if i>num:
            print(i)
            
def comienzan_por(lista):
    letra=input("Introduzca la letra deseada:")
    for i in lista:
        if i[0]==letra:
            print (i)
    return
            
def contar_vocales():
    palabra=input("Introduzca la palabra:")
    vocales=0
    for i in palabra:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            vocales+=1
    return vocales

def es_bisiesto(ano):
    return (ano%4==0 and ano%100!=0) or ano%400==0
    
    
if __name__ == '__main__':
    print(es_bisiesto(2010))
    pass                           