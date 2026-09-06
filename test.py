from fibonacci import fibonacci
from somme import somme
from longueur import longueur
from puissance import puissance
from palindrome import palindrome
from maximum import maximum



def test_somme():
    assert somme([3, 1, 4]) == 8
    assert somme([]) == 0

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(10) == 55

def test_longueur():
    assert longueur([3, 1, 4]) == 3
    assert longueur([]) == 0

def test_puissance():
    assert puissance(2, 0) == 1
    assert puissance(2, 3) == 8
    assert puissance(3, 4) == 81

def test_palindrome():
    assert palindrome("kayak") == True
    assert palindrome("kayaks") == False
    assert palindrome("") == True
    assert palindrome("a") == True

def test_maximum():
    assert maximum([3, 1, 4]) == 4
    assert maximum([-1, -5, -3]) == -1
    assert maximum([42]) == 42
    assert maximum([]) == None

def test_all():
    test_somme()
    test_fibonacci()
    test_longueur()
    test_puissance()
    test_palindrome()
    test_maximum()

if __name__ == "__main__":
    test_all()
    print("Tous les tests sont passés.")
    