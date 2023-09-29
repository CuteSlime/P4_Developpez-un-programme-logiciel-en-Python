
from random import shuffle, random
from datetime import datetime


def sort_by_score(players_to_sort):
    i = 0
    list_joueurs = []
    not_sorted_joueur = players_to_sort[:]
    while i < len(players_to_sort):
        score = -1

        meilleur_joueur = not_sorted_joueur[0]
        for joueur in not_sorted_joueur:
            if joueur.score > score:
                score = joueur.score
                meilleur_joueur = joueur
        list_joueurs.append(meilleur_joueur)
        not_sorted_joueur.remove(meilleur_joueur)
        i += 1
    return list_joueurs


def already_played_together(list_joueurs, list_previous_match):
    i = 1
    sorted_joueurs = []
    not_sorted_joueurs = list_joueurs[:]
    while len(not_sorted_joueurs) > 1:
        not_sorted = True
        for round in list_previous_match:
            last_match_player_1 = round[0][0]
            last_match_player_2 = round[1][0]

            if (not_sorted_joueurs[0].id in (last_match_player_1["id"], last_match_player_2["id"])
                    and
                    not_sorted_joueurs[i].id in (last_match_player_1["id"], last_match_player_2["id"])):

               
        sorted_joueurs.append(not_sorted_joueurs[0])
        sorted_joueurs.append(not_sorted_joueurs[i])
        not_sorted_joueurs.remove(not_sorted_joueurs[i])
        not_sorted_joueurs.remove(not_sorted_joueurs[0])
        i = 1

    return sorted_joueurs


class Tour:
    def __init__(self, nom, **kwargs):
        self.nom = nom
        self.list_matchs = kwargs.get('list_matchs', [])
        self.participants = kwargs.get('participants', [])
        self.date_debut = kwargs.get('date_debut', "")
        self.date_fin = kwargs.get('date_fin', "en cours")

    def add_match(self, participants, list_previous_match):
        joueurs = participants

        is_first_match = True
        for joueur in joueurs:
            if joueur.score > 0:
                is_first_match = False
        if is_first_match:
            shuffle(joueurs)
        else:

            joueurs = already_played_together(sort_by_score(joueurs), list_previous_match)

        groupes = (joueurs[i:i+2] for i in range(0, len(joueurs), 2))
        for groupe in groupes:
            self.list_matchs.append(([groupe[0]], [
                                    groupe[1]]))

        # for match in self.list_matchs:
        #     for last_match in last_matchs:
        #         if last_match == match:
        #             self.list_matchs.remove(last_match)

    def start_tour(self):
        self.date_debut = datetime.now().strftime('%d/%m/%Y %H:%M')

    def end_tour(self):
        self.date_fin = datetime.now().strftime('%d/%m/%Y %H:%M')
        return self.date_fin

    def play_match(self):
        for match in self.list_matchs:
            winner = random()
            if winner > 0.5:
                print("\33[94m"
                      f"{match[0][0].full_name()} gagne !"
                      "\33[00m"
                      )
                match[0][0].score += 1

            elif winner < 0.5:
                print("\33[94m"
                      f"{match[1][0].full_name()} gagne !"
                      "\33[00m"
                      )
                match[1][0].score += 1
            else:
                print("\33[94m" 'c\'est une égalité !'"\33[00m")
                match[0][0].score += 0.5
                match[1][0].score += 0.5
