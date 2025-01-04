import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '70079f53b7731ae36decefbbce154291'
HEADER = {'Content-type': 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "180037",
    "name": "estoner",
    "photo_id": 1
}

body_in_pokeball = {
    "pokemon_id": "180037"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change) 
print(response_change.text)'''

response_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeball)
print(response_in_pokeball.text)