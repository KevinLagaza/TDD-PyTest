from src.leJustePrix import LeJustePrix


def test_Comparaison_Plus():
    res = LeJustePrix().comparaison(2, 3)
    # <assert> permet de verifier une condition
    assert res == "PLUS"

def test_Comparaison_Moins():
    res = LeJustePrix().comparaison(7, 5)
    # <assert> permet de verifier une condition
    assert res == "MOINS"

def test_Comparaison_Gagne():
    res = LeJustePrix().comparaison(9, 9)
    # <assert> permet de verifier une condition
    assert res == "GAGNÉ"

def test_Retirer_Nbre_de_Vie():
    res = LeJustePrix().retirer_nbre_vies(5)
    # <assert> permet de verifier une condition
    assert res == 4