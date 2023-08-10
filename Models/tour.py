from datetime import datetime


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
