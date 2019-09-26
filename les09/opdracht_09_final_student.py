def geef_rangnummer(stations, station):
    """
    Geeft het rangnummer (positie) van het station op een traject van stations.

    Argumenten:
    stations -- de stationsnamen die samen een treintraject vormen (list van str)
    station  -- de naam van een station (str)

    Retourneert het rangnummer van het station of -1 als het station niet op het traject voorkomt.
    """
    return


def bereken_ritprijs(afstand, prijs_per_station):
    """"
    Berekent de ritprijs.

    Argumenten:
    afstand -- de afstand in aantal stations (int)
    prijs_per_station -- de prijs om één station verder te reizen (float)

    Retourneert de prijs om over gegeven afstand te reizen (float)
    """
    return


traject = ['Schagen', 'Heerhugowaard']     # etc...

# Hier komt het hoofdprogramma
print("Uw rit:")


"""
========================================================================================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_traject():
    assert len(traject) == 15, f"Fout: je traject Schagen-Maastricht is nog niet compleet."


def test_geef_rangnummer():
    for station, test_rangnr in zip(traject, range(1, 16)):
        code_rangnr = geef_rangnummer(traject, station)
        assert code_rangnr == test_rangnr, f"Fout: geef_rangnummer() geeft {code_rangnr} in plaats van {test_rangnr} bij {station}."

    code_rangnr = geef_rangnummer(traject, "Amsterdam")
    assert code_rangnr == -1, f"Fout: geef_rangnummer() geeft {code_rangnr} in plaats van -1 bij 'Amsterdam'."


def test_bereken_ritprijs():
    assert bereken_ritprijs(0, 0) == 0, \
        f"Fout: bereken_ritprijs() geeft {bereken_ritprijs(0, 0)} in plaats van 0."
    assert bereken_ritprijs(0, 5) == 0, \
        f"Fout: bereken_ritprijs() geeft {bereken_ritprijs(0, 5)} in plaats van 0."
    assert bereken_ritprijs(5, 0) == 0, \
        f"Fout: bereken_ritprijs() geeft {bereken_ritprijs(5, 0)} in plaats van 0."
    assert bereken_ritprijs(5, 5) == 25, \
        f"Fout: bereken_ritprijs() geeft {bereken_ritprijs(5, 5)} in plaats van 25."
    assert bereken_ritprijs(5, 5.0) == 25.0, \
        f"Fout: bereken_ritprijs() geeft {bereken_ritprijs(5, 5.0)} in plaats van 25.0."


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_traject()

        test_geef_rangnummer()
        print("Je functie geef_rangnummer() doorstaat de tests!")
        test_bereken_ritprijs()
        print("Je functie bereken_ritprijs() doorstaat de tests!")

        print("Je mag deze Final Assignment nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
