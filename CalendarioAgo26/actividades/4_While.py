def ciclo1():
    x = 8
    y = 3
    while y <= 16:
        x = x + 1
        y = y + 2
    print(x)
    print(y)

def ciclo2():
    x = 8
    y = 3
    while y <= 16:
        x = x + 1
        y = y + 2
    return x, y

def main():
    ciclo1()
    x, y = ciclo2()
    print()
    print(x)
    print(y)
    
main()
