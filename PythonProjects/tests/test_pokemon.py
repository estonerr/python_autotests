import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '70079f53b7731ae36decefbbce154291'
HEADER = {'Content-type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18015'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
 
def test_name_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'estoner'



    