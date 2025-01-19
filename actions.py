"Class Actions"

import random
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    La classe Actions regroupe l'ensemble des commandes/actions
    que le joueur peut exécuter dans le jeu.


    Méthodes :
    ----------
    go : bool       > permet au joueur de se déplacer dans une direction donnée
    quit : bool     > mettre fin au jeu
    aide : bool     > affiche la liste des commandes disponibles
    look : bool     > examiner la pièce (objets et PNJ présents)
    take : bool     > prendre un objet dans la salle actuelle
    drop : bool     > jeter un objet de l'inventaire du joueur
    check : bool    > afficher l'inventaire du joueur
    talk : bool     > parler à un PNJ dans la salle actuelle
    choose : bool   > faire un choix (énigme)
    attack : bool   > attaquer un ennemi / PNJ hostile
    escape : bool   > permet au joueur de s'échapper dans une des sorties disponibles
    stats : bool    > afficher les statistiques du joueur (vie, faim, soif)
    use : bool      > utiliser un objet se trouvant dans l'inventaire du joueur
    secrificie : bool  > se sacrifier ou sacrifier un PNJ allié
    """

    def go(game, list_of_words, number_of_parameters):
        """permet au joueur de se déplacer dans une direction donnée"""

        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]

        directions = {
        "N": "N", "NORD": "N", "Nord": "N", "nord": "N",
        "E": "E", "EST": "E", "Est": "E", "est": "E",
        "S": "S", "SUD": "S", "Sud": "S", "sud": "S",
        "O": "O", "OUEST": "O", "Ouest": "O", "ouest": "O",
        "D": "D", "DOWN": "D", "Down": "D", "down": "D",
        "U": "U", "UP": "U", "Up": "U", "up": "U"
        }
        direction = directions.get(direction)

        player.move(direction)
        return True


    def quit(game, list_of_words, number_of_parameters):
        """mettre fin au jeu"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        msg = f"\nMerci d'avoir joué ! \n"
        print(msg)
        game.finished = True
        return True

    def aide(game, list_of_words, number_of_parameters):
        """affiche la liste des commandes disponibles"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True


    def look(game, list_of_words, number_of_parameters):
        """examiner la pièce (objets et PNJ présents)"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if len(game.player.current_room.inventory) == 0:
            print("Il n'y a aucun objet dans la pièce")
        else:
            print("On voit:")
            for item in game.player.current_room.inventory.values():
                print(f"    - {item}")

        if len(game.player.current_room.characters) == 0:
            print("\nIl n'y aucun PNJ dans la pièce")
        else:
            print("\n Il y a:")
            for characters in game.player.current_room.characters.values():
                print(f"    - {characters} \n")


    def take(game, list_of_words, number_of_parameters):
        """prendre un objet dans la salle actuelle"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        objet = list_of_words[1]
        copie_dict_keys = list(game.player.current_room.inventory.keys())
        copie_dict = list(game.player.inventory.keys())

        if objet in copie_dict_keys:
            item = game.player.current_room.inventory[objet]
            weight_total = game.player.weight + item.weight

            if weight_total <= game.player.max_weight :
                game.player.inventory[objet] = item
                game.player.weight += item.weight

                del game.player.current_room.inventory[objet]

                print(f"Vous avez pris l'objet '{objet}'\n")
                print(f"Poids actuel : {round(game.player.weight,2)}/{game.player.max_weight}")
                print(game.player.get_inventory())

            else:
                print(f"Votre inventaire est trop lourd, retirez un objet : {weight_total}/{game.player.max_weight}")

        elif objet in copie_dict :
            print(f"L'objet '{objet}' est déjà dans votre inventaire")
        else:
            print(f"L'objet '{objet}' n'est pas dans présent dans la pièce")


    def drop(game, list_of_words, number_of_parameters):
        """jeter un objet se trouvant dans l'inventaire du joueur"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        objet = list_of_words[1]
        copie_dict = list(game.player.inventory.keys())
        if objet in copie_dict:
            game.player.current_room.inventory[objet] = game.player.inventory[objet]
            del game.player.inventory[objet]
            print(f"Vous avez déposé l'objet '{objet}'\n")
            print(f"Poids actuel : {round(game.player.weight,2)}/{game.player.max_weight}")
            print(game.player.get_inventory())
        else:
            print(f"L'objet '{objet}' n'est pas dans votre inventaire")


    def check(game, list_of_words, number_of_parameters):
        """afficher l'inventaire du joueur"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory())


    def talk(game, list_of_words,number_of_parameters):
        """parler à un PNJ se trouvant dans la salle du joueur"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        person = list_of_words[1]
        for key,value in game.player.current_room.characters.items():
            if key.upper() == person.upper():
                value.get_msg()
                return True
        print(f"{person} n'est pas dans la salle.\n")
        return False

    def choose(game, list_of_words, number_of_parameters):
        """choisir parmis une des propositions possibles lors des énigmes"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        choice = list_of_words[1]

        if choice == "1":
            print("Ce n'était pas la bonne réponse. Retentes ta chance en reparlant à Djivan.\n")
        elif choice == "2":
            print("C'était la bonne réponse ! Djivan va désormais vous aider dans votre quête. Vous pouvez poursuivre votre chemin.\n")
        elif choice == "3":
            print("Ce n'était pas la bonne réponse. Retentes ta chance en reparlant à Djivan.\n")
        else:
            print("Choix invalide. Veuillez entrer 'choose 1', 'choose 2' ou 'choose 3'.\n")
        return False


    def attack(game, list_of_words, number_of_parameters):
        """attaquer un mob / PNJ hostile"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        ennemi = list_of_words[1]

        if ennemi == "Djivan":
            print("Vous ne pouvez pas attaquer Djivan.\n")
            return "\t"

        if ennemi == "Araignée":
            liste = ["Victoire", "Victoire", "Victoire", "Défaite"]
            resultat = random.choice(liste)
            if resultat == "Défaite":
                print("Araignée vous a tué. Votre personnage est mort.\n")
                game.finished = True
                return True
            else:
                print("Vous avez tué Araignée !\n")
                return False

        if ennemi == "Groupe":
            print("Les PNJ hostiles vous ont tué. Votre personnage est mort.\n")
            game.finished = True
            return True

        if ennemi == "PNJ":
            print("Vous avez tué le PNJ hostile !\n")
            next_room = game.rooms[20]
            game.player.current_room = next_room
            print(game.player.current_room.get_long_description())
            print(game.player.current_room.get_inventoryy())

            if len(game.player.current_room.characters) != 0:
                print("Il y a les PNJ suivants dans la pièce:")
                copie = list(game.player.current_room.characters.values())
                for characters in copie:
                    print(f"    - {characters}\n")

            print(game.player.current_room.get_exit_string())
            print("_____________________________________________"\
            "_____________________________________________________"\
            "_________________________________")
            print("\n")
            return True


    def escape(game, list_of_words, number_of_parameters):
        """s'échapper dans une des exits de la current room du joueur"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        salles_escapable = ["Sentier dégagé", "montagne", "campement"]
        if game.player.current_room.name in salles_escapable:
            chance = ["Succès", "Succès", "Succès", "Succès", "Echec"]
            resultat = random.choice(chance)

            if resultat == "Succès":

                if game.player.current_room.name == "Sentier dégagé":
                    next_room = game.rooms[12]
                elif game.player.current_room.name == "montagne":
                    next_room = game.rooms[20]
                elif game.player.current_room.name == "campement":
                    next_room = game.rooms[20]

                game.player.current_room = next_room
                print("Vous vous échappez avec succès !")
                print(game.player.current_room.get_long_description())
                print(game.player.current_room.get_inventoryy())

                if len(game.player.current_room.characters) != 0:
                    print("Il y a les PNJ suivants dans la pièce:")
                    copie = list(game.player.current_room.characters.values())
                    for characters in copie:
                        print(f"    - {characters}\n")

                print(game.player.current_room.get_exit_string())
                print("_____________________________________________"\
                "_____________________________________________________"\
                "_________________________________")
                print("\n")
                return True

        liste = ["Sentier dégagé", "montagne", "campement"]
        if game.player.current_room.name not in liste:
            print("Vous n'avez pas besoin de fuir quoi que ce soit.\n")
            return False

        else:
            print("Vous n'avez pas réussi à vous échapper. Votre personnage meurt.\n")
            game.finished = True
            return False

    def stats(game, list_of_words, number_of_parameters):
        """afficher les statistiques du joueur"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(f"Votre vie : {game.player.sante}/{game.player.max_sante}")
        print(f"Votre faim : {game.player.faim}/{game.player.max_faim}")
        print(f"Votre soif : {game.player.soif}/{game.player.max_soif}\n")
        return True


    def use(game, list_of_words, number_of_parameters):
        """utiliser un objet se trouvant dans l'inventaire du joueur"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        ressource = list_of_words[1]

        if ressource in player.inventory:
            if ressource=="baie":
                player.faim = min(player.faim + 20, 100)
                print(f"Vous avez mangé une baie. Votre barre de faim est de : {player.faim}/{player.max_faim}.\n")
            elif ressource=="eau":
                player.soif = min(player.soif + 20, 100)
                print(f"Vous avez bu. Votre barre de soif est de : {player.soif}/{player.max_soif}.\n")
            elif ressource=="pansement":
                player.sante = min(player.sante + 30, 100)
                print(f"Vous avez utilisé un pansement. Votre santé est de {player.sante}/{player.max_sante}.\n")
            else:
                print(f"Vous ne pouvez pas utiliser {ressource}.\n")
        else:
            print(f"Vous n'avez pas ou plus de {ressource} dans votre inventaire.\n")


    def sacrifice(game, list_of_words, number_of_parameters):
        """se sacrifier ou sacrifier un PNJ allié"""

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        person = list_of_words[1]
        liste_personnes = ["myself", "Djivan"]
        if game.player.current_room.name == "salle du Rex":
            if person in liste_personnes:
                if person == "myself":
                    print("Vous attirez l'attention du Rex pour sauver Djivan. Le Rex vous rattrape. Votre personnage est mort.\nMerci d'avoir joué!\n")
                    game.finished = True
                if person == "Djivan":
                    print("Djivan se sacrifie. Le Rex le poursuit et vous avez le temps de récupérer l'artefact rouge.\n")
                    game.player.inventory["artefactrouge"] = game.artefactrouge
                    print(game.player.get_inventory())

                    liste = ["artefactbleu", "artefactvert", "artefactrouge"]
                    if all(item in game.player.inventory for item in liste):
                        next_room = game.rooms[22]
                        game.player.current_room = next_room
                        print(game.player.current_room.get_long_description())
                        print(game.player.current_room.get_inventoryy())

                        if len(game.player.current_room.characters) != 0:
                            print("Il y a les PNJ suivants dans la pièce:")
                            copie = list(game.player.current_room.characters.values())
                            for characters in copie:
                                print(f"    - {characters}\n")

                        print(game.player.current_room.get_exit_string())
                        print("_____________________________________________"\
                        "_____________________________________________________"\
                        "_________________________________")
                        print("\n")
                        return True
                    else:
                        print("Vous ne possédez pas tous les artefacts requis pour dévérouiller le portail. Récupérez les tous et revenez devant le portail.\n")
            else:
                print("Vous ne pouvez pas utiliser cette commande sur cet individu.\n")
        else:
            print("Vous ne pouvez pas encore utiliser cette commande. L'utilisation de cette commande vous sera communiquer quand vous serez dans la salle adéquate.\n")
