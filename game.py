"Classe Game"

# Importation
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:
    """
    La classe Game gère l'ensemble du jeu (les pièces, les objets, les commandes et les
    interactions avec le joueur).

    Attributs :
    -----------
    finished : bool                > indicateur si le jeu est terminé
    rooms : list                   > liste des pièces disponibles dans le jeu
    commands : dict                > dictionnaire des commandes disponibles et l
                                     leurs actions associées
    player : Player                > représente le joueur
    artefactrouge : Item           > artefact rouge
    artefactbleu : Item            > artefact bleu
    artefactvert : Item            > artefact vert

    Méthodes :
    ----------
    __init__(self)                 > le constructeur de la classe Game
    setup(self)                    > configure les commandes, les pièces, les objets et les PNJ
    play(self)                     > lance le jeu, gère le déroulement de la partie
    process_command(self, command_string) > traite la commande entrée 
                                            par le joueur
    print_welcome(self)            > affiche le message de bienvenue et les 
                                     détails de la pièce actuelle
    fin_jeu(self)                  > vérifie si le joueur est mort ou si le jeu est terminé
    """

    def __init__(self):
        "Le constructeur"

        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

        self.artefactrouge = Item("artefactrouge", 2)
        self.artefactbleu = Item("artefactbleu", 2)
        self.artefactvert = Item("artefactvert", 2)

    def setup(self):
        "Fonction qui configure les commandes, les pièces, les objets et les PNJ"

        # Setup des commandes utiles
        aide = Command("aide", " : afficher cette aide", Actions.aide, 0)
        self.commands["aide"] = aide
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction", Actions.go, 1)
        self.commands["go"] = go
        look = Command("look", " : voir les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un objet se trouvant dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : jeter un objet de ton inventaire", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : regarder son inventaire", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk", " : parler à un PNJ", Actions.talk, 1)
        self.commands["talk"] = talk
        choose = Command("choose", " : choisir une des propositions proposées", Actions.choose, 1)
        self.commands["choose"] = choose
        attack = Command("attack", " : attaquer un pnj ou un mob", Actions.attack, 1)
        self.commands["attack"] = attack
        escape = Command("escape", " : pour vous enfuir en cas de danger", Actions.escape, 0)
        self.commands["escape"] = escape
        use = Command("use", " : pour utiliser un objet dans votre inventaire", Actions.use, 1)
        self.commands["use"] = use
        stats = Command("stats", " : pour regarder ton niveau de vie, faim, soif", Actions.stats, 0)
        self.commands["stats"] = stats
        sacrifice = Command("sacrifice", " : pour vous sacrifier ou un allié", Actions.sacrifice, 1)
        self.commands["sacrifice"] = sacrifice


        # Setup des rooms
        plage = Room("plage", "Vous vous réveillez sur une plage, entouré de dinosaures," \
        "sans aucun souvenirs." \
        " Au loin, se trouve un portail lumineux très étrange.\n" \
        "Trouvez les 3 artefacts et n'oubliez pas de les récupérer afin de" \
        " pouvoir vous échapper d'ici par ce portail !")
        self.rooms.append(plage)

        falaise = Room("falaise", "Vous grimpez une falaise pour avoir une vue d’ensemble." \
        " A la moitié de l'escalade, vous perdez l’équilibre et tombez." \
        " Vous succombez aux dégâts de chute.")
        self.rooms.append(falaise)

        clairiere = Room("clairiere","Vous êtes maintenant dans une clairiere et" \
        " vous voyez au loin, à côté d'un étang, un groupe de tricératops.")
        self.rooms.append(clairiere)

        ruines = Room("ruines", "Vous tombez nez à nez sur une structure en ruines.")
        self.rooms.append(ruines)

        etang = Room("etang", "Vous avez suivi discrètement les tricératops jusqu'à l'étang." \
        " Vous buvez jusqu'à être rassasié.")
        self.rooms.append(etang)

        canyon = Room("canyon", "Vous vous dirigez vers un petit canyon rocheux." \
        " Vous buvez jusqu'à être rassasié. Et, vous apercevez un castor géant transportant" \
        " des branches.")
        self.rooms.append(canyon)

        ruines_piece_central = Room("Pièce centrale des ruines", "Vous marchez accidentellement" \
        " sur une dalle qui ouvre une trappe.")
        self.rooms.append(ruines_piece_central)

        ruines_couloir = Room("Couloir des ruines", "Vous avancez prudemment dans le couloir." \
        " Une faible lumière pointe sur un coffre.")
        self.rooms.append(ruines_couloir)

        grotte = Room("Intérieur de la grotte de la Plaine", "Vous pénétrez dans la grotte" \
        " et vous rencontrez un PNJ blessé. Parlez-lui")
        self.rooms.append(grotte)

        camp = Room("camp", "Vous entrez dans un camp abandonné.")
        self.rooms.append(camp)

        foret = Room("foret", "Vous vous enfoncez dans la fôret mais des dinosaures vous repèrent" \
        " et vous poursuivent. Essouflé, les dinosaures vous rattrapez. Vous succombez aux dégâts.")
        self.rooms.append(foret)

        falaise_rocheuse = Room("falaise rocheuse", "Vous êtes sur une falaise rocheuse.")
        self.rooms.append(falaise_rocheuse)

        marecage = Room("marecage", "Vous arrivez dans une zone marécageuse.")
        self.rooms.append(marecage)

        sentier_degage = Room("Sentier dégagé", "Vous avez emprunté le chemin du sentier dégagé." \
        " Vous voyez un insecte géant en train de manger. Vous pouvez soit les attaquer," \
        " soit tenter de vous enfuir.")
        self.rooms.append(sentier_degage)

        temple = Room("temple", "Vous vous trouvez devant l'entrée d'un temple.")
        self.rooms.append(temple)

        temple_passage = Room("Passage du temple", "Vous entrez dans le temple.")
        self.rooms.append(temple_passage)

        labyrinthe = Room("Labyrinthe du temple", "Vous vous enfoncez dans le labyrinthe" \
        " et des insectes venimeux surgissent. Vous succombez à vos blessures.")
        self.rooms.append(labyrinthe)

        vallee_hostile = Room("Vallée hostile","Vous êtes maintenant dans la zone" \
        " de la vallée hostile.")
        self.rooms.append(vallee_hostile)

        montagne = Room("montagne", "Vous montez une montagne et vous rencontrez un groupe" \
        " de PNJ hostiles. Vous pouvez soit les attaquer, soit tenter de vous enfuir.")
        self.rooms.append(montagne)

        campement = Room("campement", "En rentrant dans le campement, vous tombez sur un PNJ" \
        " hostile affaibli. Vous pouvez soit l'attaquer, soit tenter de vous enfuir.")
        self.rooms.append(campement)

        jardin = Room("jardin", "Vous pénétrez dans le jardin gardé par un Rex.")
        self.rooms.append(jardin)

        salle_rex = Room("salle du Rex", "Vous entrez dans la salle du Rex, le détenteur" \
        " de l'artefact rouge. Derrière lui se trouve le portail que vous avez vu en" \
        " arrivant sur cette île.\nLe seul moyen pour passer outre cette salle est" \
        " le sacrifice (vous ou Djivan).")
        self.rooms.append(salle_rex)

        portail = Room("portail", "Vous avez récupéré tous les artefacts." \
        " Deux choix secrets vous est alors proposé.")
        self.rooms.append(portail)

        plaine_nouveau = Room("plaine du nouveau monde", "Vous avez choisi de rester " \
        " sur l'île. Vous pouvez maintenant apprivoiser tous les dinosaures de cette île.")
        self.rooms.append(plaine_nouveau)

        laboratoire = Room("laboratoire", "Vous vous réveillez dans un grand laboratoire" \
        " et vous apprenez que vous avez été un testeur humain de nouvelles technologies" \
        " dont vous êtes le seul à revenir\n"
        "vivant.")
        self.rooms.append(laboratoire)



        # Setup des exits des rooms
        plage.exits = {"N" : falaise, "S" : clairiere, "O" : None, "E" : ruines}
        falaise.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        ruines.exits = {"N" : ruines_couloir, "S" : None, "O" : plage, "E" : ruines_piece_central}
        ruines_couloir.exits = {"N" : None, "S" : ruines, "O" : None, "E" : None}
        ruines_piece_central.exits = {"N" : None, "S" : None, "O" : ruines, "E" : None}
        clairiere.exits = {"N" : plage, "S" : canyon, "O" : None, "E" : etang}
        etang.exits = {"N" : None, "S" : grotte, "O" : clairiere, "E" : None}
        canyon.exits = {"N" : clairiere, "S" : None, "O" : None, "E" : grotte}
        grotte.exits = {"N" : etang, "S" : camp, "O" : canyon, "E" : None}
        camp.exits = {"N" : grotte, "S" : falaise_rocheuse, "O" : None, "E" : foret}
        foret.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        falaise_rocheuse.exits = {"N" : camp, "S" : marecage, "O" : None, "E" : None}
        marecage.exits = {"N" : falaise_rocheuse, "S" : None, "O" : temple, "E" : sentier_degage}
        sentier_degage.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        temple.exits = {"N" : None, "S" : temple_passage, "O" : labyrinthe, "E" : temple}
        temple_passage.exits = {"N" : temple, "S" : vallee_hostile, "O" : None, "E" : None}
        labyrinthe.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        vallee_hostile.exits = {"N" : temple_passage, "S" : campement, "O" : None, "E" : montagne}
        montagne.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        campement.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        jardin.exits = {"N" : montagne, "S" : salle_rex, "O" : campement, "E" : None}
        salle_rex.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        portail.exits = {"N" : None, "S" : None, "O" : plaine_nouveau, "E" : laboratoire}
        plaine_nouveau.exits = {"N" : None, "S" : None, "O" : None, "E" : None}
        laboratoire.exits = {"N" : None, "S" : None, "O" : None, "E" : None}

        # Setup du joueur et sa pièce de départ
        self.player = Player(input("\nEntrez votre pseudo: "))
        self.player.current_room = plage

        # Création et ajout des items (qui se trouvent dans les pièces)
        couteau = Item("couteau", 2)
        pansement = Item("pansement", 0.25)
        baie = Item("baie", 0.1)
        bois = Item("bois", 1.5)
        eau = Item("eau", 0.1)


        ruines_piece_central.add_item(couteau)
        ruines_couloir.add_item(baie)
        etang.add_item(baie)
        camp.add_item(baie)
        temple.add_item(baie)
        temple.add_item(eau)
        jardin.add_item(eau)
        montagne.add_item(baie)
        camp.add_item(pansement)
        falaise_rocheuse.add_item(self.artefactvert)
        temple.add_item(self.artefactbleu)
        canyon.add_item(bois)



        # Création de PNJ
        grotte.characters["Djivan"] = Character("Djivan", "un homme blessé", grotte, ["... (suivant)\n", "\nTu cherches les artefacts toi aussi j'imagine. De nombreuses personnes ont sollicité mon aide pour les trouver...\nJe peux t'aider également si tu réponds correctement à mon énigme. (suivant)\n","\nJe suis toujours devant toi, mais tu ne peux jamais m’atteindre. Qui suis-je ? \n- 1) L'ombre \n- 2) L'avenir \n- 3) Le vent\n","\nJe suis toujours devant toi, mais tu ne peux jamais m’atteindre. Qui suis-je ? \n- 1) L'ombre \n- 2) L'avenir \n -3) Le vent\n", "\nJe suis toujours devant toi, mais tu ne peux jamais m’atteindre. Qui suis-je ? \n- 1) L'ombre \n- 2) L'avenir \n -3) Le vent\n","\nJe suis toujours devant toi, mais tu ne peux jamais m’atteindre. Qui suis-je ? \n- 1) L'ombre \n- 2) L'avenir \n -3) Le vent\n"])
        montagne.characters["Groupe"] = Character("Groupe", "groupe de 3 PNJ hostiles", montagne, ["Nous ne souhaitons pas discuter"])
        campement.characters["PNJ"] = Character("PNJ", "un PNJ hostile", campement, ["Partez !"])
        sentier_degage.characters["Araignée"] = Character("Araignée", "une araignée géante", sentier_degage, ["..."])
        


    def play(self):
        "lance le jeu, gère le déroulement de la partie"
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))
            self.fin_jeu()

    def process_command(self, command_string) -> None:
        "Traite la commande entrée par le joueur"

        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands.keys():
            return False

        command = self.commands[command_word]
        command.action(self, list_of_words, command.number_of_parameters)

        if command_word == "go":
            self.player.boire_room()
            self.player.perte_soif_faim()

            print(self.player.current_room.get_inventoryy())

            if self.player.previous_room.characters.get("Djivan"):
                self.player.previous_room.characters["Djivan"].follow_joueur(self.player)

            if len(self.player.current_room.characters) != 0:
                print("Il y a les PNJ suivants dans la pièce:")
                copie = list(self.player.current_room.characters.values())
                for characters in copie:
                    print(f"    - {characters}\n")

            print(self.player.current_room.get_exit_string())
            print("_____________________________________________"\
            "_____________________________________________________"\
            "_________________________________")
            print("\n")
        return True


    def print_welcome(self):
        "Affiche le message de bienvenue et les détails de la pièce actuelle"

        print("\nEntrez 'aide' pour avoir la liste des commandes possibles.")
        print("_____________________________________________"\
        "_____________________________________________________"\
        "_________________________________")
        print(self.player.current_room.get_long_description())
        print(self.player.current_room.get_inventoryy())
        print(self.player.current_room.get_exit_string())
        print("_____________________________________________"\
        "_____________________________________________________"\
        "_________________________________")
        print("\n")

    def fin_jeu(self):
        "Vérifie si le joueur est mort ou si le jeu est terminé"
        if self.player.mort_ou_fin_jeu():
            self.finished = True
            return "\t"
        return False


def main():
    "Fonction main"
    Game().play()

if __name__ == "__main__":
    main()
