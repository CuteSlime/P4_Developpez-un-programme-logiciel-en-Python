
from random import shuffle, random
from datetime import datetime


def sort_by_score(players_to_sort: list):
    '''Trie la liste des joueurs par score

    Args:
        players_to_sort (_list_): liste des joueurs à trier

    Returns:
        _list_: liste des joueur trier par score
    '''

    i = 0
    list_players = []
    not_sorted_player = players_to_sort[:]
    while i < len(players_to_sort):
        score = -1

        meilleur_player = not_sorted_player[0]
        for player in not_sorted_player:
            if player.score > score:
                score = player.score
                meilleur_player = player
        list_players.append(meilleur_player)
        not_sorted_player.remove(meilleur_player)
        i += 1
    return list_players


def already_played_together(list_players: list, list_previous_match: list):
    '''Trie les joueurs pour s'assurer qu'ils n'ont pas déjà jouer ensemble

    Args:
        list_players (_list_): liste des joueurs a Trier
        list_previous_match (_list_): Liste des match du tournois qui ont déjà été jouer

    Returns:
        _list_: liste trier des joueurs
    '''

    i = 1
    print(list_players)
    sorted_players = []
    not_sorted_players = list_players[:]
    while len(not_sorted_players) > 1:
        print(sorted_players, "\n", not_sorted_players)
        for match in list_previous_match:
            last_match_player_1 = match[0][0]
            last_match_player_2 = match[1][0]

            if (not_sorted_players[0].id in (last_match_player_1["id"], last_match_player_2["id"])
                    and
                    not_sorted_players[i].id not in (last_match_player_1["id"], last_match_player_2["id"])):
                sorted_players.append(not_sorted_players[0])
                sorted_players.append(not_sorted_players[i])
                not_sorted_players.remove(not_sorted_players[i])
                not_sorted_players.remove(not_sorted_players[0])
                i = 1
                break

            else:
                i += 1

    return sorted_players


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
