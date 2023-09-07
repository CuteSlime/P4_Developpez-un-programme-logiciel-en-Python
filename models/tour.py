from random import shuffle
from datetime import datetime
from .match import Match


class Tour:
    def __init__(self, nom, list_joueurs_tournois):
        self.nom = nom
        self.list_matchs = []
        self.date_debut = ""
        self.date_fin = "en cours"
        self.start_tour()
        self.add_match(list_joueurs_tournois)

    def add_match(self, list_joueurs_tournois):
        joueurs = list_joueurs_tournois
        shuffle(joueurs)
        while len(joueurs) > 1:
            self.list_matchs.append(Match(joueurs[0], joueurs[1]))
            del joueurs[0:2]

    def start_tour(self):
        self.date_debut = datetime.now().strftime('%d/%m/%Y %H:%M')

    def tour_fini(self):
        self.date_fin = datetime.now().strftime('%d/%m/%Y %H:%M')
        return self.date_fin
