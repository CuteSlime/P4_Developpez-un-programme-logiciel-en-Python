
from random import random
from Models.Models import Tournoi, Tour, Match, Club, Joueur


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
