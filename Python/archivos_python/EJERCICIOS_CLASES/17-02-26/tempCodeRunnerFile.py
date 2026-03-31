import requests


def get_pokedata(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    print("No fue posible conectarse...")
    return None


def get_pokeinfo(data):
    name = data["name"]
    height = data["height"]
    weight = data["weight"]

    sprites = data["sprites"]

    print(f"Nombre {name}")
    print(f"Altura {height}")
    print(f"Peso: {weight}")
    print(
        f"url img : {sprites.get("other").get("official-artwork").get("front_default")}"
    )


informacion_pokemon = get_pokedata(25)


if informacion_pokemon:
    get_pokeinfo(informacion_pokemon)
else:
    print("Error al recuperar información")
