def ciclo():
    d = 0
    r = 3
    s = r / 2
    while  s > 2 or r % 2 == 0:
        d = d + 1
        r = r - 2
        s = s - 2
    print(str(d) +  " " + str(r) + " " + str(s))

def main():
    ciclo()

main()
