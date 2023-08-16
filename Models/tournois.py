import json


def list_tournois():
    tournois_data = []
    with open('./data/tournois.json', 'r', encoding='utf8') as tournois_data:
        tournois_data = json.load(tournois_data)
    return tournois_data


tournois_data = list_tournois()


class Tournoi():
    def __init__(self, lieu, date_debut, date_fin, nb_tour=4):
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tour = nb_tour
        self.numero_tour_actuel = 1
        self.list_tours = []
        self.list_joueurs = []
        self.remarque = ""

    def add_to(self):
        exist = False
        if not isinstance(self, Tournoi):
            return print("Ceci n'est pas un Tournoi valide")
        for tournoi in tournois_data:
            if self.__dict__ == tournoi:
                exist = True
                break
        if exist:
            return print("Ce tournoi existe déjà")
        tournois_data.append(self.__dict__)
        tournoi_json = json.dumps(tournois_data, indent=4)
        with open('../data/tournois.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(tournoi_json)

    def remove_from(self):
        if not isinstance(self, Tournoi):
            return ValueError("Ceci n'est pas un Tournoi valide")
        if self.__dict__ in tournois_data:
            tournois_data.remove(self.__dict__)
        tournoi_json = json.dumps(tournois_data, indent=4)
        with open('../data/tournois.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(tournoi_json)

    def add_joueur(self, joueur):
        self.list_joueurs.append(joueur)

    def add_tour(self, tour_name):
        self.list_tours.append(tour_name)
