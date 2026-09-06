def maximum(t, plus_grand=None, index=0):
    if index == len(t):
        return plus_grand
    if plus_grand is None or t[index] > plus_grand:
        plus_grand = t[index]
    return maximum(t, plus_grand, index + 1)   # un seul retour, dans tous les cas