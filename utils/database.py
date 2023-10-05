import json
from models.round import Round
from models.player import Player
from utils.text_color import (
    text_orange,
    text_red,
    text_white
)


def convert_sub_objects(list_tournaments: list):
    '''reconversion des liste de joueurs et tours récuperé depuis le JSON, en objets

    Args:
        objects_list (_list_) : la liste des tournois ou ce trouve les sous list de tours et joueurs

    Return:
        _list_ : la liste avec les sous objets convertie
    '''

    for obj in list_tournaments:
        if hasattr(obj, "list_players"):
            list_player = []
            for player in obj.list_players:
                player = Player(**player)
                list_player.append(player)

            obj.list_players = list_player

        if hasattr(obj, "list_rounds"):
            list_round = []
            for round in obj.list_rounds:
                if isinstance(round, dict):
                    round = Round(**round)
                list_round.append(round)
            obj.list_rounds = list_round
    return list_tournaments


def objects_list_to_dict(objects_list: list):
    ''' convertie une liste d'objets en liste de dictionnaires.
        utilisé quand l'ont veut envoyer nos objet dans la base de donnée JSON

    Args:
        objects_list (_list_) : la liste d'objet

    Returns:
        _list_ : la liste transformé en dictionnaire
    '''

    list_dict = []
    for obj in objects_list:
        if isinstance(obj, dict) is False:
            list_dict.append(obj.__dict__)
        else:
            list_dict.append(obj)
    return list_dict


def database_access(database_name: str, object_class, access_type: str, *dict_list: list):
    '''fonction en charge de la lecture et écriture des fichier JSON pour la base de donnée

    Args:
        database_name (_str_): Nom du fichier Json servant de base de donnée
        object_class (_Class_): la classe de l'objet
        access_type (_type_): "r" pour lire les donnée, "w" pour les écrire pour lire ensuite

    Returns:
        _list_: la liste d'objet correspondante au fichier JSON appellé
    '''
    access_type = str(access_type)

    if access_type == "r":
        objects_list = []
        database = json.load(
            open('./data/' + str(database_name) + '.json', 'r', encoding='utf8'))
        for database_object in database:
            objects_list.append(object_class(**database_object))
        return objects_list
    elif access_type == "w":
        json.dump(dict_list, open(
            './data/' + str(database_name) + '.json', 'w', encoding='utf8'), indent=4)
        database_access(database_name, object_class, "r")


def add_to_database(self, objects_list, database_name, object_class):
    '''fonction en charge de préparer la list d'objet pour l'ajout en base de donnée

    Args:
        objects_list (_list_) : la liste d'objets à ajouter
        database_name (_str_): Nom du fichier Json servant de base de donnée
        object_class (_Class_): la classe de l'objet
    '''

    exist = False
    if not isinstance(self, object_class):
        return print(text_red, "Ceci n'est pas un ", str(database_name), " valide", text_white)
    if not objects_list:
        for obj in objects_list:
            if self.__dict__ == obj.__dict__:
                exist = True
                break
        if exist:
            return print("Ce ", str(database_name), " existe déjà")

    # ajoute l'objet à la list puis convertie cette list d'objet en list de dictionnaire
    objects_list.append(self)
    dict_list = []
    for obj in objects_list:
        if hasattr(obj, "list_players"):
            obj.list_players = objects_list_to_dict(obj.list_players)
        if hasattr(obj, "list_rounds"):
            obj.list_rounds = objects_list_to_dict(obj.list_rounds)
        print(text_orange, obj, text_white)
        dict_list.append(obj.__dict__)
    database_access(database_name, object_class, "w", *dict_list)


def remove_from_database(self, objects_list, database_name, object_class):
    '''fonction en charge de préparer la list d'objet pour la suppression de la base de donnée

    Args:
        objects_list (_list_) : la liste d'objets à retirer
        database_name (_str_): Nom du fichier Json servant de base de donnée
        object_class (_Class_): la classe de l'objet
    '''

    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")

    for obj in objects_list:
        if self.__dict__ == obj.__dict__:
            objects_list.remove(obj)
    dict_list = []
    for obj in objects_list:

        obj = obj.__dict__
        dict_list.append(obj)
    database_access(database_name, object_class, "w", *dict_list)


def update_database(self, original: object, objects_list: list, database_name: str, object_class):
    '''
    fonction d'édition de la base de donnée,
    compare et modifie les objet avant de envoyer à la gestion de base de donnée.

    Args:
        original (_object_) : l'objet d'origine avant modification
        objects_list (_list_) : la liste d'objets à modifier
        database_name (_str_): Nom du fichier Json servant de base de donnée
        object_class (_Class_): la classe de l'objet
    '''

    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    for obj in objects_list:
        if original.__dict__ == obj.__dict__:
            objects_list[objects_list.index(obj)] = self

        if hasattr(obj, "list_players"):
            obj.list_players = objects_list_to_dict(obj.list_players)
        if hasattr(obj, "list_rounds"):
            obj.list_rounds = objects_list_to_dict(obj.list_rounds)
    dict_list = []
    for obj in objects_list:
        obj = obj.__dict__
        dict_list.append(obj)
    database_access(database_name, object_class, "w", *dict_list)
