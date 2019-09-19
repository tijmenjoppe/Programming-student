def lang_genoeg(lengte):
    """ Geeft bericht of iemand lang genoeg is voor de attractie."""
    return ""


"""
========================================================================================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import hashlib


def test_lang_genoeg():
    res1 = "0ca9ddb266e1f9e2bdb7976fd347ab07"
    res2 = "1fc6e9419705055a33b1f8044ce93171"

    assert hashlib.md5(lang_genoeg(100).encode()).hexdigest() == res1, "Fout: de functie lang_genoeg() geeft niet het juiste bericht bij 100cm."
    assert hashlib.md5(lang_genoeg(200).encode()).hexdigest() == res2, "Fout: de functie lang_genoeg() geeft niet het juiste bericht bij 200cm."
    assert hashlib.md5(lang_genoeg(119).encode()).hexdigest() == res1, "Fout: de functie lang_genoeg() geeft niet het juiste bericht bij 119cm."
    assert hashlib.md5(lang_genoeg(120).encode()).hexdigest() == res2, "Fout: de functie lang_genoeg() geeft niet het juiste bericht bij 120cm."


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_lang_genoeg()
        print("Je functie lang_genoeg() doorstaat de tests! Je mag deze opdracht nu inleveren op Canvas... ")

    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
