# Define the Player class.
class Player():
    """
    La classe Player permet de gérer le nom du joueur, la pièce dans laquelle il se situe et ses déplacements 
    entre les différentes pièces.

    Attributs : 
    name : str              > nom du joueur
    current_room : Room     > pièce où se trouve le joueur dont la valeur initiale est prédéfinie : None

    Méthodes
    move(self, direction): 
    > Le joueur se déplace entre les pièces en indiquant une direction : N, E, O, S grâce au dictionnaire des sorties
    de la pièce actuelle. Si la prochaine pièce est None alors un message d'erreur est affiché.

    Exemples
    --------
    >>> player = Player("LT")
    >>> player.current_room = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> player.move("S")
    Vous êtes dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.
    >>> player.move("O")
    Aucune porte dans cette direction !
    False
    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
    
    def get_history(self,history):
        get_history = "Vous avez déjà visité les pièces suivantes:\n"
        for room in self.history:
            a = "\t -" + room.description + "\n"
            get_history += a
        return get_history


    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # nommer le dernier lieu visité 
        last_current_room = self.current_room
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())

        # ajouter le dernier lieu visité dans history
        self.history.append(last_current_room)
            # retourne les historiques des rooms visités 
        print("\n" + self.get_history(self.history))
        return True


    