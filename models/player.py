

class Player:

    def __init__(self, name, first_name, birthday, **kwargs):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.score = kwargs.get('score', 0)
        self.club = kwargs.get('club')
        self.id = kwargs.get('id', 0)

    def full_name(self):
        return f"{self.first_name} {self.name}"

    def __str__(self):
        return f"{self.full_name()} Née le : {self.birthday} {self.score} {self.club}"
