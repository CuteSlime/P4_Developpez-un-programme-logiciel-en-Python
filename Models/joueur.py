
class Joueur:

    def __init__(self, nom, prenom, date_naissance, **kwargs):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = kwargs.get('score', 0)
        self.club = kwargs.get('club')

    def full_name(self):
        return f"{self.prenom} {self.nom}"

    # def add_to(self):
    #     joueurs_database = database_access("joueurs", Joueur, "r")
    #     exist = False
    #     if not isinstance(self, Joueur):
    #         return print("Ceci n'est pas un Joueur valide")
    #     for joueur in joueurs_database:
    #         if self.__dict__ == joueur:
    #             exist = True
    #             break
    #     if exist:
    #         return print("Ce joueur existe déjà")
    #     joueurs_database.append(self.__dict__)
    #     database_access("joueurs", Joueur, "w", joueurs_database)

    # def remove_from(self):
    #     joueurs_database = database_access("joueurs", Joueur, "r")
    #     if not isinstance(self, Joueur):
    #         return ValueError("Ceci n'est pas un Joueur valide")
    #     if self.__dict__ in joueurs_database:
    #         joueurs_database.remove(self.__dict__)
    #         database_access("joueurs", Joueur, "w", joueurs_database)

    # def update_from(self, original):
    #     joueurs_database = database_access("joueurs", Joueur, "r")
    #     if not isinstance(self, Joueur):
    #         return ValueError("Ceci n'est pas un Joueur valide")
    #     if original.__dict__ in joueurs_database:
    #         joueurs_database.remove(original.__dict__)
    #         joueurs_database.append(self.__dict__)
    #         database_access("joueurs", Joueur, "w", joueurs_database)

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
