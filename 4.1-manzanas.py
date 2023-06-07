descuento:float = 0
precioDeManzanas:int = int(input("Ingresa el precio de las manzanas: "))
cantidaDeManzanas:int = int(input("Cuantas manzanas vendieron: "))
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