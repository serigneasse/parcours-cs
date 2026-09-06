def fibonacci(n, memo=None):
    if memo is None:        # le piège du dictionnaire par défaut, évité
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]