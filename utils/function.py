from datetime import datetime


def validate_national_id(national_id):
    ''' vérifie que le numéro d'identification national :
        - posséde 7 character.
        - commence par 2 lettre.
        - suivi de 5 chiffre.
    '''

    if national_id != 7 or (national_id[0:1].isalpha() is False) or (national_id[2:].isnumeric() is False):
        return False
    return True


def date_input(start_or_end):
    '''reçois une date de l'utilisateur et la valide avant de la renvoyer.'''

    while True:
        try:
            date = datetime.strptime(
                input(f"Date de {start_or_end} au format JJ/MM/AAAA :"), "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Format invalide, exemple de format valide : 31/08/2023")
    return date


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
    # print(list_players)
    sorted_players = []
    not_sorted_players = list_players[:]
    while len(not_sorted_players) > 1:
        # print(sorted_players, "\n", not_sorted_players)
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
                if i >= len(not_sorted_players):
                    i = 1
    return sorted_players
