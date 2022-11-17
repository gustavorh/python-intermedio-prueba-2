# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:56:55 2022

Nombre: Gustavo Reyes Herrera
RUT: 21023531-0

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

def calcularPromedio(lista1, lista2, lista3):
    promedio = lambda x, y, z: (x + y + z) / 3
    print(promedio)

def main():
    lista1 = [4, 5, 6, 7, 4, 3]
    lista2 = [5, 6, 4, 3, 3, 3]
    lista3 = [6, 6, 5, 4, 3, 3]
    
    #promedio = lambda x, y, z: (x + y + z) / 3
    
    for i in range(6):
        calcularPromedio(lista1[i], lista2[i], lista3[i])
    
    #promedio = promedio(lista1[0], lista2[0], lista3[0])
    #print(promedio)
    
    #promedio = promedio(lista1[1], lista2[1], lista3[1])
    #print(promedio)
    


if __name__ == '__main__':
    main()