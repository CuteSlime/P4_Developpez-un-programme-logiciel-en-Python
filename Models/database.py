import json


def database_access(database_name, cls, access_type, *arg):
    access_type = str(access_type)

    if access_type == "r":
        objects_list = []
        with open('./data/' + str(database_name) + '.json', 'r', encoding='utf8') as Json_data:
            database = json.loads(Json_data.read())
            # print("\33[93m", database, "\33[0m")
            for obj in database:
                objects_list.append(cls(**obj))
    elif access_type == "w":
        print("\33[93m", arg[1], "\33[0m")
        with open('./data/' + str(database_name) + '.json', 'w', encoding='utf8') as Json_data:
            json.dumps(arg, indent=4)
        database_access(database_name, cls, "r")
        arg = objects_list
        print(arg)
        return arg
    return objects_list


def add_to_database(self, database_name, cls):
    objects_database = database_access(database_name, cls, "r")
    exist = False
    if not isinstance(self, cls):
        return print("Ceci n'est pas un ", str(database_name), " valide")
    for obj in objects_database:
        if self.__dict__ == obj:
            exist = True
            break
    if exist:
        return print("Ce ", str(database_name), " existe déjà")
    objects_database.append(self.__dict__)
    database_access(database_name, cls, "w", objects_database)


def remove_from_database(self, database_name, cls):
    objects_database = database_access(database_name, cls, "r")
    if not isinstance(self, cls):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    if self.__dict__ in objects_database:
        objects_database.remove(self.__dict__)
        database_access(database_name, cls, "w", objects_database)


def update_database(self, original, database_name, cls):
    objects_database = database_access(database_name, cls, "r")
    if not isinstance(self, cls):
        return ValueError("Ceci n'est pas un ", str(database_name), " valide")
    if original.__dict__ in objects_database:
        objects_database.remove(original.__dict__)
        objects_database.append(self.__dict__)
        database_access(database_name, cls, "w", objects_database)
