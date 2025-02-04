# Exploring Web Technologies and Python Programming

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    
    print(f"Name: {name}")
    print("Abilities:", abilities)
else:
    print("Failed to retrieve data")


def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

pokemon_data = [pokemon for pokemon in pokemon_data if pokemon is not None]

average_weight = calculate_average_weight(pokemon_data)

for pokemon in pokemon_data:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Name: {name}")
    print("Abilities:", abilities)
print(f"Average Weight: {average_weight}")


# Exploring the Digital Cosmos with Python and the Web
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    response = requests.get(url)
    
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']  
            mass = planet['mass']['massValue']  
            orbit_period = planet['sideralOrbit']  
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    response = requests.get(url)
    
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']  
            mass = planet['mass']['massValue']  
            orbit_period = planet['sideralOrbit']
            planet_data.append((name, mass, orbit_period))
    
    return planet_data

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda x: x[1])
    return heaviest_planet

planets = fetch_planet_data()

name, mass, _ = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")