
import json


def list_clubs():

    with open('./data/clubs.json', 'r', encoding='utf8') as clubs_data:
        clubs_data = json.load(clubs_data)
    return clubs_data


clubs_data = list_clubs()


class Club:
    def __init__(self, nom, identifiant_national):
        self.nom = nom
        self.identifiant_national = identifiant_national

    def add_to(self):
        exist = False
        if not isinstance(self, Club):
            return print("Ceci n'est pas un Club valide")
        for club in clubs_data:
            if self.__dict__ == club:
                exist = True
                break
        if exist:
            return print("Ce joueur existe déjà")
        clubs_data.append(self.__dict__)
        club_json = json.dumps(clubs_data, indent=4)
        with open('./data/clubs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(club_json)

    def remove_from(self):
        if not isinstance(self, Club):
            return ValueError("Ceci n'est pas un Club valide")
        if self.__dict__ in clubs_data:
            clubs_data.remove(self.__dict__)
        club_json = json.dumps(clubs_data, indent=4)
        with open('./data/clubs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(club_json)

    def update_from(self, original):
        if not isinstance(self, Club):
            return ValueError("Ceci n'est pas un Club valide")
        if original.__dict__ in clubs_data:
            clubs_data.remove(original.__dict__)
            clubs_data.append(self.__dict__)
            club_json = json.dumps(clubs_data, indent=4)
        with open('./data/clubs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(club_json)
            return clubs_data

    def __str__(self) -> str:
        self.nom

    def __repr__(self):
        self.nom, self.identifiant_national
