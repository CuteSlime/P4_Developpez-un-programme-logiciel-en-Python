import json
from random import random
from Models.Models import Tournoi, Tour, Match, Club, Joueur


list_club = []


with open('./data/clubs.json', 'r', encoding='utf8') as clubs_data:
    clubs_data = json.load(clubs_data)


with open('./data/joueurs.json', 'r', encoding='utf8') as joueurs_data:
    joueurs_data = json.load(joueurs_data)

"""start_match reçois un match, et retourne le gagnant toute en distribuant les point"""


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
