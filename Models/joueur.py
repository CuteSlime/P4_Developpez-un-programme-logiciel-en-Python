import json
# from .club import Club


def list_joueurs():
    with open('../data/joueurs.json', 'r', encoding='utf8') as joueurs_data:
        joueurs_data = json.load(joueurs_data)
    return joueurs_data


joueurs_data = list_joueurs()


class Joueur:
    def __init__(self, nom, prenom, date_naissance, **kwargs):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = kwargs.get('score', 0)
        self.club = kwargs.get('club')

    def full_name(self):
        return f"{self.prenom} {self.nom}"

    def add_to(self):
        exist = False
        if not isinstance(self, Joueur):
            return print("Ceci n'est pas un Joueur valide")
        for joueur in joueurs_data:
            if self.__dict__ == joueur:
                exist = True
                break
        if exist:
            return print("Ce joueur existe déjà")
        joueurs_data.append(self.__dict__)
        joueur_json = json.dumps(joueurs_data, indent=4)
        with open('../data/joueurs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(joueur_json)

    def remove_from(self):
        if not isinstance(self, Joueur):
            return ValueError("Ceci n'est pas un Joueur valide")
        if self.__dict__ in joueurs_data:
            joueurs_data.remove(self.__dict__)
        joueur_json = json.dumps(joueurs_data, indent=4)
        with open('../data/joueurs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(joueur_json)

    def __str__(self):
        return f"{self.full_name()} Née le :{self.date_naissance} {self.score} {self.club}"


# teste
joueur = Joueur(**joueurs_data[0])


joueur2 = Joueur("Toucuit", "Phillipe", "14 Mars 2001", club="not an actor")
joueur3 = Joueur("Toucuit", "Phillip", "14 Mars 2001", club="not an actor")

joueur2.add_to()


# for i, joueur in enumerate(joueurs_data):
#     if self.__dict__ == joueur:
#         print("trouvé !")
#         break
