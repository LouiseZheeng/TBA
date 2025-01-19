"Classe Player"

class Player():
    """
    La classe Player représente un joueur dans le jeu, avec des 
    attributs liés à la santé, la faim, la soif, l'inventaire et les
    déplacements effectués.

    Attributs :
    -----------
    name : str             > nom du joueur
    sante : int            > santé actuelle du joueur (de 0 à 100)
    max_sante : int        > santé maximale du joueur (égal à 100)
    faim : int             > niveau de faim du joueur (de 0 à 100)
    max_faim : int         > niveau maximal de faim (égal à 100)
    soif : int             > niveau de soif du joueur (de 0 à 100)
    max_soif : int         > niveau maximal de soif (égal à 100)
    inventory : dict       > inventaire du joueur
    weight : int           > poids total de l'inventaire du joueur
    max_weight : int       > poids maximal que le joueur peut porter
    current_room : Room    > pièce actuelle où se trouve le joueur
    visited_rooms : list   > liste des pièces visitées par le joueur
    previous_room : Room   > pièce précédente où le joueur se trouvait

    Méthodes :
    ---------
    __init__(self, name) :        > le constructeur de la classe Player
    move(direction) :             > déplace le joueur dans la direction donnée
    mort_ou_fin_jeu() :           > vérifie si les conditions de mort ou de 
                                    fin de jeu du joueur sont remplies 
    get_inventory() :             > retourne l'inventaire du joueur
    boire_room() :                > restaure la soif du joueur
    perte_soif_faim() :           > réduit les niveaux de faim et de soif du joueur
    """


    # Définir le constructeur
    def __init__(self, name):
        "Initialiser le joueur"
        self.name = name
        self.sante = 100
        self.max_sante = 100
        self.faim = 50
        self.max_faim = 100
        self.soif = 50
        self.max_soif = 100
        self.inventory = {}
        self.weight = 0
        self.max_weight = 8
        self.current_room = None
        self.visited_rooms = []
        self.previous_room = None

    def move(self, direction):
        "Fonction pour faire déplacer le joueur"

        next_room = self.current_room.exits[direction]
        if next_room is None:
            print("\nCette sortie n'existe pas.\n")
            return False

        if self.current_room not in self.visited_rooms:
            self.visited_rooms.append(self.current_room)

        self.previous_room = self.visited_rooms[-1]
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True


    def mort_ou_fin_jeu(self):
        "Fonction pour définir les conditions de la mort du joueur"

        if all(direction is None for direction in self.current_room.exits.values()):
            liste1 = ["Sentier dégagé", "montagne", "campement", "salle du Rex", "laboratoire", "plaine du nouveau monde"]
            if self.current_room.name not in liste1:
                print("Votre personnage est mort. Merci d'avoir joué !\n")
                return True

        if self.faim == 0 :
            print("Vous êtes mort affamé.\n")
            return True
        if self.soif == 0:
            print("Vous êtes mort assoifé.\n")
            return True
        if self.sante == 0:
            print("Vous avez succombez à vos blessures.\n")
            return True
        if "bois" in self.inventory :
            print("Vous avez pris le bois du castor." \
            " Il vous poursuit et vous blesse gravement au point où vous finissez" \
            " par succomber à vos blessures. Votre personnage est mort." \
            " \nMerci d'avoir joué !\n")
            return True

        liste = ["plaine du nouveau monde", "laboratoire"]
        if self.current_room.name in liste:
            print("C'est la fin du jeu. Merci d'avoir joué!\n@Credit : Ark\n")
            return True
        return False


    def get_inventory(self):
        "Fonction affichant l'inventaire du joueur"

        if not self.inventory:
            print("Votre inventaire est vide.")
            return False

        inventory = "Vous disposez des items suivants :\n"
        for name, item in self.inventory.items():
            inventory += f"    - {str(item)}\n"
        return inventory


    def boire_room(self):
        "Fonction qui remet la soif du joueur à 100 s'il se trouve dans le canyon ou l'etang"

        if self.current_room.name == "canyon":
            self.soif = self.max_soif
            print(f"Vous buvez l'eau fraîche. Votre soif est de : {self.soif}/{self.max_soif}")
            return True

        if self.current_room.name == "etang":
            print("Vous buvez l'eau pure de l'étang.")
            print(f"Votre soif est de : {self.soif}/{self.max_soif}")
            self.soif = self.max_soif
            return True

        return False


    def perte_soif_faim(self):
        "Fonction qui permet de perdre de la soif et de l'eau"

        if self.current_room not in self.visited_rooms:
            self.visited_rooms.append(self.current_room)

        if len(self.visited_rooms)%2 == 0:
            self.faim -= 10
            print("\nVous commencez à avoir faim.")
            print(f"Votre barre de faim est de : {self.faim}/{self.max_faim}\n")

            if self.current_room.name not in ["etang", "canyon"]:
                self.soif -= 10
                print("\nVous commencez à avoir soif.")
                print(f"Votre barre de soif est de : {self.soif}/{self.max_soif}\n")
        return True

