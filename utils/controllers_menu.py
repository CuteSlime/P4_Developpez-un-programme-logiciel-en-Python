from models.tournaments import Tournament
from models.club import Club
from models.player import Player
from datetime import datetime
from utils.database import convert_sub_objects, database_access, add_to_database, remove_from_database, update_database
from utils.text_color import (
    text_red,
    text_blue,
    text_white
)


def tournament_statue(self, list_tournaments):
    '''vérifie la selection de l'utilisateur et renvoie un tournois avec sont id

    Args:
        list_tournaments (_list_): liste des tournois

    Returns:
        _list_: list de deux élement, une id et un objet tournoi
    '''

    tournament = self.menu_list(
        "list_tournaments", list_tournaments, list_only=True)[1]
    id = tournament
    tournament = list_tournaments[id]

    while tournament.started is False:
        while list_tournaments[id].started is False:
            print(text_red, "Ce tournoi n'as pas encore commencé.", text_white)
            tournament = self.menu_list(
                "list_tournaments", list_tournaments, list_only=True)[1]
            id = tournament
            tournament = list_tournaments[id]

    while tournament.ended is True:
        while list_tournaments[id].ended is True:
            print(text_red, "Ce tournoi est terminé", text_white)
            tournament = self.menu_list(
                "list_tournaments", list_tournaments, list_only=True)[1]
            id = tournament
            tournament = list_tournaments[id]

    return [id, tournament]


def start_round(self, id, round, tournament, list_tournaments):
    '''exécuter le tour actuel et mettre à jour le tournoi

    Args:
        id (_int_): id correspondant au tournoi d'origine
        round (_object_): le tour actuel
        tournament (_object_): le tournoi actuel
        list_tournaments (_list_): la list des tournois en base de donnée

    Returns:
        retourne à la liste des tournois actif
    '''

    round.play_match()
    if tournament.actual_turn_number == len(tournament.list_rounds):
        tournament.ended = True
        best_score = 0
        winner = round.participants[0]
        for participant in round.participants:
            if participant.score > best_score:
                best_score = participant.score
                winner = participant
        tournament.end_date = datetime.now().strftime('%d/%m/%Y %H:%M')
        print(text_blue, f"Tournament {tournament.name} terminé !{text_white}")
        print(
            text_blue, f"Félicitation à {winner.full_name()} {text_white}")

    elif tournament.actual_turn_number < len(tournament.list_rounds):
        tournament.actual_turn_number += 1

    for game in round.list_matchs:
        for player in game:
            player[0] = player[0].__dict__
    list_participants = []

    for participant in round.participants:
        participant = participant.__dict__
        list_participants.append(participant)

    round.participants = list_participants

    update_database(tournament, list_tournaments[id],
                    list_tournaments, "tournaments", Tournament)
    list_tournaments = convert_sub_objects(
        database_access("tournaments", Tournament, "r"))
    return self.active_tournament("actual_tournaments", list_tournaments)
