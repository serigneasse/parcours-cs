def inverse(chaine):
    if chaine == "":                     # cas de base : rien à renverser
        return ""
    return inverse(chaine[1:]) + chaine[0]