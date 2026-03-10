# Resolvendo a sequência Fibonacci...
A = 0; B = 1; X = 0

while X <= 2000:
    print(X)
    X = A + B
    A = B
    B = X
