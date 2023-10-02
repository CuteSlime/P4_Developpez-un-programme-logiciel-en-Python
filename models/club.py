

class Club:
    def __init__(self, name, national_id):
        self.name = name
        self.national_id = national_id

    def __str__(self):
        return f"{self.name} ID National : {self.national_id}."

    def __repr__(self):
        self.name, self.national_id
