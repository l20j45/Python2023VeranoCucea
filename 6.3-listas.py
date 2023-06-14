milista = [4,5,7,2,87,54,32]
print(milista)
print(milista[5])
print(len(milista))
milista.append(13)
print(milista)
milista.sort()

for element in milista:
    print(f"element {element}")

for count, element in enumerate(milista):
    print(f"contador {count} element {element}")
    
if 7 in milista:
    print("si esta el siete")
    print(milista.index(7))