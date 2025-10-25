import time
import random
from controllers.controller import fetch_pokemon_data, add_pokemon_to_db

def main():
    while True:
        pokemon_id = random.randint(1,350)
        pokemon_schema = fetch_pokemon_data(pokemon_id)

        if pokemon_schema:
            add_pokemon_to_db(pokemon_schema)
            print(f"Pokemon {pokemon_schema.name} adicionado ao banco de dados.")
        else:
            print(f"Não foi possível obter dados para o Pokemon com ID {pokemon_id}")
        time.sleep(5)

if __name__ == "__main__":
    main()