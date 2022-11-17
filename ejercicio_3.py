# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:51:07 2022

Nombre: Gustavo Reyes Herrera
RUT: 21023531-0

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

from functools import reduce

def calculadora(lista):
    suma = reduce(lambda a, b: a+b, lista)
    print(f"La suma de los elementos de la lista {lista} es: {suma}")
    
    resta = reduce(lambda a, b: a-b, lista)
    print(f"La resta de los elementos de la lista {lista} es: {resta}")
    
    multiplicacion = reduce(lambda a, b: a*b, lista)
    print(f"La multiplicación de los elementos de la lista {lista} es: {multiplicacion}")
    
    division = reduce(lambda a, b: a/b, lista)
    print(f"La división de los elementos de la lista {lista} es: {division}")
    
    exponente = reduce(lambda a, b: a**b, lista)
    print(f"La exponente de los elementos de la lista {lista} es: {exponente}")
    
    raiz = reduce(lambda a, b: a**(1/b), lista)
    print(f"La raíz cuadrada de los elementos de la lista {lista} es: {raiz}")
    
    
def main():
    numeros = input("Ingrese una lista de números separados por un espacio (1 2 3...): ")
    lista_numeros = numeros.split()
    lista_numeros = list(map(lambda numeros: int(numeros), lista_numeros))
    
    calculadora(lista_numeros)

if __name__ == '__main__':
    main()