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
    cases = [(12, False, -10,  0.00),
             (12, False, -10,  0.00),
             (12, False,  50, 40.00),
             (12, False,  51, 45.60),
             (64, False, -10,  0.00),
             (64, False,  50, 40.00),
             (64, False,  51, 45.60),

             (12,  True, -10,  0.00),
             (12,  True,  50, 24.00),
             (12,  True,  51, 27.36),
             (64,  True, -10,  0.00),
             (64,  True,  50, 24.00),
             (64,  True,  51, 27.36),

             (11, False, -10,  0.00),
             (11, False,  50, 28.00),
             (11, False,  51, 31.92),
             (65, False, -10,  0.00),
             (65, False,  50, 28.00),
             (65, False,  51, 31.92),

             (11,  True, -10,  0.00),
             (11,  True,  50, 26.00),
             (11,  True,  51, 29.64),
             (65,  True, -10,  0.00),
             (65,  True,  50, 26.00),
             (65,  True,  51, 29.64)]

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

