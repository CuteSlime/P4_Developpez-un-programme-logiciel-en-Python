from datetime import datetime


def validate_national_id(national_id):
    if national_id != 7 or (national_id[0:1].isalpha() is False) or (national_id[2:].isnumeric() is False):
        return False
    return True


def date_input(start_or_end):
    while True:
        try:
            date = datetime.strptime(
                input(f"Date de {start_or_end} au format JJ/MM/AAAA :"), "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Format invalide, exemple de format valide : 31/08/2023")
    return date
