import json
# from types import SimpleNamespace
# from .club import Club


def database_access(database_name, cls, access_type, *arg):
    access_type = str(access_type)

    if access_type == "r":
        objects_list = []
        with open('./data/' + str(database_name) + '.json', 'r', encoding='utf8') as Json_data:
            database = json.load(Json_data.read())
            for obj in database:
                objects_list.append(cls(**obj))
    elif access_type == "w":
        objects_list = arg
        new_data = json.dumps(objects_list, indent=4)
        with open('./data/' + str(database_name) + '.json', 'w', encoding='utf8') as Json_data:
            Json_data.write(new_data)
    return objects_list


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
        for joueur in joueurs_database:
            if self.__dict__ == joueur:
                exist = True
                break
        if exist:
            return print("Ce joueur existe déjà")
        joueurs_database.append(self.__dict__)
        joueur_json = json.dumps(joueurs_database, indent=4)
        with open('./data/joueurs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(joueur_json)
        return joueurs_database

    def remove_from(self):
        if not isinstance(self, Joueur):
            return ValueError("Ceci n'est pas un Joueur valide")
        if self.__dict__ in joueurs_database:
            joueurs_database.remove(self.__dict__)
        joueur_json = json.dumps(joueurs_database, indent=4)
        with open('./data/joueurs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(joueur_json)
        return joueurs_database

    def update_from(self, original):
        if not isinstance(self, Joueur):
            return ValueError("Ceci n'est pas un Joueur valide")
        if original.__dict__ in joueurs_database:
            joueurs_database.remove(original.__dict__)
            joueurs_database.append(self.__dict__)
            joueur_json = json.dumps(joueurs_database, indent=4)
            with open('./data/joueurs.json', 'w', encoding='utf8') as jsonfile:
                jsonfile.write(joueur_json)
            return joueurs_database

    def __str__(self):
        return f"{self.full_name()} Née le :{self.date_naissance} {self.score} {self.club}"


# # teste
# joueur = Joueur(**joueurs_database[0])


# joueur2 = Joueur("Toucuit", "Phillipe", "14 Mars 2001", club="not an actor")
# joueur3 = Joueur("Toucuit", "Phillip", "14 Mars 2001", club="not an actor")

# joueur2.add_to()


# for i, joueur in enumerate(joueurs_database):
#     if self.__dict__ == joueur:
#         print("trouvé !")
#         break
