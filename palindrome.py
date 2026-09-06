def palindrome(chaine):
    if len(chaine) <= 1:                 # 0 ou 1 caractère : toujours vrai
        return True
    if chaine[0] != chaine[-1]:          # extrémités différentes : fini
        return False
    return palindrome(chaine[1:-1])      # on retire les deux bouts