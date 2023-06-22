from pokedex import Pokedex
from pokemon import Pokemon


pokedex = Pokedex()


def input_int(text) -> int:
    while True:
        try:
            value = int(input(text))
            break
        except Exception as error:
            print(f"{error}: Por favor digite um número inteiro!!")

    return value


valid_menu_options = ["0", "1", "2", "3", "4"]

while True:
    user_input = input("\n"
                       "1 para adicionar um pokémon a Pokédex\n"
                       "2 para procurar um pokémon\n"
                       "3 para ver quais são os pokémons cadastrados\n"
                       "4 para remover um pokémon\n"
                       "0 para sair\n"
                       "Digite uma das opções acima: ")

    if user_input not in valid_menu_options:
        while True:
            user_input = input("Por favor digite uma opção valida: ")

            if user_input in valid_menu_options:
                break

    if user_input == "1":
        while True:
            new_pokemon_index = input_int("\tDigite o index do novo pokémon: ")
            new_pokemon_name = input("\tDigite o nome do novo pokémon: ")
            new_pokemon_attack = input_int("\tDigite o ataque do novo pokémon: ")
            new_pokemon_defense = input_int("\tDigite o defesa do novo pokémon: ")

            new_pokemon = Pokemon(index=new_pokemon_index,
                                  name=new_pokemon_name,
                                  attack=new_pokemon_attack,
                                  defense=new_pokemon_defense)
            pokedex.add_pokemon(new_pokemon)

            while True:
                user_input_cadastro = input("\tCadastrar mais um pokémon? (S ou N): ").lower()
                if user_input_cadastro in ["s", "n"]:
                    break

            if user_input_cadastro == "n":
                break

    if user_input == "2":
        while True:
            pokemon_index = input_int("\tDigite o index do pokémon: ")
            pokemon = pokedex.get_pokemon_by_index(pokemon_index)

            if pokemon:
                pokemon.show_stats()

            while True:
                user_input_show = input("\tDeseja ver mais um pokémon? (S ou N): ").lower()
                if user_input_show in ["s", "n"]:
                    break

            if user_input_show == "n":
                break

    if user_input == "3":
        result = pokedex.get_all_pokemon()

        for pokemon in result:
            pokemon.show_stats()

    if user_input == "4":
        while True:
            pokemon_to_remove = input_int("\tDigite o index do pokémon a ser removido: ")
            pokedex.remove_pokemon(pokemon_to_remove)

            while True:
                user_input_remover = input("\tRemover mais um pokémon? (S ou N): ").lower()
                if user_input_remover in ["s", "n"]:
                    break

            if user_input_remover == "n":
                break

    if user_input == "0":
        print("Volte sempre!!")
        break
