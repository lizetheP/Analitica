def pies_metros(pies):
    return pies * .3048

def main():
    pies = float(input("Dame los pies: "))
    res = pies_metros(pies)
    print("%.2f pies equivalen a %.2f metros" % (pies, res))
    
    pies_metros2 = lambda pies : pies * 0.3048
    resultado = pies_metros2(pies)
    print("%.2f pies equivalen a %.2f metros" % (pies, resultado))

main()