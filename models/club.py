
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

    def add_to(self):
        exist = False
        if not isinstance(self, Club):
            return print("Ceci n'est pas un Club valide")
        for club in clubs_database:
            if self.__dict__ == club:
                exist = True
                break
        if exist:
            return print("Ce joueur existe déjà")
        clubs_database.append(self.__dict__)
        club_json = json.dumps(clubs_database, indent=4)
        with open('./data/clubs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(club_json)

    def remove_from(self):
        if not isinstance(self, Club):
            return ValueError("Ceci n'est pas un Club valide")
        if self.__dict__ in clubs_database:
            clubs_database.remove(self.__dict__)
        club_json = json.dumps(clubs_database, indent=4)
        with open('./data/clubs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(club_json)

    def update_from(self, original):
        if not isinstance(self, Club):
            return ValueError("Ceci n'est pas un Club valide")
        if original.__dict__ in clubs_database:
            clubs_database.remove(original.__dict__)
            clubs_database.append(self.__dict__)
            club_json = json.dumps(clubs_database, indent=4)
        with open('./data/clubs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(club_json)
            return clubs_database

    def __str__(self) -> str:
        self.nom

    def __repr__(self):
        self.nom, self.identifiant_national
