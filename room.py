"class Room"

class Room:
    """
    Représente une pièce dans le jeu.

    Attributs:
    ----------
    name : str          > nom de la pièce
    description : str   > description de la pièce
    exits : dict        > sorties de la pièce
    inventory : dict    > inventaire de la pièce
    characters : dict   > les PNJ se trouvant dans la pièce

    Méthodes:
    ---------
    get_exit(direction):        > retourne la pièce correspondant à une direction donnée
    get_exit_string():          > décris les sorties possibles de la pièce
    get_long_description():     > retourne une description complète de la pièce
    add_item(item):             > ajoute un objet à l'inventaire de la pièce
    get_inventory():            > liste présents dans la pièce
    """


    def __init__(self, name, description):
        "le constructeur"

        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}

    def get_exit(self, direction):
        "retourne la pièce correspondant à une direction donnée"

        if direction in self.exits.keys():
            return self.exits[direction]
        return None

    def get_exit_string(self):
        "décris les sorties possibles de la pièce"

        exit_string = "Sortie(s) possible(s): "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        "retourne la longue description de la piècé"

        return f"\n{self.description}"


    def add_item(self, item):
        "ajouter des items dans une piècé"

        self.inventory[item.name]=item

    def get_inventoryy(self):
        "afficher les items présents dans la pièce"

        if not self.inventory:
            print("\nItem(s) présent(s) : il n'y a pas d'items dans cette salle.")
            return "\t"
        inventory = "\nLa pièce contient :\n"
        for item in self.inventory.values():
            inventory += f"    - {str(item)}\n"
        return inventory
    

