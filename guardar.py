import json
import os
from pathlib import Path
 
import requests
 
 
 
def show_image_and_stats(response_json):
    print(f"Weight: {response_json['weight']}")
    print(f"First ability: {response_json['abilities'][0]['ability']['name']}")
 
    image_url = response_json["sprites"]["other"]["home"]["front_default"]
    os.system(f"open {image_url}")
 
 
def save_info(response_json, pokemon_name):
    base_dir = Path(__file__).resolve().parent
    pokedex_dir = base_dir / "pokedex"
    path = pokedex_dir / f"{pokemon_name}.json"
 
    with open(path, "w") as fh:
        json.dump(response_json, fh, indent=4)
 
 
def main():
    pokemon_name = "ditto"
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    status_code = response.status_code
    
    if status_code >= 400 and status_code <= 599:
        print(f"El pokemon: '{pokemon_name}' no existe")
    else:
        response_json = response.json()
        show_image_and_stats(response_json)
        save_info(response_json, pokemon_name)
 

 
 
if __name__ == "__main__":
    main()



    

