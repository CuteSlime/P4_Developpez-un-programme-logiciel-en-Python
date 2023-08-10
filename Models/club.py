
import json


list_club = []


with open('./data/clubs.json', 'r', encoding='utf8') as clubs_data:
    clubs_data = json.load(clubs_data)


class Club:
    def __init__(self, nom, identifiant_national):
        self.nom = nom
        self.identifiant_national = identifiant_national

    def __str__(self) -> str:
        self.nom

    def __repr__(self) -> str:
        self.nom, self.identifiant_national
