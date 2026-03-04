from analyseur import compter_lignes
from analyseur import compter_mots
from analyseur import top_mots
def test_lignes():
    texte = "Ligne 1\nLigne 2\nLigne 3"
    assert compter_lignes(texte) == 3

def test_mots():
    texte = "Bonjour, le monde !"
    assert compter_mots(texte) == 3

def test_top():
    texte = "pomme poire pomme banane pomme poire"

    resultat = dict(top_mots(texte))

    assert resultat["pomme"] == 3
    assert resultat["poire"] == 2