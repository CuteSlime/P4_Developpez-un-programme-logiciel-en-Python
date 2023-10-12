
from random import shuffle, random
from datetime import datetime
from utils.models_round import sort_by_score, already_played_together


class Round:
    def __init__(self, name, **kwargs):
        self.name = name
        self.list_matchs = kwargs.get('list_matchs', [])
        self.participants = kwargs.get('participants', [])
        self.start_date = kwargs.get('start_date', "")
        self.end_date = kwargs.get('end_date', "en cours")

    def add_match(self, participants, list_previous_match):
        players = participants

        is_first_match = True
        for player in players:
            if player.score > 0:
                is_first_match = False
        if is_first_match:
            shuffle(players)
        else:

            players = already_played_together(sort_by_score(players), list_previous_match)

        groupes = (players[i:i+2] for i in range(0, len(players), 2))
        for groupe in groupes:
            self.list_matchs.append(([groupe[0]], [groupe[1]]))

    def start_tour(self):
        self.start_date = datetime.now().strftime('%d/%m/%Y %H:%M')

    def end_tour(self):
        self.end_date = datetime.now().strftime('%d/%m/%Y %H:%M')
        return self.end_date

    def play_match(self):
        for game in self.list_matchs:
            winner = random()
            if winner > 0.5:
                print("\33[94m"
                      f"{game[0][0].full_name()} gagne !"
                      "\33[00m"
                      )
                game[0][0].score += 1

            elif winner < 0.5:
                print("\33[94m"
                      f"{game[1][0].full_name()} gagne !"
                      "\33[00m"
                      )
                game[1][0].score += 1
            else:
                print("\33[94m" 'c\'est une égalité !'"\33[00m")
                game[0][0].score += 0.5
                game[1][0].score += 0.5
