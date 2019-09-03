def standaardprijs(afstandKM):
    """Bepaal de standaardprijs op basis van *afstandKM*."""
    return 0.0


def ritprijs(leeftijd, weekendrit, afstandKM):
    """Bepaal de ritprijs op basis van *leeftijd*, *weekendrit* en *afstandKM*."""
    return 0.0


"""
========================================================================================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_ritprijs():
    cases = [(12, False, -10, 0.0),
             (12, False, -10, 0.0),
             (12, False, 50, 40.0),
             (12, False, 51, 45.6),
             (64, False, -10, 0.0),
             (64, False, 50, 40.0),
             (64, False, 51, 45.6),

             (12, True, -10, 0.0),
             (12, True, 50, 40.0 * .6),
             (12, True, 51, 45.6 * .6),
             (64, True, -10, 0.0),
             (64, True, 50, 40.0 * .6),
             (64, True, 51, 45.6 * .6),

             (11, False, -10, 0.0),
             (11, False, 50, 40.0 * .7),
             (11, False, 51, 45.6 * .7),
             (65, False, -10, 0.0),
             (65, False, 50, 40.0 * .7),
             (65, False, 51, 45.6 * .7),

             (11, True, -10, 0.0),
             (11, True, 50, 40.0 * .65),
             (11, True, 51, 45.6 * .65),
             (65, True, -10, 0.0),
             (65, True, 50, 40.0 * .65),
             (65, True, 51, 45.6 * .65)]

    for case in cases:
        assert round(ritprijs(case[0], case[1], case[2]), 2) == round(case[3], 2),\
            "Fout: ritprijs({}, {}, {}) geeft {} in plaats van {}".format(case[0], case[1], case[2], ritprijs(case[0], case[1], case[2]), case[3])


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_ritprijs()
        print("Je functie ritprijs() doorstaat de tests! Je mag deze opdracht nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))

