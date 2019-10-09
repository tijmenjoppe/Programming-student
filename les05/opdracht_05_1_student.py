def som(getal1, getal2, getal3):
    """Return de som van drie gegeven getallen."""
    return


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_som():
    for i in range(10):
        lst = random.sample(range(-9, 10), 3)
        assert som(lst[0], lst[1], lst[2]) == sum(lst), "Fout: sum({},{},{}) geeft {} in plaats van {}".format(lst[0], lst[1], lst[2], som(lst[0], lst[1], lst[2]), sum(lst))


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_som()
        print("Je functie som() doorstaat de tests! Je mag deze opdracht nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
