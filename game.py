# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)
        basement = Room("Basement", "dans le sous sol de la maison. D'effroyables bruits proviennent des armoires.")
        self.rooms.append(basement)
        cabane = Room("Cabane", "dans une cabane. Les toiles d'araignées remplissent la cabane.")
        self.rooms.append(cabane)

        # Create exits for rooms
        forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None, "U" : cabane, "D" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None, "U" : None, "D" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave, "U" : None, "D" : None}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle, "U" : None, "D" : None}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None, "U" : None, "D" : basement}
        basement.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : castle, "D" : None}
        cabane.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : forest}


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print nothing
        if command_word not in self.commands.keys():
            return      
            
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
