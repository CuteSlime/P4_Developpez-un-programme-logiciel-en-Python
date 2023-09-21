
from random import shuffle, random
from datetime import datetime


class Tour:
    def __init__(self, nom, **kwargs):
        self.nom = nom
        self.list_matchs = []
        self.participants = kwargs.get('participants', [])
        self.date_debut = ""
        self.date_fin = "en cours"

    def add_match(self, participants):
        joueurs = participants
        shuffle(joueurs)

        groupes = (joueurs[i:i+2] for i in range(0, len(joueurs), 2))
        for groupe in groupes:
            self.list_matchs.append(([groupe[0]], [
                                    groupe[1]]))

    def start_tour(self):
        self.date_debut = datetime.now().strftime('%d/%m/%Y %H:%M')

    def end_tour(self):
        self.date_fin = datetime.now().strftime('%d/%m/%Y %H:%M')
        return self.date_fin

    def play_match(self):
        for match in self.list_matchs:
            winner = random()
            if winner > 0.5:
                print(match[0][0].full_name(), "gagne !")
                match[0][0].score += 1

            elif winner < 0.5:
                print(match[1][0].full_name(), "gagne !")
                match[1][0].score += 1
            else:
                print('c\'est une égalité !')
                match[0][0].score += 0.5
                match[1][0].score += 0.5
