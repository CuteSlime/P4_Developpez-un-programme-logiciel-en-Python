import json


def database_access(database_name, object_class, access_type, *dict_list):
    access_type = str(access_type)

    if access_type == "r":
        objects_list = []
        database = json.load(
            open('./data/' + str(database_name) + '.json', 'r', encoding='utf8'))
        print("\33[93m", database, "\33[0m")
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
        dict_list.append(obj.__dict__)
    print("\33[94m", dict_list, "\33[00m")
    database_access(database_name, object_class, "w", *dict_list)


def remove_from_database(self, objects_list, database_name, object_class):
    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    if self in objects_list:
        objects_list.remove(self)
        dict_list = []
    for obj in objects_list:
        obj = obj.__dict__
        dict_list.append(obj)
    database_access(database_name, object_class, "w", dict_list)


def update_database(self, original, objects_list, database_name, object_class):
    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    if original in objects_list:
        objects_list.remove(original)
        objects_list.append(self)
        dict_list = []
        for obj in objects_list:
            obj = obj.__dict__
            dict_list.append(obj)
    database_access(database_name, object_class, "w", dict_list)
