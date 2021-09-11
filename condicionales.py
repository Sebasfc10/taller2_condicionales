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

"""
En un supermercado se hace una promoción, mediante la cual el
cliente obtiene un descuento dependiendo de un número que se
escoge al azar. Si el número escogido es menor que 74 el descuento
es del 15% sobre el total de la compra, si es mayor o igual a 74 el
descuento es del 20%. Obtener cuanto dinero se le descuenta.
"""
compra = float(input("su compra tiene un total de: "))
numero = int(input('ingrese su numero de su promocion: '))
if numero < 74:
    d = compra *15/100
    descuento = compra - d
    print(f'el total a pagar es de {descuento} con un descuento del 15%')
if numero >= 74:
    d = compra * 20/100
    descuento = compra - d
    print(f'el total a pagar es de {descuento} con un descuento del 20%')
    
"""
Una compañía de seguros está abriendo un departamento de
finanzas y estableció un programa para captar clientes, que consiste
en lo siguiente: Si el monto por el que se efectúa la fianza es menor
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
es mayor que $50.000 la cuota a pagar será el 2% del monto. La
afianzadora desea determinar cual será la cuota que debe pagar al
cliente.
"""
cuota = float(input('ingrese el valor de la fianza: '))
if cuota <= 50000:
    f = cuota * 3/100
    cf = cuota + f
    print(f'la cuota final a pagar es de {cf} con una fianza del 3%')
if cuota > 50000:
    f = cuota * 2/100
    cf = cuota + f
    print(f'la cuota final a pagar es de {cf} con una fuianza del 2%')
