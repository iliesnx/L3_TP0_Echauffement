import requests

def get_pokemon(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    r = requests.get(url)

    if r.status_code == 404:
        print("Pokemon introuvable")
        return

    data = r.json()

    nom = data["name"].upper()
    poids = data["weight"]
    taille = data["height"]
    types = [t["type"]["name"] for t in data["types"]]

    print("Nom:", nom)
    print("Poids:", poids)
    print("Taille:", taille)
    print("Types:", ", ".join(types))


pokemon = input("Nom du pokemon: ")
get_pokemon(pokemon)