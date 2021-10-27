from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in self.pokemons:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon_name)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}" + "\n" + f"Pokemon count {len(self.pokemons)}"
        for pokemon in self.pokemons:
            result += "\n"
            result += f"{pokemon.pokemon_details()}"
        return result
