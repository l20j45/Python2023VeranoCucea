import funciones
import time
import os

def saludo():
    print("Hola buenos dias")
    
def suma(number1, number2):
    number1 *= number1
    number2 *= number2
    total = number1 + number2
    return total
    
       
    
name = "lizeth"
numero1 = 2
numero2 = 2
total = 3
funciones.clear(name)
saludo()
total = suma(numero1, numero2)
time.sleep(2)
print(numero1)
print(numero1)
print(total)
print("Salio")