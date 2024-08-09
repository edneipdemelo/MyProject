X = 0
Y = 1
RESULTADO = 0

while RESULTADO < 2000:
    RESULTADO = X + Y
    X = Y
    Y = RESULTADO
    if RESULTADO > 2000:
        break
    print(RESULTADO)