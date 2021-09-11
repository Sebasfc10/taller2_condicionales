# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:48:14 2021

@author: jeha2
"""

"""
Hacer un algoritmo que calcule el total a pagar por la compra de
camisas. Si se compran tres camisas o mas se aplica un descuento
del 30% sobre el total de la compra y si son menos de tres camisas
un descuento del 10%.
"""
compra = int(input('¿Cuantas camisas desea comprar? : '))
if compra >= 3:
    print('se aplicara un descuento del 30%')
else:
    print('se aplicara un descuento del 10%')