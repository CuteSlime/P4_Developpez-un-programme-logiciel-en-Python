import json
from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def database_access(database_name, object_class, access_type, *objects_list):
    access_type = str(access_type)

    if access_type == "r":
        objects_list2 = json.load(
            open('./data/' + str(database_name) + '.json', 'r', encoding='utf8'))
        # print("\33[93m", database, "\33[0m")
        # for obj2 in database:
        #     objects_list.append(object_class(**obj2))
    elif access_type == "w":
        json.dump(objects_list, open('./data/' + str(database_name) +
                                     '.json', 'w', encoding='utf8'), indent=4, cls=Encoder)
        database_access(database_name, object_class, "r")
    return objects_list2


def add_to_database(self, objects_list, database_name, object_class):
    exist = False
    if not isinstance(self, object_class):
        return print("Ceci n'est pas un ", str(database_name), " valide")
    for obj in objects_list:
        if self.__dict__ == obj:
            exist = True
            break
    if exist:
        return print("Ce ", str(database_name), " existe déjà")
    objects_list.append(self.__dict__)
    print("\33[94m", objects_list, "\33[00m")
    database_access(database_name, object_class, "w", objects_list)


def remove_from_database(self, objects_list, database_name, object_class):
    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    if self.__dict__ in objects_list:
        objects_list.remove(self.__dict__)
        database_access(database_name, object_class, "w", objects_list)


def update_database(self, original, objects_list, database_name, object_class):
    if not isinstance(self, object_class):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    if original.__dict__ in objects_list:
        objects_list.remove(original.__dict__)
        objects_list.append(self.__dict__)
        database_access(database_name, object_class, "w", objects_list)
