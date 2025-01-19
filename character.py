"class Character"

class Character:
    """
    Représente un PNJ dans le jeu, qui peut interagir avec le joueur, 
    se déplacer entre les salles, et communiquer.

    Attributs:
    ------------
        name : str            > nom du PNJ
        description : str     > description du PNJ
        current_room : Room   > salle actuelle où se trouve le PNJ
        msgs : list           > liste de messages prédéfinis du PNJ
        list_msgs : list      > temporaire des messages restants du PNJ

    Méthodes:
    -----------
        __str__():     > retourne une représentation textuelle du PNJ
        get_msg():     > affiche le prochain message disponible du PNJ
        follow_joueur(player):    > pour que le PNJ suive le joueur dans sa salle actuelle
    """

    def __init__(self, name, description, current_room, msgs):
        "le constructeur"

        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.list_msgs = []

    def __str__(self):
        "représentation textuelle du PNJ"

        character = f"{self.name} : {self.description}"
        return character

    def get_msg(self):
        "affiche les prochains messages disponibles du PNJ"

        if self.msgs:
            if not self.list_msgs:
                for i in self.msgs:
                    self.list_msgs.append(i)
            print(self.list_msgs.pop(0))
        else:
            print(f"{self.name} n'a rien à dire.")

    def follow_joueur(self, player):
        "pour que le PNJ suive le joueur dans sa salle actuelle"

        next_room = player.current_room
        if self.name in self.current_room.characters:
            del self.current_room.characters[self.name]
        self.current_room = next_room
        self.current_room.characters[self.name] = self
