from datetime import datetime
from models.round import Round
from models.player import Player


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


def convert_sub_objects(list_tournaments):
    '''conversion des list de joueurs et tours récuperé depuis le JSON, en objets'''

    for obj in list_tournaments:
        if obj.list_players:
            list_player = []
            for player in obj.list_players:
                player = Player(**player)
                list_player.append(player)

            obj.list_players = list_player

        if obj.list_rounds:
            list_round = []
            for round in obj.list_rounds:
                if isinstance(round, dict):
                    round = Round(**round)
                list_round.append(round)
            obj.list_rounds = list_round
    return list_tournaments
