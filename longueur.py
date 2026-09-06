def longueur(t):
    if t == []:                    # cas de base
        return 0
    return 1 + longueur(t[1:])     # on retourne, et on combine