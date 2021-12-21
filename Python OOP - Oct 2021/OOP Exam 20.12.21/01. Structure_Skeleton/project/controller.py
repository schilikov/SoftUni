class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        successfully_added = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                successfully_added.append(player)

        result = f"Successfully added: {', '.join(x.name for x in successfully_added)}"
        return result

    def add_supply(self, *args):
        for x in args:
            self.supplies.append(x)

    def sustain(self, player_name, sustenance_type):
        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        needed_supply = [x for x in self.supplies if x.__class__.__name__ == sustenance_type]

        if sustenance_type == "Food" and not needed_supply:
            raise Exception("There are no food supplies left!")

        if sustenance_type == "Drink" and not needed_supply:
            raise Exception("There are no drink supplies left!")

        supply = needed_supply[-1]

        for player in self.players:
            if player.name == player_name:
                if player.stamina == 100:
                    return f"{player_name} have enough stamina."

                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy

                self.supplies.remove(supply)
                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        global player_one, player_two
        for p in self.players:
            if p.name == first_player_name:
                player_one = p
            if p.name == second_player_name:
                player_two = p

        if player_one.stamina == 0 and player_two.stamina == 0:
            return f'''Player {first_player_name} does not have enough stamina.
            Player {second_player_name} does not have enough stamina.'''

        if player_one.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."

        if player_two.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        duelists = {
            1: player_one,
            2: player_two
        }
        counter = None

        if player_one.stamina < player_two.stamina:
            counter = 1
        elif player_one.stamina > player_two.stamina:
            counter = 2

        player_one_start_stamina = player_one.stamina
        player_two_start_stamina = player_two.stamina
        player_one_stamina = player_one.stamina / 2
        player_two_stamina = player_two.stamina / 2

        while player_one_start_stamina > 0 and player_two_start_stamina > 0:
            if counter % 2 == 0:
                player_one_start_stamina -= player_two_stamina
            if counter % 2 != 0:
                player_two_start_stamina -= player_one_stamina

            counter += 1

        if player_one_start_stamina <= 0:
            player_one_start_stamina = 0
            return f"Winner: {first_player_name}"

        if player_two_start_stamina <= 0:
            player_two_start_stamina = 0
            return f"Winner: {second_player_name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            player_stamina = player.stamina
            player_stamina += 40