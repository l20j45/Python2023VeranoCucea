word = 'Hola topo'
comprobacionA = comprobacionE = comprobacionI = comprobacionO = comprobacionU = False
for letter in word:
    if 'a' in letter.lower() and comprobacionA == False:
        print('a')
        comprobacionA = True
    if 'e' in letter.lower() and comprobacionE == False:
        print('e')
        comprobacionE = True
    if 'i' in letter.lower() and comprobacionI == False:
        print('i')
        comprobacionI = True
    if 'o' in letter.lower() and comprobacionO == False:
        print('o')
        comprobacionO = True
    if 'u' in letter.lower() and comprobacionU == False:
        print('u')
        comprobacionU = True
