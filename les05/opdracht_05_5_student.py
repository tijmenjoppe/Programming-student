def kwadraten_som(grondgetallen):
    """Sommeert de kwadraten van gegeven *grondgetallen*."""
    return


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_kwadraten_som():
    lst, som = [], 0
    assert kwadraten_som(lst) == som, "Fout: kwadraten_som({}) geeft {} in plaats van {}".format(lst, kwadraten_som(lst), som)

    lst, som = [4, 5, 3], 50
    assert kwadraten_som(lst) == som, "Fout: kwadraten_som({}) geeft {} in plaats van {}".format(lst, kwadraten_som(lst), som)

    lst, som = [4, 5, 3, -81], 50
    assert kwadraten_som(lst) == som, "Fout: kwadraten_som({}) geeft {} in plaats van {}".format(lst, kwadraten_som(lst), som)

    lst, som = [-4, -5, -3, -81], 0
    assert kwadraten_som(lst) == som, "Fout: kwadraten_som({}) geeft {} in plaats van {}".format(lst, kwadraten_som(lst), som)


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_kwadraten_som()
        print("Je functie kwadraten_som() doorstaat de tests! Je mag deze opdracht nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
