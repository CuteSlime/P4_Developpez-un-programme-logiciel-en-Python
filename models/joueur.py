

class Joueur:

    def __init__(self, nom, prenom, date_naissance, **kwargs):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = kwargs.get('score', 0)
        self.club = kwargs.get('club')

    def full_name(self):
        return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"{self.full_name()} Née le : {self.date_naissance} {self.score} {self.club}"


# # teste
# joueur = Joueur(**joueurs_database[0])

# joueur2 = Joueur("Toucuit", "Phillipe", "14 Mars 2001", club="not an actor")
# joueur3 = Joueur("Toucuit", "Phillip", "14 Mars 2001", club="not an actor")

# joueur2.add_to()


# for i, joueur in enumerate(joueurs_database):
#     if self.__dict__ == joueur:
#         print("trouvé !")
#         break
