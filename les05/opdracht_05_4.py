def new_password(oldpassword, newpassword):
    """Controleer of *newpassword* voldoet aan de eisen om *oldpassword* te vervangen."""
    return False


def new_password2(oldpassword, newpassword):
    """Controleer of *newpassword* voldoet aan de eisen om *oldpassword* te vervangen én minstens 1 cijfer bevat."""
    return False


"""
========================================================================================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_new_password():
    assert new_password("hallo", "hallo") is False, "Fout: de functie new_password() accepteert het oude password - dat mag niet."
    assert new_password("hallo", "hello") is False, "Fout: de functie new_password() accepteert een password van minder dan 6 karakters - dat mag niet."
    assert new_password("hallo", "hallos") is True, "Fout: de functie new_password() accepteert een goed nieuw password niet."


def test_new_password2():
    assert new_password2("hallo", "hallo") is False,  "Fout: de functie new_password2() accepteert het oude password - dat mag niet."
    assert new_password2("hallo", "hello") is False,  "Fout: de functie new_password2() accepteert een password van minder dan 6 karakters - dat mag niet."
    assert new_password2("hallo", "hallos") is False, "Fout: de functie new_password2() accepteert een password zonder een cijfer - dat mag niet."
    assert new_password2("hallo", "hallo5") is True,  "Fout: de functie new_password2() accepteert een goed nieuw password niet."


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_new_password()
        print("Je functie test_new_password() doorstaat de tests! Je mag deze opdracht nu inleveren op Canvas...")

        test_new_password2()
        print("Je optionele uitbreiding test_new_password2() doorstaat de tests! Goed werk!")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
