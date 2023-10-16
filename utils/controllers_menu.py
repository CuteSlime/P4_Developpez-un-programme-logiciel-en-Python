from models.tournaments import Tournament
from datetime import datetime
from utils.database import convert_sub_objects, database_access, update_database
from utils.text_color import (
    text_red,
    text_white
)


# active tournament
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
            self.view.tournament_report(tournament, tournament.list_players)
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
        tournament.end_date = datetime.now().strftime('%d/%m/%Y %H:%M')
        participants = []
        for participant in round.participants:
            participants.append(participant)

        self.view.tournament_report(tournament, participants)

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


# tournament edition
def tournament_name_edit(self, view_name, id, tournament, list_tournaments):
    '''edition du nom du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''
    tournament.name = self.view.update_name_tournament(tournament)
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
    return self.menu_edit(view_name, id, tournament, list_tournaments)


def tournament_place_edit(self, view_name, id, tournament, list_tournaments):
    '''edition du lieu de déroulement du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    tournament.place = self.view.update_place_tournament(tournament)
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
    return self.menu_edit(view_name, id, tournament, list_tournaments)


def tournament_start_date_edit(self, view_name, id, tournament, list_tournaments):
    '''edition de la date de début du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    tournament.start_date = self.view.update_start_date_tournament(tournament)
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
    return self.menu_edit(view_name, id, tournament, list_tournaments)


def tournament_end_date_edit(self, view_name, id, tournament, list_tournaments):
    '''edition de la date de fin du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    tournament.end_date = self.view.update_end_date_tournament(tournament)
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
    return self.menu_edit(view_name, id, tournament, list_tournaments)


def tournament_round_edit(self, view_name, id, tournament, list_tournaments):
    '''edition des tour du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    tournament.nb_round = int(self.view.update_nb_round_tournament(tournament))

    while tournament.nb_round != len(tournament.list_rounds):
        if tournament.nb_round > len(tournament.list_rounds):
            tournament.add_tour("Round" + str(len(tournament.list_rounds) + 1))
        if tournament.nb_round < len(tournament.list_rounds):
            tournament.remove_tour(tournament.list_rounds[len(tournament.list_rounds)])
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)

    return self.menu_edit(view_name, id, tournament, list_tournaments)


def tournament_add_player(self, view_name, manage_view, choice, id, tournament, list_tournaments, list_players):
    '''ajout d'un joueur au tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        manage_view (_str_): nom de la vue de gestion
        choice (_int_): choix effectuer dans la vue
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée
        list_players (_list_): list des joueur en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    player = self.menu_list(
        "list_players", list_players, list_only=True)[0]
    if player != "return":
        tournament.add_player(player)
    else:
        list_tournaments = convert_sub_objects(
            database_access("tournaments", Tournament, "r"))
        tournament = list_tournaments[id]
        return self.menu_edit("menu_modification_tournament", id, tournament, list_tournaments)

    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
    return self.edit_tournament(choice, view_name, id, tournament,
                                list_tournaments, manage_view)


def tournament_remove_player(self, tournament_players, id, tournament, list_tournaments):
    '''retrait d'un joueur du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        tournament_players (_list_): list de joueurs du tournois en cours
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    player = self.menu_list(
        "list_players", tournament_players, list_only=True)
    if player[0] != "return":
        tournament.remove_player(tournament.list_players[player[1]])
    else:
        return self.menu_edit("menu_modification_tournament", id, tournament, list_tournaments)
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)


def tournament_start(self, view_name, manage_view, id, tournament, list_tournaments):
    '''lancement du tournoi

    Args:
        view_name (_str_): nom de la vue à utilisé
        manage_view (_str_): nom de la vue de gestion
        id (_int_): id du tournois
        tournament (_object): le tournoi en cours
        list_tournaments (_list_): liste des tournois en base de donnée

    Returns:
        retour au menu d'édition du tournoi
    '''

    tournament.start()
    update_database(
        tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
    return self.menu_manage(manage_view, id, tournament, list_tournaments, view_name)
