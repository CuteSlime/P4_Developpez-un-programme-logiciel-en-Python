def number_of_turn(number_of_player):
    nb_turn = 0
    while float(number_of_player) > 1:
        number_of_player /= 2
        nb_turn += 1

    return nb_turn


class Tournoi():
    def __init__(self, nom, lieu, date_debut, date_fin, **kwargs):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tour = kwargs.get('nb_tour', 4)
        self.started = kwargs.get('started', False)

        self.numero_tour_actuel = kwargs.get('numero_tour_actuel', 1)
        self.list_tours = kwargs.get('list_tours', [])
        self.list_joueurs = kwargs.get('list_joueurs', [])
        self.remarque = kwargs.get('remarque', "")

    def fill_tour(self):
        if self.started:
            i = 0
            while i < self.nb_tour:
                self.list_tours.append({
                    "nom": "Round" + str(i+1),
                    "list_matchs": [],
                    "participants": [],
                    "date_debut":  "", "date_fin": "en cours"
                })
                i += 1

    def start(self):
        if len(self.list_joueurs) % 2 == 0:
            self.nb_tour = number_of_turn(len(self.list_joueurs))
            self.started = True
            self.fill_tour()
        else:
            return "erreur"

    def add_joueur(self, joueur):
        self.list_joueurs.append(joueur)

    def remove_joueur(self, joueur):
        self.list_joueurs.remove(joueur)

    def add_tour(self, tour_name):
        self.nb_tour += 1
        self.list_tours.append(tour_name)

    def remove_tour(self, tour_name):
        self.nb_tour -= 1
        self.list_tours.remove(tour_name)

    def __str__(self):
        return (f"\33[92m \n"
                f"Nom : {self.nom}  \n"
                f"à : {self.lieu} \n"
                f"Début du tournoi : {self.date_debut}   Fin : {self.date_fin} \n"
                f"Description : {self.remarque}\33[0m"
                )
