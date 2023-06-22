from pokemon import Pokemon


class Pokedex:
    def __init__(self):
        self.pokemon_list: list[Pokemon]
        self.pokemon_list = []

    def add_pokemon(self, new_pokemon: Pokemon) -> None:
        for pokemon in self.pokemon_list:
            if pokemon.index == new_pokemon.index:
                print("Pokémon já cadastrado!!")
                return None

        self.pokemon_list.append(new_pokemon)
        print("Pokemon cadastrado com sucesso!!")
        return None

    def get_pokemon_by_index(self, index: int) -> [Pokemon, None]:
        if len(self.pokemon_list) == 0:
            print("Pokedex vazia!!")
            return None

        for pokemon in self.pokemon_list:
            if pokemon.index == index:
                return pokemon

        print("Pokémon não encontrado!!")
        return None

    def get_all_pokemon(self) -> [list, None]:
        if len(self.pokemon_list) == 0:
            print("Pokedex vazia!!")
            return None

        return self.pokemon_list

    def remove_pokemon(self, index: int) -> None:
        pokemon_to_remove = self.get_pokemon_by_index(index)

        if pokemon_to_remove:
            self.pokemon_list.remove(pokemon_to_remove)
            print("Pokémon removido com sucesso!!")
