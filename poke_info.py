import requests

def get_pokemon(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    # Requête à l'API pour récupérer les infos du Pokémon
    r = requests.get(url)

    if r.status_code == 404:
        print("Pokemon introuvable")
        return

    # Conversion de la réponse JSON en dictionnaire Python
    data = r.json()

    nom = data["name"].upper()
    poids = data["weight"]
    taille = data["height"]
    # Récupération de la liste des types du Pokémon
    types = [t["type"]["name"] for t in data["types"]]

    print("Nom:", nom)
    print("Poids:", poids)
    print("Taille:", taille)
    print("Types:", ", ".join(types))


pokemon = input("Nom du pokemon: ")
get_pokemon(pokemon)