

class Club:
    def __init__(self, nom, identifiant_national):
        self.nom = nom
        self.identifiant_national = identifiant_national

    def __str__(self):
        return f"{self.nom} ID National : {self.identifiant_national}."

    def __repr__(self):
        self.nom, self.identifiant_national
