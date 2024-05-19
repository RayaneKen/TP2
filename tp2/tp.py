import json
import csv


with open('txt.json', 'r') as f:
    nombres = json.load(f)
with open('nombre.csv', 'w', newline='') as x:
    lecteur = csv.writer(x)
    lecteur.writerow(['reel', 'imaginaire'])
    lecteur.writerows(nombres)

#--------------------------------------------------------


def charger_pokemons_csv(f):
    pokemons = {}
    with open(f, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nom = row[0]
            stats = list(map(int, row[1:]))
            pokemons[nom] = stats
    return pokemons
    
pkmn = charger_pokemons_csv('pokemon.csv')
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
