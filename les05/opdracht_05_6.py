""" Schrijf (en test) de functie wijzig() met één parameter: letterlijst.
    Zorg dat de functie de lijst leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. """

def wijzig(letterlijst):
	pass


"""
=======================================================[ TEST ]=========================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_wijzig():
    lst = []
    wijzig(lst)
    assert lst == ['d', 'e', 'f'], "Fout: wijzig() werkt niet op een lege lijst."

    lst = ['a', 'b', 'c']
    wijzig(lst)
    assert lst == ['d', 'e', 'f'], "Fout: wijzig() werkt niet op een lijst gevuld met strings."

    lst = [0, 1, 2]
    wijzig(lst)
    assert lst == ['d', 'e', 'f'], "Fout: wijzig() werkt niet op een lijst gevuld met integers."


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_wijzig()
        print("Je functie doorstaat de tests! Je mag deze opdracht nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
