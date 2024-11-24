# Define the Room class.

class Room:
    """
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
