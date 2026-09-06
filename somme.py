def somme(t, i=0):
    if i == len(t):          # 1. cas de base — quand on s'arrête
        return 0
    return t[i] + somme(t, i + 1)   # 2. on réduit  3. on combine