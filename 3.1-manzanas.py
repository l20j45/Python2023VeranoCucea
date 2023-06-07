descuento:float = 0
precioDeManzanas:int = int(input("Ingresa el precio de las manzanas: "))
cantidaDeManzanas:int = int(input("Cuantas manzanas vendieron: "))

if cantidaDeManzanas >10:
    descuento = (precioDeManzanas * cantidaDeManzanas) *.1 
   
print(f"las manzanas estas en : {precioDeManzanas} y fueron : {cantidaDeManzanas}")
if (descuento > 0):
    print(f"y el descuento fue de : {descuento}")
print("total a pagar : " + str((precioDeManzanas*cantidaDeManzanas)-descuento))