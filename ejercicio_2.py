# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:22:27 2022

Nombre: Gustavo Reyes Herrera
RUT: 21023531-0

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

def main():

    primos = lambda n: [x for x in range(2, n) if all(x % y != 0 for y in range(2, x))]

    lista_primos = primos(1000)
    
    print(lista_primos)

if __name__ == '__main__':
    main()