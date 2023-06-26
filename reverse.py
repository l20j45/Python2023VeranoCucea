palabra = input('Ingrese una palabra: ')
palabra = palabra.replace(' ', '').lower()
newpalabra = ''
for i in palabra[::-1]:
    newpalabra += i