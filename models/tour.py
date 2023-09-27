
from random import shuffle, random
from datetime import datetime


class Tour:
    def __init__(self, nom, **kwargs):
        self.nom = nom
        self.list_matchs = kwargs.get('list_matchs', [])
        self.participants = kwargs.get('participants', [])
        self.date_debut = kwargs.get('date_debut', "")
        self.date_fin = kwargs.get('date_fin', "en cours")

    def add_match(self, participants, last_matchs):
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
            joueurs = list_joueurs

        groupes = (joueurs[i:i+2] for i in range(0, len(joueurs), 2))
        for groupe in groupes:
            self.list_matchs.append(([groupe[0]], [
                                    groupe[1]]))

        # shuffle(joueurs)
        # is_first_match = True
        # for joueur in joueurs:
        #     if joueur.score > 0:
        #         is_first_match = False
        # if is_first_match:

        # if last_matchs == []:

        #     groupes = (joueurs[i:i+2] for i in range(0, len(joueurs), 2))
        #     for groupe in groupes:
        #         self.list_matchs.append(([groupe[0]], [
        #             groupe[1]]))
        # else:
        #     new_players = []

        #     first_list = []
        #     second_list = []
        #     for match in last_matchs:
        #         first_list.append(match[0][0])
        #         second_list.append(match[1][0])
        #     print(first_list, "\n", second_list, "\n")
        #     for joueur in joueurs:
        #         if joueur.__dict__ in (first_list):
        #             new_players.append(joueur)
        #     for joueur in joueurs:
        #         if joueur.__dict__ in (second_list):
        #             new_players.append(joueur)
        #     groupes = (new_players[i:i+2]
        #                for i in range(0, len(new_players), 2))
        #     for groupe in groupes:
        #         self.list_matchs.append(([groupe[0]], [
        #             groupe[1]]))
        # # re_draw = []

        # need_re_draw = True

        # while need_re_draw:
        #     if re_draw != []:
        #         draw_player = re_draw[:]
        #         shuffle(draw_player)
        #         print("111")
        #         groupes = (draw_player[i:i+2]
        #                    for i in range(0, len(draw_player), 2))
        #         print(groupes)
        #         re_draw = []

        #     else:
        #         groupes = (joueurs[i:i+2] for i in range(0, len(joueurs), 2))
        #         print("------", groupes)
        #     for groupe in groupes:
        #         print("_________=", groupe)
        #         if last_matchs == []:
        #             self.list_matchs.append(([groupe[0]], [
        #                 groupe[1]]))
        #         else:
        #             for last_match in last_matchs:
        #                 print("\n",
        #                       last_match, [[groupe[0].__dict__], [groupe[1].__dict__]], "\n")
        #                 if [[groupe[0].__dict__], [groupe[1].__dict__]] != last_match and [[groupe[1].__dict__], [groupe[0].__dict__]] != last_match:
        #                     print("\n append !")
        #                     self.list_matchs.append(([groupe[0]], [
        #                                             groupe[1]]))

        #                 else:
        #                     print("000")
        #                     re_draw.append(groupe[0])
        #                     re_draw.append(groupe[1])
        #                     print(re_draw)

        #     if re_draw == []:
        #         need_re_draw = False

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
