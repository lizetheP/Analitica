metros = float(input("Dame los metros: "))
metros_pies = lambda metros : metros / 0.3048
resultado = metros_pies(metros)
print("%.2f metros equivalen a %.2f metros" % (metros, resultado))

