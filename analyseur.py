import sys
import re
from collections import Counter

def lire_fichier(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def compter_lignes(texte):
    return texte.count("\n") + 1

def compter_mots(texte):
    # On utilise une expression régulière pour extraire tous les mots (insensible à la casse)
    mots = re.findall(r'\b\w+\b', texte.lower())
    return len(mots)

def top_mots(texte):
    # Extraction des mots comme ci-dessus
    mots = re.findall(r'\b\w+\b', texte.lower())
    # Utilisation de Counter pour compter les occurrences de chaque mot
    compteur = Counter(mots)
    return compteur.most_common(5)

def afficher_stats(texte):

    print("Lignes :", compter_lignes(texte))
    print("Mots :", compter_mots(texte))
    print("Top 5 :")

    for mot, count in top_mots(texte):
        print(mot, count)


if __name__ == "__main__":
    texte = lire_fichier(sys.argv[1])
    afficher_stats(texte)