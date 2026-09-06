def puissance(x, n):
    if n == 0:
        return 1
    moitie = puissance(x, n // 2)
    if n % 2 == 0:
        return moitie * moitie
    return x * moitie * moitie