# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:19:22 2022

Nombre: Gustavo Reyes Herrera
RUT: 21023531-0

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

def imprimir_colores(*args):
    for color in args:
        print(color.upper())

def main():
    colores = []
    color = input("Ingrese su color favorito, para salir, escriba 'salir': ")
    while color != "salir":
        colores.append(color)
        color = input("Ingrese su color favorito, para salir, escriba 'salir': ")
        
    imprimir_colores(*colores)

if __name__ == '__main__':
    main()