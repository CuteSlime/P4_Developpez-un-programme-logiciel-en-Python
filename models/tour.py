
from random import shuffle, random
from datetime import datetime


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
            i = 0
            list_joueurs = []
            not_sorted_joueur = joueurs[:]
            while i < len(joueurs):
                score = -1

                meilleur_joueur = not_sorted_joueur[0]
                for joueur in not_sorted_joueur:
                    if joueur.score > score:
                        score = joueur.score
                        meilleur_joueur = joueur
                list_joueurs.append(meilleur_joueur)
                not_sorted_joueur.remove(meilleur_joueur)
                i += 1
            i = 0
            while i < len(list_joueurs):
                try:
                    list_joueurs[i+1]
                except IndexError:
                    i += 1
                    break

                if list_joueurs[i].score == list_joueurs[i + 1].score:
                    for round in list_previous_match:

                        for match in round:
                            if list_joueurs[i].__dict__ in match:
                                print(
                                    list_joueurs[i].full_name(), " [------joueur------] ", list_joueurs[i + 1].full_name())
                                if list_joueurs[i + 1].__dict__ in match:
                                    print(
                                        list_joueurs[i].full_name(), " [--VS--] ", list_joueurs[i + 1].full_name())
                                    list_joueurs.insert(
                                        i + 1, list_joueurs.pop(i))
                    i += 1
                else:
                    i += 1
            joueurs = list_joueurs

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
