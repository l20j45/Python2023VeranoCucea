print("\t Convertidor de pesos a dolares")
print("+--------------------+----------+".center(100,"x"))

pesos = int(input("¿Cuantos pesos quieres convertir? "))
valor_dolar = float(input("¿En cuanto se encuenta el Dolar? "))

conversion = float(pesos / valor_dolar)


print("+--------------------+----------+".center(30,"x"))

print(f"Su equivalente en dolares es: {conversion}")