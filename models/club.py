
import json


def list_clubs():

    with open('./data/clubs.json', 'r', encoding='utf8') as clubs_database:
        clubs_database = json.load(clubs_database)
    return clubs_database


clubs_database = list_clubs()


class Club:
    def __init__(self, nom, identifiant_national):
        self.nom = nom
        self.identifiant_national = identifiant_national

    def __str__(self) -> str:
        self.nom

    def __repr__(self):
        self.nom, self.identifiant_national
