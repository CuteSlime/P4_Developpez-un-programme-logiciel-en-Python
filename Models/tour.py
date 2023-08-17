from datetime import datetime
import json

from .match import Match
# from .club import Club


def list_tours():
    with open('../data/tours.json', 'r', encoding='utf8') as tours_data:
        tours_data = json.load(tours_data)
    return tours_data


tours_data = list_tours()


class Tour:
    def __init__(self, nom):
        self.nom = nom
        self.list_matchs = []
        self.date_debut = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.date_fin = "en cours"

    def add_match(self, match):
        self.list_matchs.append(match.match_print())

    def tour_fini(self):
        self.date_fin = datetime.now().strftime('%d/%m/%Y %H:%M')
        return self.date_fin

    def add_to(self):
        exist = False
        if not isinstance(self, Tour):
            return print("Ceci n'est pas un Tour valide")
        for tour in tours_data:
            if self.__dict__ == tour:
                exist = True
                break
        if exist:
            return print("Ce tour existe déjà")
        tours_data.append(self.__dict__)
        tour_json = json.dumps(tours_data, indent=4)
        with open('../data/tours.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(tour_json)

    def remove_from(self):
        if not isinstance(self, Tour):
            return ValueError("Ceci n'est pas un Tour valide")
        if self.__dict__ in tours_data:
            tours_data.remove(self.__dict__)
        tour_json = json.dumps(tours_data, indent=4)
        with open('../data/tours.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(tour_json)

    def update_from(self, original):
        if not isinstance(self, Tour):
            return ValueError("Ceci n'est pas un Club valide")
        if original.__dict__ in tours_data:
            tours_data.remove(original.__dict__)
            tours_data.append(self.__dict__)
            tour_json = json.dumps(tours_data, indent=4)
        with open('../data/tours.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(tour_json)
            return tours_data
