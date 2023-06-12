""" import funciones
import time
 """
from funciones import clear
from time import sleep
descuento:float = 0


while cantidaDeManzanas != 0:
    funciones.clear()
    cantidaDeManzanas:int = int(input("Cuantas manzanas vendieron: (si pones un 0 me salgo)"))
    if cantidaDeManzanas == 0:
        break
    precioDeManzanas:int = int(input("Ingresa el precio de las manzanas: "))
    name:str = input("Ingresa tu nombre: ")
    descuentoLeyenda = ''

    if name == "daniel" or cantidaDeManzanas == 18 :
        descuento = (precioDeManzanas * cantidaDeManzanas) *.2
        descuentoLeyenda = 'tu descuento es del 20 %'
    elif cantidaDeManzanas >10:
        descuento = (precioDeManzanas * cantidaDeManzanas) *.1 
        descuentoLeyenda = 'tu descuento es del 10%'

        
    print('Nota de venta'.center(50,'x'))
    print(f"las manzanas estas en : {precioDeManzanas} y fueron : {cantidaDeManzanas}")

    if (descuento > 0):
        print(f"y el descuento fue de : {descuento} \n{descuentoLeyenda}")
        
    print(f"total a pagar : {(precioDeManzanas*cantidaDeManzanas)-descuento}")
    sleep(3)
