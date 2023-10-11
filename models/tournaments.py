from utils.text_color import text_red, text_white, text_green


class Tournament():
    def __init__(self, name, place, start_date, end_date, **kwargs):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.nb_round = kwargs.get('nb_round', 4)
        self.started = kwargs.get('started', False)
        self.ended = kwargs.get('ended', False)
        self.actual_turn_number = kwargs.get('actual_turn_number', 1)
        self.list_rounds = kwargs.get('list_rounds', [])
        self.list_players = kwargs.get('list_players', [])
        self.remark = kwargs.get('remark', "")

    def fill_tour(self):
        if self.started:
            i = 0
            while i < self.nb_round:
                self.list_rounds.append({
                    "name": "Round" + str(i+1),
                    "list_matchs": [],
                    "participants": [],
                    "start_date":  "", "end_date": "en cours"
                })
                i += 1

    def start(self):
        if len(self.list_players) % 2 == 0:

            for id, player in enumerate(self.list_players):
                player.id = id
            if self.nb_round > len(self.list_players) - 1:
                print(f'{text_red}/!\\ pour {len(self.list_players)} joueurs'
                      f' le nombre de tour maximum est de {len(self.list_players) -1}'
                      f'\nnombre de tour fixer à {len(self.list_players) -1}{text_white}')
                self.nb_round = len(self.list_players) - 1
            self.started = True
            self.fill_tour()
        else:
            return "erreur"

    def add_player(self, player):
        self.list_players.append(player)

    def remove_player(self, player):
        self.list_players.remove(player)

    def add_tour(self, tour_name):
        self.nb_round += 1
        self.list_rounds.append(tour_name)

    def remove_tour(self, tour_name):
        self.nb_round -= 1
        self.list_rounds.remove(tour_name)

    def __str__(self):
        return (f"\n"
                f"Nom : {text_green}{self.name}{text_white}    Lieu : {text_green}{self.place}{text_white}     "
                f"Début du tournoi : {text_green}{self.start_date}{text_white}   "
                f"Fin : {text_green}{self.end_date}{text_white} \n"
                f"Description : {text_green}{self.remark}{text_white}\n"
                )
