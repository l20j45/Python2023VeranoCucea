precioDeManzanas:int = int(input("Ingresa el precio de las manzanas: "))
cantidaDeManzanas:int = int(input("Cuantas manzanas vendieron: "))

print("Vas a pagar")
# soy un comentario
"""
    comentario multi linea
    """
    
 # CONCATENACION   
print(f"las manzanas estas en : {precioDeManzanas} y fueron : {cantidaDeManzanas}")
print("y fueron : " + str(cantidaDeManzanas))
print("total a pagar : " + str(precioDeManzanas*cantidaDeManzanas))