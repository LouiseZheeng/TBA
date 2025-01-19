"class Item"

class Item():
    """
    Représente un objet (item) dans le jeu avec un nom et un poids.

    Attributs:
    ----------
    name : str             > nom de l'objet
    weight : float         > poids de l'objet (kg)

    Méthodes:
    ---------
    __str__():             > représentation textuelle de l'objet
    """

    def __init__(self, name, weight):
        "le constructeur"

        self.name = name
        self.weight = weight

    def __str__(self):
        "représentation textuelle de l'item"

        item = f"{self.name} ({self.weight} kg)"
        return item