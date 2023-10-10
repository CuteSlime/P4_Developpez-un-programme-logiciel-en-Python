from utils.text_color import text_white, text_green


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
        return (f"{text_green}{self.full_name()}{text_white} "
                f"Née le : {text_green}{self.birthday}{text_white} "
                f"club : {text_green}{self.club}{text_white}")
