def aantal_kluizen_vrij():
    """ Retourneert het aantal beschikbare kluizen (int). """
    pass


def kluis_uitgeven(code):
    """
    Geeft de eerst beschikbare kluis uit. Kluisnummer en code worden opgeslagen in kluizen.txt.

    Argumenten:
    code -- de opgegeven code (str)

    Retourneert het kluisnummer (int) dat is uitgegeven of -1 als het uitgeven van een kluis is mislukt.
    """
    pass


def kluis_openen(kluisnummer, code):
    """
    Opent een kluis.

    Argumenten:
    kluisnummer -- het nummer van de kluis (int)
    code -- de code behorend bij de kluis (str)

    Retourneert True als de kluis geopend kon worden, anders False.
    """
    pass


def kluis_teruggeven(kluisnummer, code):
    """
    Geeft een kluis terug. Bijbehorende regel wordt uit kluizen.txt verwijderd.

    Argumenten:
    kluisnummer -- het nummer van de kluis (int)
    code -- de code behorend bij de kluis (str)

    Retourneert True als de kluis teruggegeven kon worden, anders False.
    """
    pass


"""
Het hoofdprogramma met het menu.
"""
print("================= Menu =================")





"""====================================================[ TEST ]=========================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_aantal_kluizen_vrij():
    cases = [('11;6754\n1;geheim\n5;kluisvanpietje\n12;z@terd@g\n', 8),
             ('1;ww1\n2;ww2\n3;ww3\n4;ww4\n5;ww5\n6;ww6\n7;ww7\n8;ww8\n9;ww9\n10;ww10\n11;ww11\n12;ww12\n', 0),
             ('', 12)]

    for case in cases:
        with open('kluizen.txt', 'w') as kluizen_db:
            kluizen_db.write(case[0])

        res = aantal_kluizen_vrij()
        assert res == case[1], (
            f"Fout: jouw functie aantal_kluizen_vrij() geeft {res} in plaats van {case[1]}\n"
            f"als kluizen.txt de volgende inhoud zou bevatten:\n\n"
            f"---[ kluizen.txt]---\n{case[0]}--------------------"
        )


def test_kluis_uitgeven():
    res = kluis_uitgeven('a')

    assert type(res) == int, (
        f"Fout: jouw functie kluis_openen() retourneert een {type(res)} in plaats van een int."
    )

    assert res == -1, (
        f"Fout: jouw functie kluis_openen() accepteert een incorrecte code {'a'}."
    )

    cases = [('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 5),
             ('11;6754\n1;geheim\n5;kluisvanpietje\n12;z@terd@g\n', 2),
             ('1;ww1\n2;ww2\n3;ww3\n4;ww4\n5;ww5\n6;ww6\n7;ww7\n8;ww8\n9;ww9\n10;ww10\n11;ww11\n12;ww12\n', -1),
             ('', 1)]

    for case in cases:
        with open('kluizen.txt', 'w') as kluizen_db:
            kluizen_db.write(case[0])

        res = kluis_uitgeven('test')

        assert type(res) == int, (
            f"Fout: jouw functie kluis_openen() retourneert een {type(res)} in plaats van een int."
        )

        assert res == case[1], (
            f"Fout: jouw functie kluis_uitgeven(code) retourneert {res} in plaats van {case[1]}\n"
            f"als kluizen.txt de volgende inhoud zou bevatten:\n\n"
            f"---[ kluizen.txt]---\n{case[0]}--------------------"
        )

        if res > 0:
            with open('kluizen.txt', 'r') as kluizen_db:
                lines = kluizen_db.readlines()
            assert str(case[1]) + ';test' in lines[-1], (
                f"Fout: jouw functie kluis_uitgeven(code) slaat de uitgegeven kluis {case[1]}\n"
                f"niet goed op in kluizen.txt, als deze de volgende inhoud zou bevatten:\n\n"
                f"---[ kluizen.txt]---\n{case[0]}--------------------"
            )


def test_kluis_openen():
    cases = [('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 2, 'geheim', True),
             ('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 3, 'geenidee', False),
             ('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 5, 'geenidee', False),
             ('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 3, 'geheim', False)]

    for case in cases:
        with open('kluizen.txt', 'w') as kluizen_db:
            kluizen_db.write(case[0])

        res = kluis_openen(case[1], case[2])

        assert type(res) == bool, (
            f"Fout: jouw functie kluis_openen() retourneert een {type(res)} in plaats van een bool."
        )

        assert res == case[3], (
            f"Fout: jouw functie kluis_openen({case[1]}, {case[2]}) retourneert {res} in plaats van {case[3]}\n"
            f"als kluizen.txt de volgende inhoud zou bevatten:\n\n"
            f"---[ kluizen.txt]---\n{case[0]}--------------------"
        )


def test_kluis_teruggeven():
    cases = [('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 2, 'geheim', True),
             ('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 3, 'geenidee', False),
             ('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 5, 'geenidee', False),
             ('1;6754\n2;geheim\n3;kluisvanpietje\n4;z@terd@g\n', 3, 'geheim', False)]

    for case in cases:
        with open('kluizen.txt', 'w') as kluizen_db:
            kluizen_db.write(case[0])

        res = kluis_teruggeven(case[1], case[2])

        assert type(res) == bool, (
            f"Fout: jouw functie kluis_teruggeven() retourneert een {type(res)} in plaats van een bool."
        )

        assert res == case[3], (
            f"Fout: jouw functie kluis_teruggeven({case[1]}, {case[2]}) retourneert {res} in plaats van {case[3]}\n"
            f"als kluizen.txt de volgende inhoud zou bevatten:\n\n"
            f"---[ kluizen.txt]---\n{case[0]}--------------------"
        )

        with open('kluizen.txt', 'r') as kluizen_db:
            data = kluizen_db.read()

        if res:
            assert str(case[1]) + ';' + case[2] not in data, (
                f"Fout: jouw functie kluis_teruggeven({case[1]}, {case[2]}) lijkt de gegevens van de teruggegeven\n"
                f"kluis {case[1]} niet te verwijderen uit kluizen.txt, als deze de volgende inhoud zou bevatten:\n\n"
                f"---[ kluizen.txt]---\n{case[0]}--------------------"
            )

        assert case[0].count(chr(10))-res == data.count(chr(10)), (
            f"Fout: jouw functie kluis_teruggeven({case[1]}, {case[2]}) lijkt teveel gegevens te verwijderen\n"
            f"uit kluizen.txt, als deze de volgende inhoud zou bevatten:\n\n"
            f"---[ kluizen.txt]---\n{case[0]}--------------------"
        )


if __name__ == '__main__':
    with open('kluizen.txt') as kluizen_origineel:
        data_backup = kluizen_origineel.read()

    try:
        print("\x1b[0;32m")

        test_aantal_kluizen_vrij()
        print("Je functie aantal_kluizen_vrij() doorstaat de tests!")

        test_kluis_uitgeven()
        print("Je functie kluis_uitgeven() doorstaat de tests!")

        test_kluis_openen()
        print("Je functie kluis_openen() doorstaat de tests!")

        test_kluis_teruggeven()
        print("Je functie kluis_teruggeven() doorstaat de tests!")

        print("\nJe mag deze opdracht nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))

    with open('kluizen.txt', 'w') as kluizen_origineel:
        kluizen_origineel.write(data_backup)
