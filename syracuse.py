def syracuse(n):
    tv = 0
    tva = 0
    u0 = n
    am = u0
    d = True
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        tv = tv + 1

        if am < n:
            am = n
        if d:
            if n < u0:
                tva = tv - 1
                d = False   
    return tv,am,tva   

def main():
    # exemple d'exécution
    n = 15
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

if __name__ == "__main__":
    main()
    résultat = syracuse(15)
    print(résultat)