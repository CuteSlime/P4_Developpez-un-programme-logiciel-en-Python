import json


def database_access(database_name, object_class, access_type, *dict_list):
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
    '''si l'objet et bien de la bonne classe et n'est pas encore dans la list d'objet'''

    exist = False
    if not isinstance(self, object_class):
        return print("Ceci n'est pas un ", str(database_name), " valide")
    if not objects_list:
        for obj in objects_list:
            if self.__dict__ == obj.__dict__:
                exist = True
                break
        if exist:
            return print("Ce ", str(database_name), " existe déjà")

    '''ajoute l'objet à la list puis convertie cette list d'objet en list de dictionnaire'''
    objects_list.append(self)
    dict_list = []
    for obj in objects_list:
        print("\33[93m", obj, "\33[00m")
        dict_list.append(obj.__dict__)
    database_access(database_name, object_class, "w", *dict_list)


def remove_from_database(self, objects_list, database_name, object_class):
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


def update_database(self, original, objects_list, database_name, object_class):
    '''
    replace orignal in a list of object by a new object,
    translate the new list into dictionnary and send it to database
    '''
    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    for obj in objects_list:
        if original.__dict__ == obj.__dict__:
            objects_list[objects_list.index(obj)] = self

        if obj.list_joueurs:
            list_dict = []
            for sub_object in obj.list_joueurs:
                if isinstance(sub_object, dict) is False:
                    list_dict.append(sub_object.__dict__)
                else:
                    list_dict.append(sub_object)
            obj.list_joueurs = list_dict
        if obj.list_tours:
            list_dict = []
            for sub_object in obj.list_tours:
                if isinstance(sub_object, dict) is False:
                    list_dict.append(sub_object.__dict__)
                else:
                    list_dict.append(sub_object)
            obj.list_tours = list_dict
    dict_list = []
    for obj in objects_list:
        obj = obj.__dict__
        dict_list.append(obj)
    database_access(database_name, object_class, "w", *dict_list)
