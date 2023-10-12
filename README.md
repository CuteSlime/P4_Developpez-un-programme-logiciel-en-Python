# P4_Developpez-un-programme-logiciel-en-Python
Projet numéro 4 du parcour OpenClassrooms "développeur d'application python"

## installer le projet (Windows)

commencer par cloner le projet avec git clone

### une fois le projet en local, créer votre environement virtuel :

```py
py -m venv .env
```

### activer l'environement virtuel :

```py
./.env/scripts/activate
```

### installer les dépendance :

```py
pip install -r requirements.txt
```

### lancer le logiciel :

```py
py main.py
```

### Pour générer un nouveau rapport Flake8, à la racine du projet utilisé la commande :

```py
flake8 --format=html --htmldir="flake8_rapport"
```