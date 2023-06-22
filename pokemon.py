class Pokemon:
    def __init__(self, index: int, name: str, attack: int, defense: int):
        self.index = index
        self.name = name
        self.attack = attack
        self.defense = defense

    def show_stats(self):
        print(f"index: {self.index} | "
              f"nome: {self.name} | "
              f"ataque: {self.attack} | "
              f"defesa: {self.defense}")
