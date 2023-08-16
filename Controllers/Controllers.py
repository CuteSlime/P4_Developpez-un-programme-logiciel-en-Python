
from random import random
from Models.tournois import Tournoi
from Models.tour import Tour
from Models.match import Match
from Models.club import Club
from Models.joueur import Joueur
from Views.Views import menu_principal, menu_tournois, menu_club, menu_joueur

list_tournois = []
list_tours = []
list_matchs = []
list_joueurs = []
list_clubs = []


class Controller:
    '''Main controller'''

    def __init__(self, view):
        self.tournois = list_tournois()
        self.tours = list_tours()
        self.matchs = list_matchs()
        self.clubs = list_clubs()
        self.joueurs = list_joueurs()

    # def lister_joueurs(joueurs_data):
    #     for joueur in joueurs_data:
    #         print(joueur)
    #         list_joueurs.append(Joueur(**joueur))
    #     return list_joueurs

    """start_match reçois un match, et retourne le gagnant toute en distribuant les point"""
    def run():
        choix = 0
        menu_principal()
        if choix in ["1", "2", "3", "4"]:
            if choix == "1":
                return menu_tournois()
            elif choix == "2":
                return menu_joueur()
            elif choix == "3":
                return menu_club()
            elif choix == "4":
                exit()

        else:
            print("Choix incorrect !")

    def start_match(match):
        winner = random()
        if winner > 0.5:
            print(match.joueur1.full_name(), "gagne !")
            match.joueur1.score += 1

        elif winner < 0.5:
            print(match.joueur2.full_name(), "gagne !")
            match.joueur2.score += 1
        else:
            print('c\'est une égalité !')
            match.joueur1.score += 0.5
            match.joueur2.score += 0.5
        print(match.match_print(), "teste")
        return match.match_print()
