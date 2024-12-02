# Define the Room class.

class Room:
    """
    La classe Room permet de donner une description et le nom de la pièce dans laquelle le joueur se situe et 
    également les différentes sorties possibles.

    Attributs : 
    name : str          > nom de la pièce
    description : str   > description de la pièce
    exits : dict        > dictionnaire des sorties disponibles 

    Méthodes : 
    get_exit(self, direction)   > retourne la pièce de la direction indiquée par le joueur si elle existe
    get_exit_string(self)       > retourne une chaîne de caractère décrivant les sorties disponibles de la pièce où le joueur est actuellement
    get_long_description(self)  > donne une description de la pièce et les sorties disponibles 

    Exemples :
    >>> forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
    >>> forest.get_exit("N") == cave
    >>> forest.get_exit_string()
    Sorties: N, E, S
    >>> forest.get_long_description()
    Vous entendez une brise légère à travers la cime des arbres. \n\n Sorties : N, E, S
    La classe Room permet de donner une description de la et le nom de la pièce dans laquelle le joueur se situe et également les différentes sorties possibles

    Attributs : 
    name : str 
    description : str 
    exits : dict 

    Méthodes : 
    get_exit(self, direction)
    get_exit_string(self)
    get_long_description(self)

    Exemples : 
    >>> 

    >>>

    >>> 
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    


    


