def fibonacci(n, memo=None):
    if memo is None:        # le piège du dictionnaire par défaut, évité
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def inverse(chaine):
    if chaine == "":                     # cas de base : rien à renverser
        return ""
    return inverse(chaine[1:]) + chaine[0]

def longueur(t):
    if t == []:                    # cas de base
        return 0
    return 1 + longueur(t[1:])     # on retourne, et on combine

def maximum(t, plus_grand=None, index=0):
    if index == len(t):
        return plus_grand
    if plus_grand is None or t[index] > plus_grand:
        plus_grand = t[index]
    return maximum(t, plus_grand, index + 1)   # un seul retour, dans tous les cas

def palindrome(chaine):
    if len(chaine) <= 1:                 # 0 ou 1 caractère : toujours vrai
        return True
    if chaine[0] != chaine[-1]:          # extrémités différentes : fini
        return False
    return palindrome(chaine[1:-1])      # on retire les deux bouts

def puissance(x, n):
    if n == 0:
        return 1
    moitie = puissance(x, n // 2)
    if n % 2 == 0:
        return moitie * moitie
    return x * moitie * moitie

def somme(t, i=0):
    if i == len(t):          # 1. cas de base — quand on s'arrête
        return 0
    return t[i] + somme(t, i + 1)   # 2. on réduit  3. on combine