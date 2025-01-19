"class command"

class Command:
    """
    Représente une commande dans le jeu

    Attributs:
    ----------
    command_word : str        > le mot-clé de la commande
    help_string : str         > description / aide associée à la commande
    action : fonction         > fonction à exécuter lorsque la commande est utilisée
    number_of_parameters : int > nombre de paramètres nécessaires pour exécuter la commande

    Méthodes:
    ---------
    __str__():       > représentation textuelle de la commande
    """

    def __init__(self, command_word, help_string, action, number_of_parameters):
        "le constructeur"

        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self):
        "représentation textuelle"
        return  self.command_word \
                + self.help_string
