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
    print(f'la cuota final a pagar es de {cf} con una fianza del 2%')
    
"""
Una fábrica ha sido sometida a un programa de control de
contaminación para lo cual se efectúa una revisión de los puntos de
contaminación generados por la fábrica. El programa de control de
contaminación consiste en medir los puntos que emite la fábrica en
cinco días de una semana y si el promedio es superior a los 170
puntos entonces tendrá la sanción de parar su producción por una
semana y una multa del 50% de las ganancias diarias cuando no se
detiene la producción. Si el promedio obtenido de puntos es de 170 o
menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
desea saber cuanto dinero perderá después de ser sometido a la
revisión.
"""
pts = int(input('ingrese los puntos de la revision: '))
dinero = float(input('ingrese el dinero ganado en la produccion: '))
if pts > 170:
    d = dinero * 50/100
    perder = dinero - d
    print(f'tendran una multa del 50% y perdera {perder}')
if pts < 170:
    print('no perdera nada')

"""
Una persona se encuentra con un problema de comprar un automóvil
o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
mientras el automóvil se devalúa, con el terreno sucede lo contrario.
Esta persona comprará el automóvil si al cabo de tres años la
devaluación de este no es mayor que la mitad del incremento del valor del terreno. Ayúdale a esta pesona a determinar si debe o no
comprar el automóvil.
"""
precio = float(input('Ingrese el valor del automovil y del terreno : '))
terre = float(input('Ingrese el incremento anual del terreno % :'))
auto = float(input('Ingrese el valor de la devaluacion anual del automovil % :'))

terre = (((precio * terre)/100)*3)/2
auto = ((precio * auto)/100)*3
if auto < terre:
    print('te conviene el automovil')
else:
    print('te conviene el terreno')
    
    
"""
En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoreas que
compre. Si las computadoras son menos de cinco se les dará un 10%
de descuento sobre el total de la compra; si el número de
computadoras es mayor o igual a cinco pero menos de diez se le
otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
precio de cada computadora es de $11.000
"""

cant = int(input('ingrese el numero de computadoras que comprara: '))
pc = 11000
if cant < 5:
    pc = pc * cant 
    pc1 = pc * 10/100
    pagar = pc + pc1
    print(f'el valor final a pagar es {pc} con descuento del 10%')
if cant >= 5 and cant < 10:
    pc = pc * cant
    pc1 = pc * 20/100
    pagar = pc + pc1
    print(f'el valor final a pagar es {pc} con descuento del 20%')
if cant >= 10:
    pc = pc *cant 
    pc1 = pc * 40/100
    pagar = pc + pc1
    print(f'el valor final a pagar es {pc} con descuento del 40%')
    
"""
Un proveedor de estéreos ofrece un descuento del 10% sobre el
precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
independientemente de esto, ofrece un 5% de descuento si la marca
es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
cualquiera por la compra de su aparato. IVA es del 16%.
"""
valor = float(input('ingrese el valor del producto: '))
m = str(input('ingrese la marca en mayuscula: '))
i = valor *16/100
iva = valor + i

if valor >= 2000:
    if m == 'NOSY': 
        d = valor * 10/100
        v1 = valor - d
        v = v1 * 5/100
        v2= v1 - v
        final = v2 - i
        print(f'el valor final a pagar es de {final} si su compra es mayor de $2000')
    else:
        print(f'no es de marca favorita')
        d = valor * 10/100
        v1 = valor - d
   
"""
Una empresa quiere hacer una compra de varias piezas de la misma
clase a una fábrica de refacciones. La empresa, dependiendo del
monto total de la compra, decidirá que hacer para pagar al fabricante.
Si el monto total de la compra excede de $500.000 la empresa tendrá
la capacidad de invertir de su propio dinero un 55% del monto de la
compra, pedir prestado al banco un 30% y el resto lo pagará
solicitando un crédito al fabricante. Si el monto total de la compra no
excede de $500.00 la empresa tendrá capacidad de invertir de su
propio dinero un 70% y el restante 30% lo pagará solicitando crédito
al fabricante. El fabricante cobra por concepto de interes un 20%
sobre la cantidad que se le pague a crédito. Obtener la cantidad a
inverir, valor del préstamo, valor del crédito y los intereses.
"""
pieza = int(input('ingrese el numero de piezas que comprara: '))
costo = float(input('ingrese el costos de las piezas: '))
total = pieza * costo
if total > 500000:
    inv = total * 0.55
    prt = total * 0.30
    crd = total * 0.15
else:
    inv = total * 0.70
    prt = 0
    crd = total * 0.30
interes =  crd *0.20
print(f'invertir {inv}, prestamo {prt}, creditos {crd} y el interes es {interes}')
    
        
    