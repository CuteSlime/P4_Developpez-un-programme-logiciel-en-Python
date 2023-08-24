import json
# from .tour import Tour
# from .joueur import Joueur
# from .tour import Tour


def list_tournois():
    tournois_database = []
    with open('./data/tournois.json', 'r', encoding='utf8') as tournois_database:
        tournois_database = json.load(tournois_database)
    return tournois_database


tournois_database = list_tournois()


class Tournoi():
    def __init__(self, lieu, date_debut, date_fin, nb_tour=4):
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tour = nb_tour
        self.numero_tour_actuel = 1
        self.list_tours = []
        self.list_joueurs = []
        self.remarque = ""

    def add_joueur(self, joueur):
        self.list_joueurs.append(joueur)
        print(self.list_joueurs)

    def add_tour(self, tour_name):
        self.list_tours.append(tour_name)
